import os
import re

with open(".\input.txt") as f:
    game_details = f.read()

global game_config

game_config = {
    "red": 12,
    "green": 13,
    "blue": 14
}

#Convert the input into list of games
games_list = game_details.split("\n")

plausible_game_ids = []
id_score = 0

#Get each set from game list and check possibility
for game in games_list:
    
    sets = game.split(";")
    invalid = False
    
    #Check if each set is possible
    for game_set in sets:
        
        green_balls = re.findall("(\d+)(?=\s+green)", game_set)
        if len(green_balls) > 0:
            green_balls = int(green_balls[0])
        else:
            green_balls = 0
        red_balls = re.findall("(\d+)(?=\s+red)", game_set)
        if len(red_balls) > 0:
            red_balls = int(red_balls[0])
        else:
            red_balls = 0
        blue_balls = re.findall("(\d+)(?=\s+blue)", game_set)
        if len(blue_balls) > 0:
            blue_balls = int(blue_balls[0])
        else:
            blue_balls = 0

        if green_balls > game_config["green"] or red_balls > game_config["red"] or blue_balls > game_config["blue"]:
            invalid = True

    if not invalid:
        game_id = re.findall("(?:Game\s)(\d+)", game)[0]
        id_score += int(game_id)


print(id_score)
