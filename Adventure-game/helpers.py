import json


def open_json(name):
    with open(name) as file:
        x = json.load(file)
        file.close()

    return x


def save_json(player_list, defeated):
    players = [{
            "name": player.get_name(),
            "hp": player.get_hp(),
            # "max_hp": player.get_max_hp(),
            # "voice_lines": player.get_voice_lines(),
            # "games_won": player.get_games_won()
    } for player in player_list]
    players = json.dumps(players)
    defeated = [player.__dict__ for player in defeated]
    defeated = json.dumps(defeated)

    clearing = open("game.json", "w")
    clearing.write("")
    clearing.close()

    with open("game.json", "a") as file:
        file.write(players)
        file.write("\n")
        file.write(defeated)
        file.write("\n")
        file.close()
