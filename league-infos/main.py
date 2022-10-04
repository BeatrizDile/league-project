import json
from api_call import Player

with open("summoners_data.json", "r") as file:
    summoners_data_file = json.load(file)

players_dict = summoners_data_file["players"]
summoner_exists = False
i = 0

for name in players_dict:
    summoner_available = name["summoner_name"].lower().replace(" ", "")
    old_lp = summoners_data_file["players"][i]["lp_solo"]
    player = Player(summoner_available)
    player.players_info()

    if player.lp_solo > old_lp:
        plus_lp = player.lp_solo - old_lp
        print(f"{player.summoner_name} gained +{plus_lp} PDL!\n")
        player.save_data_to_file()

    elif player.lp_solo < old_lp:
        loss_lp = player.lp_solo - old_lp
        print(f"{player.summoner_name} lost {loss_lp} PDL!\n")
        player.save_data_to_file()

    else:
        print(f"{player.summoner_name} still has {player.lp_solo} PDL.\n")
        player.save_data_to_file()

    i += 1

