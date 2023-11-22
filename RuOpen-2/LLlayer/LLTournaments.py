from IOLayer.IOWrapper import IOWrapper
from ModelClasses.ModelTournament import ModelTournament

class LLTournament:

    def __init__(self):
        
        self.IOWrapper = IOWrapper()


    def addNewTournament(self, new_tournament: dict):
    
      
        # Get all tournament registered in system
        tournament_list = self.getAllTournaments()
        
        # Make new instance of Tournament Class for new tournament
        new_tournament_class = ModelTournament(new_tournament["id"], new_tournament["name"] ,new_tournament["status"], \
                                               new_tournament["start_date"],new_tournament["end_date"], \
                                               new_tournament["host_name"], new_tournament["rounds"])

        
        # Append newly made tournament class to current tournaments in system
        for tournament in tournament_list:
            
            if tournament.id == new_tournament_class.id:
                tournament_list.remove(tournament)
        
        tournament_list.append(new_tournament_class)

        # Sending new tournament list to IO layer to be stored to JSON
        self.IOWrapper.StoreTournamentToFile(tournament_list)


    def addNewTournamentChangedDate(self, model_object):
        """Adds the tournament in which had the date changed back to the list of tournaments"""
        tournament_list = self.getAllTournaments()

        for tournament in tournament_list:
            
            if tournament.id == model_object.id:
                tournament_list.remove(tournament)
        
        tournament_list.append(model_object)
        self.IOWrapper.StoreTournamentToFile(tournament_list)


    def removeTournament(self, id: int):
        """Removes tournament with given ID from list of tournaments"""
        tournaments_list = self.getAllTournaments()
        new_tournaments_list = [i for i in tournaments_list if i.id != id]
        self.IOWrapper.StoreTournamentToFile(new_tournaments_list)
        
        if len(new_tournaments_list) != tournaments_list:
            return "Succesfully removed!"
        else:
            return "No ID matching..."
         

    def startTournament(self, id):

        """
        Finds tournament that matches ID, returns 0 if not found, returns -1 if tournament has already started and returns -2 if tournament has finished.
        Otherwise returns "Success" <- annavega nuna
        Returns 0 if no matching tournament was found.
        """

        return self.changeStatus(id, "not started")
        
    
    def finishTournament(self, id):
        
        """
        Finds tournament that matches ID, returns 0 if not found, returns -1 if tournament has not started and returns -2 if tournament has finished.
        Otherwise returns "Success" <- annavega nuna.
        Returns 0 if no matching tournament was found.
        """

        return self.changeStatus(id, "ongoing")


    def changeStatus(self, id, start_status):

        """
        Takes in id and what status starting as (can be either "not started" or "ongoing").
        Returns -1 if tournament was already ongoing when trying to start
        Returns -2 if tournament was not started when trying to finish.
        Returns -3 if tournament was already finished.
        Returns 0 if no matching tournament was found.
        """
        # load all tournaments
        tournament_list = self.getAllTournaments()
        
        id_found = False

        for i in range(len(tournament_list)):
            
            if tournament_list[i].id == id:

                if tournament_list[i].status == "finished":
                        return -3 # Raise tournament already finished

                elif (tournament_list[i].status == "ongoing" and start_status == "not started"):
                    # if tournament was already ongoing when trying to start
                    return -1 

                elif (tournament_list[i].status == "not started" and start_status == "ongoing"):
                    # if tournament was already ongoing when trying to start
                    return -2

                if tournament_list[i].status == "not started" and start_status == "not started":
                        tournament_list[i].status = "ongoing"
                        id_found = True

                elif tournament_list[i].status == "ongoing" and start_status == "ongoing":
                        tournament_list[i].status = "finished"
                        id_found = True
        
        if id_found == True:
            # Sending new tournament list to datalayer
            self.IOWrapper.StoreTournamentToFile(tournament_list)
            return "Success" 
        return 0 # if id_found is false (no matching tournament was found)
    
    def getAllTournaments(self):
        """Loads all tournaments from file and returns them as a list"""
        tournaments_list = self.IOWrapper.LoadTournamentsFromFile()
        return tournaments_list


    def getTournamentsByStatus(self, status):
        """Returns a list of tournaments with the given status"""
        tournaments_list = self.IOWrapper.LoadTournamentsFromFile()
        status_tournaments = [i for i in tournaments_list if i.status == status]
        return status_tournaments


    def getOngoingTournaments(self):
        """Returns a list of tournaments that are ongoing"""
        return self.getTournamentsByStatus("ongoing")


    def getFinishedTournaments(self):
        """Returns a list of tournaments that are finished"""
        return self.getTournamentsByStatus("finished")


    def getFutureTournaments(self):
        """Returns a list of tournaments that have not started"""
        return self.getTournamentsByStatus("not started")


    def getTournamentByID(self, ID):
        """Returns a list of tournaments with the given ID"""
        tournament_list = []
        tournaments = self.IOWrapper.LoadTournamentsFromFile()

        for tournament in tournaments:
            if tournament.id == ID:
                tournament_list.append(tournament)
        
        return tournament_list

    
    