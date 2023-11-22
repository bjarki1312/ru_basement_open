import json
import os
from ModelClasses.ModelPlayer import ModelPlayer

class IOPlayers:

    def __init__(self):
        """Constructor that sets the file name, and creates the file if it doesn't exist."""       
        
        path = f"JsonData{os.sep}Players.json"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)

    
    def StorePlayersToFile(self, data):
        """Stores Players to the file."""
        
        new_players_list = []

        for player in data:
            new_players_list.append({"id": player.id, "player_name": player.name, "isCaptain" : player.isCaptain,\
                                 "email" : player.email, "ssn": player.ssn, "birthday": player.birthday,\
                                 "address": player.address, "home_num": player.home_number, "cell_num": player.cell_number,\
                                 "club_name": player.club, "team_name": player.team, "score": player.score, "qp": player.qp})
            
        with open(self.file_name, 'w') as file_object:  #open the file in write mode
            json.dump(new_players_list, file_object, indent = 4) 

    def LoadPlayersFromFile(self):
        """Loading all players registered in system, and returns a list of ModelPlayer objects"""
        
        players_list = []
        data_stream = open(self.file_name)
        players = json.load(data_stream)

        for player in players:
            players_list.append(ModelPlayer(player["id"], player["player_name"], player["isCaptain"], player["email"], player["ssn"],\
                                player["birthday"], player["address"], player["home_num"], player["cell_num"], player["club_name"], player["team_name"], player["score"],\
                                player["qp"]))
        
        return players_list
