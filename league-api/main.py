import json
from api_call import Player

with open("summoners_data.json", "r") as file:
    summoners_data_file = json.load(file)

players_dict = summoners_data_file["players"]
elo_list = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM"]
rank_list = ["I", "II", "III", "IV"]


def identify_elo(old_elo, current_elo):
    old_elo_index = elo_list.index(old_elo)
    current_elo_index = elo_list.index(current_elo)

    if current_elo_index > old_elo_index:
        print(f"Got a higher elo: from {old_elo} {old_solo_rank} to {current_elo} {player.rank_solo}.\n")
    else:
        print(f"Got a lower elo: from {old_elo} {old_solo_rank} to {current_elo} {player.rank_solo}.\n")


def identify_rank(old_rank, current_rank):
    old_rank_index = rank_list.index(old_rank)
    current_rank_index = rank_list.index(current_rank)

    if current_rank_index < old_rank_index:
        print(f"Got a higher rank: from {old_solo_elo} {old_rank} to {player.elo_solo} {current_rank}\n.")
    else:
        print(f"Got a lower rank: from {old_solo_elo} {old_rank} to {player.elo_solo} {current_rank}\n.")


for i, name in enumerate(players_dict):
    summoner_available = name["summoner_name"].lower().replace(" ", "")
    old_lp = summoners_data_file["players"][i]["lp_solo"]
    old_solo_elo = summoners_data_file["players"][i]["elo_solo"]
    old_solo_rank = summoners_data_file["players"][i]["rank_solo"]
    player = Player(summoner_available)
    player.players_info()

    if player.elo_solo == old_solo_elo and player.rank_solo == old_solo_rank:
        print("Same elo and same rank.")
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

    elif player.rank_solo != old_solo_rank:
        identify_rank(old_solo_rank, player.rank_solo)
        player.save_data_to_file()

