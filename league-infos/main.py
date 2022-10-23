import json
from api_call import Player

with open("summoners_data.json", "r") as file:
    summoners_data_file = json.load(file)

players_dict = summoners_data_file["players"]
elo_list = ["BRONZE", "SILVER", "GOLD", "PLATINUM"]


def identify_elo(old_elo, current_elo):
    old_elo_index = elo_list.index(old_elo)
    current_elo_index = 0
    for elo in elo_list:
        if elo == current_elo:
            current_elo_index = elo_list.index(current_elo)

    if current_elo_index > old_elo_index:
        print(f"Got a higher elo: from {old_elo} to {current_elo}")
    else:
        print(f"Got a lower elo: from {old_elo} to {current_elo}")


for i, name in enumerate(players_dict):
    summoner_available = name["summoner_name"].lower().replace(" ", "")
    old_lp = summoners_data_file["players"][i]["lp_solo"]
    old_solo_elo = summoners_data_file["players"][i]["elo_solo"]
    player = Player(summoner_available)
    player.players_info()

    if player.elo_solo == old_solo_elo:
        print("Same elo.")
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

    elif player.elo_solo != old_solo_elo:
        identify_elo(old_solo_elo, player.elo_solo)
        player.save_data_to_file()

