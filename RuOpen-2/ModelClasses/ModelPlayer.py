class ModelPlayer:

    def __init__(self, id = None, name = None, isCaptain = None, email = None, ssn = None, birthday = None, address=None, home_num=None, cell_num=None, club = None, team=None, score=None, qp=None): # Might not be correct info, this is just a guess
        
        self.id = id
        self.name = name
        self.isCaptain = isCaptain
        self.email = email
        self.ssn = ssn
        self.birthday = birthday
        self.address = address
        self.home_number = home_num
        self.cell_number = cell_num
        self.club = club
        self.team = team
        self.score = score
        self.qp = qp
        
        

    def makeCaptain(self): # Isn't in the UML, but I think it might be useful, annars bara eyða
        """Makes player captain, returns True if successful, False if player is already captain"""
        
        if self.isCaptain == False:
            self.isCaptain = True
            return True
        else:
            return False
    
    def __str__(self) -> str:

        """Returns all attributes seperated by a comma"""
        
        return f"{self.player_id}, {self.name}, {self.email}, {self.social_security}, {self.birthday}, {self.address}, {self.home_number}, {self.cell_number}, {self.team}, {self.score}, {self.isCaptain}"

