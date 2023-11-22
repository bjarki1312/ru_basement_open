import json
import os
from ModelClasses.ModelClub import ModelClub

class IOClubs:

    def __init__(self):

        path = f"JsonData{os.sep}Clubs.json"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)  

    def StoreClubToFile(self, data): # data is ModelClub object   
        '''
        Stores a list of clubs to file

        Args:
            data (ModelClub list): list of clubs to be stored
        '''        
        new_data = []
        for i in data:
            new_data.append({"id": i.id, "name": i.name, "address": i.address, "phone_number": i.phone_number})
            

        with open(self.file_name, 'w') as file_object:  #open the file in write mode
            json.dump(new_data, file_object, indent = 4) 

    def LoadClubsFromFile(self):
        '''
        Gets a list of clubs from file

        Returns:
            ModelClub list: list of club objects
        '''        
        club_list = []
        data_stream = open(self.file_name)
        clubs = json.load(data_stream)
        
        for club in clubs:
            club_list.append(ModelClub(club["id"], club["name"], club["address"], club["phone_number"]))
        
        return club_list




   

   


