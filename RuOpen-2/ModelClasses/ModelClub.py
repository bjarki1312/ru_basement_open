class ModelClub:

    def __init__(self, tournament_id, name, address, phone_number):
        
        self.id = tournament_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        
        
    def __str__(self) -> str:
        """Returns all attributes seperated by a comma"""
        
        return f"{self.id}, {self.name}, {self.address}, {self.phone_number}"