from IOLayer.IOWrapper import IOWrapper
from LLlayer.LLTournaments import LLTournament
from ModelClasses.ModelClub import ModelClub

class LLClub:

    def __init__(self):
        """Constructor for LLClub, that initializes the IOWrapper"""

        self.IOWrapper = IOWrapper()

    def addNewClub(self, new_club):
        """Takes in a dict of a club, maps it to a Club object and appends to the file"""
        
        club_list = self.getAllClubs()
        club = ModelClub(new_club["id"], new_club["name"], new_club["address"], new_club["phone_number"])
        club_list.append(club)
        self.IOWrapper.StoreClubToFile(club_list)


    def removeClub(self, id):
        """Removes all clubs with matching id"""
        
        club_list = self.IOWrapper.LoadClubsFromFile()

        new_club_list = [i for i in club_list if i.id != id]
        self.IOWrapper.StoreClubToFile(new_club_list)
        if len(new_club_list) != club_list:
            return "Succesfully removed!"
        else:
            return "No ID matching..."

    
    def getAllClubs(self):
        """Returns list of all clubs"""
        
        clubs_list = self.IOWrapper.LoadClubsFromFile()
        return clubs_list
    
    
            
          
        



