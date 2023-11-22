import json
import os
from ModelClasses.ModelTeam import ModelTeam

class IOTeams:

    def __init__(self):
        """Constructor that sets the file name, and creates the file if it doesn't exist."""
        
        path = f"JsonData{os.sep}Teams.json"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)

    def StoreTeamToFile(self, data):
        """Stores the team to file"""

        new_team_list = []
        
        # For loop to convert each ModelTournament (class) back to dictionary 
        for team in data:
            new_team_list.append({"id": team.id, "club_name": team.club_name, "team_name" : team.team_name,\
                                 "home_or_away" : team.home_or_away, "Captain": team.captain, "Players": team.players,\
                                 "Count": team.count, "wins": team.wins, "loss": team.loss})
            
        with open(self.file_name, 'w') as file_object:  #open the file in write mode
            json.dump(new_team_list, file_object, indent = 4) 

        
    def LoadTeamsFromFile(self):
        """Loading all Teams registered in system, and returns a list of ModelTeam objects"""
        
        teams_list = []
        data_stream = open(self.file_name)
        teams = json.load(data_stream)
        
        for team in teams:
            teams_list.append(ModelTeam(team["id"], team["club_name"], team["team_name"], team["home_or_away"], team["Captain"], team["Players"], team["Count"], team["wins"], team["loss"]))
        
        return teams_list
