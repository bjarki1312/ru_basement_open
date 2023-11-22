import json
import os
from ModelClasses.ModelTournament import ModelTournament

class IOTournaments:

    def __init__(self):
        """Constructor that sets the file name, and creates the file if it doesn't exist."""
        
        path = f"JsonData{os.sep}Tournaments.json"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)       

    def StoreTournamentToFile(self, data):
        """Stores the tournament to file, and returns a list of ModelTournament objects"""
        
        # Make new instance of list to be stored with updated tournaments
        new_tournament_list = []
        
        # For loop to convert each ModelTournament (class) back to dictionary 
        for tournament in data:
            new_tournament_list.append({"id": tournament.id, "name": tournament.name, "status" : tournament.status, "start_date" : tournament.start_date,\
                                        "end_date": tournament.end_date, "host_name": tournament.host_name, "rounds": tournament.rounds})
            
        with open(self.file_name, 'w') as file_object:  #open the file in write mode
            json.dump(new_tournament_list, file_object, indent = 4) 


    def LoadTournamentsFromFile(self):
        '''Loading all Tournaments registered in system, and returns a list of ModelTournament objects'''
        
        tournaments_list = []
        data_stream = open(self.file_name)
        tournaments = json.load(data_stream)
        
        for tournament in tournaments:
            tournaments_list.append(ModelTournament(tournament["id"], tournament["name"], tournament["status"], tournament["start_date"], tournament["end_date"], tournament["host_name"], tournament["rounds"]))
        
        return tournaments_list
