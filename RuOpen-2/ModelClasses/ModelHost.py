class ModelHost:
    def __init__(self, id, name, phone_number) -> None:
        self.id = id
        self.name = name
        self.phone_number = phone_number

    def __str__(self) -> str:
        """Returns all attributes seperated by a comma"""

        return f"{self.id}, {self.name}, {self.phone_number}"