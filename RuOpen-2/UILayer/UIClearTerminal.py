import os
from datetime import datetime

class UIClearTerminal:

    def __init__(self):
        """Nothing to initialize"""

        pass
          
    def clear(self):
        """Clears the terminal screen"""
        
        os.system('cls' if os.name == 'nt' else 'clear')

    def printHeader(self, title, extra = [], bottom = ""):
        """Prints a header with a title and a bottom line"""

        print()
        print(f"{title :-^55}")
        print(f"{'B/b: Back' : ^55}")
        centered_args = [f"{i : <30}" for i in extra]
        
        if len(extra) != 0:
            print()
        for i in centered_args:
            print(f"{i : ^55}")
        print(f"{bottom :-^55}")

    def check_date(self, input):
        """Checks if the input is a valid date, else it returns the minimum date"""
        try:
            return datetime.strptime(input.replace("-", " "), "%d %m %Y")
        except ValueError:
            return datetime.min

