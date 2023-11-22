import json
import os
from ModelClasses.ModelGame import ModelGame


class IOGames:
    def __init__(self):
        """Constructor that sets the file name, and creates the file if it doesn't exist."""
        
        path = f"JsonData{os.sep}Games.json"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)

    def StoreGamesToFile(self, data): # data is a list of ModelGame objects
        """Stores the data to the file."""
        
        data_dict = []
        for i in data:
            data_dict.append({"id": i.id, "date": i.date, "round_nr": i.round_nr,"Game_type": i.game_type, "Home_team": i.home_team, "Away_team": i.away_team, "Home_player": i.home_player, "Away_player": i.away_player, "Home_leg": i.home_leg, "Away_leg": i.away_leg})

        with open(self.file_name, 'w') as data_stream:
            json.dump(data_dict, data_stream, indent = 4)
    
    def LoadGamesFromFile(self):
        """Loads the data from the file."""
        
        games_list = []
        data_stream = open(self.file_name)
        games = json.load(data_stream)
        
        for game in games:
            games_list.append(ModelGame(game["id"], game["date"], game["round_nr"], game["Game_type"], game["Home_team"], game["Away_team"], game["Home_player"], game["Away_player"], game["Home_leg"], game["Away_leg"]))

        return games_list
