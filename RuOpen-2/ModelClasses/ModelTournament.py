class ModelTournament:

    def __init__(self, tournament_id, name ,status, start_date, end_date, host_name, rounds):

        self.id = tournament_id
        self.name = name
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.host_name = host_name
        self.rounds = rounds
    
            
    def __str__(self) -> str:
        """Returns all attributes seperated by a commas"""
        
        return f"{self.id} {self.name} {self.status} {self.start_date} {self.end_date} {self.host_name} {self.rounds}"
            