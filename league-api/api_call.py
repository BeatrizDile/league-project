import json
import requests
import os


class Player:
    def __init__(self, name_given):
        self.given_summoner_name = name_given
        self.summoner_name = ""
        self.summoner_id = ""
        self.elo_solo = ""
        self.rank_solo = ""
        self.lp_solo = ""
        self.wins_solo = ""
        self.losses_solo = ""
        self.win_rate_solo = ""
        self.api_call()

    def api_call(self):
        api_key = os.environ["KEY"]

        summoner_info = requests.get(
            url=f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.given_summoner_name}?api_key="
                f"{api_key}")
        summoner_info.raise_for_status()
        summoner_data = summoner_info.json()
        self.summoner_id = summoner_data["id"]

        elo_info = requests.get(
            url=f"https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.summoner_id}?api_key={api_key}")
        elo_info.raise_for_status()
        elo_data = elo_info.json()

        for i, item in enumerate(elo_data):
            if item["queueType"] == "RANKED_SOLO_5x5":
                self.summoner_name = elo_data[i]["summonerName"]
                self.elo_solo = elo_data[i]["tier"]
                self.rank_solo = elo_data[i]["rank"]
                self.lp_solo = elo_data[i]["leaguePoints"]
                self.wins_solo = elo_data[i]["wins"]
                self.losses_solo = elo_data[i]["losses"]
                self.win_rate_solo = round((self.wins_solo * 100) / (self.wins_solo + self.losses_solo), 1)

    def players_info(self):
        print(f"{self.summoner_name}\n{self.elo_solo} {self.rank_solo}\nPDL: {self.lp_solo}\nWins: {self.wins_solo} - "
              f"Losses: {self.losses_solo} ({self.win_rate_solo}%)")

    def save_data_to_file(self):
        with open("summoners_data.json", "r") as file:
            summoners_data_file = json.load(file)

        players_dict = summoners_data_file
        summoner_to_update = {
                             "id": self.summoner_id,
                             "summoner_name": self.summoner_name,
                             "elo_solo": self.elo_solo,
                             "rank_solo": self.rank_solo,
                             "lp_solo": self.lp_solo,
                             "wins_solo": self.wins_solo,
                             "losses_solo": self.losses_solo
                            }

        for i, item in enumerate(players_dict["players"]):
            if self.given_summoner_name == item["summoner_name"].lower().replace(" ", ""):
                players_dict["players"][i] = summoner_to_update

                with open("summoners_data.json", "w") as file:
                    json.dump(players_dict, file, indent=7)
