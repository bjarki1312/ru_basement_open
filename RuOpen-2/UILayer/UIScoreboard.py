from UILayer.UIClearTerminal import UIClearTerminal 


class UIScoreboard:
    
    def __init__(self, home_team_name: str, home_players: list, away_team_name: str, away_players: list, date: str ) -> None:

        self.display_team_list = [
            ["|           ", "","","","","","","","","","","",],
            [" ","","","","","","","","","","","",]]
        self.importedTeamList = [[player.capitalize() for player in home_players],[player.capitalize() for player in away_players]]
        self.listOfTeams = [home_team_name.center(12), away_team_name.center(12)]
        self.home_team_score,self.away_team_score = 0,0
        self.Terminal = UIClearTerminal()

        self.date = "20:00 " + date
        self.game_count = 1

        self.getScoreList()
        self.getWidth(self.display_team_list)
        self.getLengthOfLongestName(self.display_team_list)
        
    def __str__(self) -> str:
        
        '''Returns the scoreboard filled out with the given content.'''
        # Colors can be added by using \033[1;30m. 
        # you can change the color by changing the number after the semicolon
        formattedPlayerList = self.getFormat(self.display_team_list)
        
        list_of_seperators = [
            "╬═══╬═══╬═════╬═══╬═══╬".center(self.WIDTH, "═"), #41
            "╩═══╩═══╬═════╬═══╩═══╩",                         #42
            "╩═══╩═══╩═════╩═══╩═══╩".center(self.WIDTH, "═"), #43
            "╦═══╦═══╦═════╦═══╦═══╦".center(self.WIDTH, "═"), #44
            "VS.".center(self.WIDTH-sum([len(team) for team in self.listOfTeams])), #45
            "".center(self.WIDTH, "═"),                         #46
            "  L1. L2.       L2. L1.".center(self.WIDTH),       #47
            "╦══════════════════════".center(self.WIDTH, "═"),  #48
            "╩══════════════════════".center(self.WIDTH, "═"),  #49
            " Quality Points ".center(self.WIDTH), #50
            ]        

        return ( #the number inside the {} correlate to the filler.
            "\033[1;30m{0}\n"                                                                                       #Date
            "╔{46}╗\n"
            "║\033[1;32m{39}\033[1;30m\033[1;31m{45}\033[1;30m\033[1;35m{40}\033[1;30m║\n"                          #Teams
            "╚{46}╝\n"
            "{47}\n"            #--------Start of the main scoreboard-------#
            "╔{44}╗\t\033[1;33mPlayer List:\033[1;30m\n"    
            "║ \033[1;32m{1}\033[1;30m║{25}║ 501 ║{26}║ \033[1;35m{13}\033[1;30m ║\n"     #501
            "║ \033[1;32m{2}\033[1;30m║{27}║ 501 ║{28}║ \033[1;35m{14}\033[1;30m ║\t\033[1;32m{39}\033[1;30m\n"
            "║ \033[1;32m{3}\033[1;30m║{29}║ 501 ║{30}║ \033[1;35m{15}\033[1;30m ║\t\033[1;32m{52}\033[1;30m\n"
            "║ \033[1;32m{4}\033[1;30m║{31}║ 501 ║{32}║ \033[1;35m{16}\033[1;30m ║\n"
            "╠{41}╣\t\033[1;35m{40}\033[1;30m\n"
            "║ \033[1;32m{5}\033[1;30m║{33}║ 301 ║{34}║ \033[1;35m{17}\033[1;30m ║\t\033[1;35m{53}\033[1;30m\n"
            "║ \033[1;32m{6}\033[1;30m║{33}║     ║{34}║ \033[1;35m{18}\033[1;30m ║\n"
            "╠{41}╣\n"
            "║ \033[1;32m{7}\033[1;30m║{35}║  C  ║{36}║ \033[1;35m{19}\033[1;30m ║\n"
            "║ \033[1;32m{8}\033[1;30m║{35}║     ║{36}║ \033[1;35m{20}\033[1;30m ║\n"
            "╠{41}╣\n"
            "║ \033[1;32m{9}\033[1;30m║{37}║     ║{38}║ \033[1;35m{21}\033[1;30m ║\n"
            "║ \033[1;32m{10}\033[1;30m║{37}║ 501 ║{38}║ \033[1;35m{22}\033[1;30m ║\n"
            "║ \033[1;32m{11}\033[1;30m║{37}║     ║{38}║ \033[1;35m{23}\033[1;30m ║\n"
            "║ \033[1;32m{12}\033[1;30m║{37}║     ║{38}║ \033[1;35m{24}\033[1;30m ║\n"
            "╠{43}╣\n"
            "║\033[1;31m{51}\033[1;30m║\n"                                                                          #Winner
            "╚{46}╝\n"
            

            ).format(  # The below

                self.date.rjust(self.WIDTH),                                                        #0
                *[player.ljust(self.LONGESTNAME_WIDTH) for player in formattedPlayerList],   #1-24
                *self.score_list,                                                                   #25-38 
                *self.listOfTeams,                                                                #39 & 40
                *list_of_seperators,                                                                #41 - 50
                self.getTournamentScore(),                                                        #51
                *[", ".join(sublist) for sublist in self.importedTeamList]
                
            )

    def getScoreList(self) -> list:

        self.score_list = []
        for i in range(14):
            self.score_list.append(" \033[1;30mO\033[1;30m ║ \033[1;30mO\033[1;30m ")
        
    def getWidth(self, listOfPlayers) -> None:

        '''Gets the width of the board to let the formatting be dynamic'''

        length = self.getLengthOfLongestName(listOfPlayers)
        self.WIDTH = (length*2) + 26 #Widdth of the spacings
        return self.WIDTH

    def getLengthOfLongestName(self, listOfPlayers) -> None:

        '''Finds the length of the longest name in the list.'''

        longest_name = ""
        for team in listOfPlayers:

            for name in team:
                if len(name) > len(longest_name):
                    longest_name = name

        self.LONGESTNAME_WIDTH = len(longest_name)
        return self.LONGESTNAME_WIDTH

    def getFormat(self, listOfPlayers) -> list:

        new_list = []
        for team in listOfPlayers:
            
            for num in range(12):
                new_list.append(team[num % len(team)])
        
        return new_list

    def getTournamentScore(self) -> str:

        self.NO_WINNER, self.TEAM_1,self.TEAM_2 = 0,1,2

        winner_banner = [
            "".center(len(self.listOfTeams[0]))+ f"{self.home_team_score}    SCORE    {self.away_team_score}".center(self.WIDTH-sum([len(team) for team in self.listOfTeams])) + "".center(len(self.listOfTeams[1])),
            "Winner!".center(len(self.listOfTeams[0])) + f"{self.home_team_score}    SCORE    {self.away_team_score}".center(self.WIDTH-sum([len(team) for team in self.listOfTeams])) + "".center(len(self.listOfTeams[1])),
            "".center(len(self.listOfTeams[0])) + f"{self.home_team_score}    SCORE    {self.away_team_score}".center(self.WIDTH-sum([len(team) for team in self.listOfTeams])) + "Winner!".center(len(self.listOfTeams[1])),
            ]

        if self.home_team_score + self.away_team_score == 7:
            
            if self.home_team_score > self.away_team_score:
                return winner_banner[self.TEAM_1]
            
            else:
                return winner_banner[self.TEAM_2]
        
        return winner_banner[0]
        
    def getPlayerName(self, team) -> str:

        '''Asks the user for a player name in the given team list. Returns player name when a valid name is given.'''

        player_name = input("\033[1;33mplayer name: \033[0;0m").capitalize()
        
        while player_name.strip() not in self.importedTeamList[team]:
            
            print("\033[1;31mNot a player in the team.")
            player_name = input("\033[1;33mplayer name: \033[0;0m").capitalize()
        return player_name

    def fillScoreboard(self) -> None:
        '''Lets the user input the player names into the scoreboard.'''
        four_round_counter = 0
        used_names = []
      
        for team in range(2):

            for player_slot in range(12):

                self.Terminal.clear()
                self.LONGESTNAME_WIDTH = self.getLengthOfLongestName(self.display_team_list)
                self.WIDTH = self.getWidth(self.display_team_list)
                print(self)
                player_name = self.validateSlotLocation(used_names, team, four_round_counter)
                used_names.append(player_name)
                self.display_team_list[team].insert(player_slot, player_name)
                self.display_team_list[team] = self.display_team_list[team][:-1]
                four_round_counter += 1
            
            if team == 0:
                self.display_team_list[1].insert(0,"|      ")
        
        self.LONGESTNAME_WIDTH = self.getLengthOfLongestName(self.display_team_list)
        self.WIDTH = self.getWidth(self.display_team_list)

    def validateSlotLocation(self, used_names: list, team, four_round_counter) -> str:
        """Checks if the player is already playing in that section."""
        
        player_name = self.getPlayerName(team)

        if four_round_counter % 4 == 0:
            used_names.clear()
        
        if player_name in used_names:
            
            while player_name in used_names:
                print("\033[1;31mERROR: Player already playing in that section!\033[0;0m")
                player_name = self.getPlayerName(team)
        
        return player_name

    def fillScoreboardAutomatically(self) -> None:
        '''Automatically fills in the player slots with the team names.'''

        for team in range(2):
            for player_slot in range(12):
                self.display_team_list[team].insert(player_slot, self.importedTeamList[team][player_slot%len(self.importedTeamList[team])])
        
        self.LONGESTNAME_WIDTH = self.getLengthOfLongestName(self.display_team_list)
        self.getWidth(self.display_team_list)

    def fillScore(self) -> None:
        '''Lets the user fill the score of the scoreboard.'''
        
        self.rounds_list = {}
        score_ui = [
            " \033[1;30mO\033[1;30m ║ \033[1;30mO\033[1;30m ", # 0 = O ║ O
            " \033[1;31mX\033[1;30m ║ \033[1;30mO\033[1;30m ", # 1 = X ║ O
            " \033[1;31mX\033[1;30m ║ \033[1;31mX\033[1;30m ", # 2 = X ║ X
            " \033[1;30mO\033[1;30m ║ \033[1;31mX\033[1;30m ", # 3 = O ║ X
        ]
        
        round_nr = 0
        for score_location in range(0,14,2):
            
            round_nr += 1
            print(self)
            score = self.getScore(round_nr)
            self.givePoint(score)
            self.score_list[score_location] = score_ui[int(score[0])]
            
            if int(score[1]) == 1:
                self.score_list[score_location+1] = score_ui[3]
            else:
                self.score_list[score_location+1] = score_ui[int(score[1])]
    
    def getScore(self, round_nr) -> list:
        '''Asks the user for the score for that round. returns valid score'''

        score = input(f"\033[1;33mScore for round {round_nr} (ex. input: [2 1] or [1 2]): ").split()
        while self.validateScoreInput(score) is False:

            print("\033[1;31minvalid score, try again.")
            score = input(f"\033[1;33mScore for round {round_nr} (ex. input: [2 1] or [1 2]): ").split()    
        
        self.Terminal.clear()
        return score
    
    def givePoint(self, score) -> None:

        if score[0] == "2": 
            self.home_team_score += 1 
        else: 
            self.away_team_score += 1

    def validateScoreInput(self, score) -> bool:
        '''Makes sure that the user input score is a valid score.'''
        
        valid_scores = ["2","0"],["2","1"],["1","2"],["0","2"]
        if score in valid_scores:
            self.rounds_list[self.game_count] = [int(item) for item in score]
            self.game_count += 1
            return True
        
        return False 

    def getData(self) -> dict:
        return {
            'Team_Score': [self.home_team_score, self.away_team_score],
            'ScoreData': self.rounds_list,
            'QualityPoints': self.quality_points,
            'PlayerList': [self.display_team_list[0][0:12],self.display_team_list[1][0:12]]
        }

    def askQualityPoints(self):
        """Asks the user if they want to input quality points, if yes, it calls the getQualityPoints() function."""
        self.quality_points = {}
        _choice = input("\033[1;34mWould you like to input Quality Points? (y/n): \033[0;0m")
        if _choice.lower() == "y":
            self.getQualityPoints()
        return
        

    def getQualityPoints(self):
        """Asks the user for the quality points of the players, then proceeds to print them out and ask if they want to add more 
        for another player."""
        another_one = True
        while another_one:
            
            player_name = self.getQualityName()
            self.getQualityScore(player_name)
            print(self.quality_points)
            print(self.printQualityPoints())
            another_one = self.askIfMore()
    
    def printQualityPoints(self):
        temp = [f"║ {str(name).ljust(self.LONGESTNAME_WIDTH)}║ {', '.join(score).ljust(self.WIDTH-self.LONGESTNAME_WIDTH-4)} ║" for name, score in self.quality_points.items()]
        txt = "\n".join(temp)
        print(self)
        return(
            "{2}\n"
            "╔{0}╗\n"
            "{3}\n"
            "╚{1}╝\n"
        ).format(
            "╦══════════════════════".center(self.WIDTH, "═"),  #48
            "╩══════════════════════".center(self.WIDTH, "═"),  #49
            'Quality Points'.center(self.WIDTH),
            txt
        )
    
    def getQualityName(self) -> str:
        """Asks the user for the name of the player they want to input quality points for, error checks if the player is in the
            team list, returns True or False depending on if the user wants to add more quality points for another player."""
        _player_name = input("\033[1;33mplayer name: ").capitalize()
        while _player_name.strip() not in self.importedTeamList[0] and _player_name.strip() not in self.importedTeamList[1]:
            
            print("\033[1;31mNot a player in a team.")
            _player_name = input("\033[1;33mplayer name: ").capitalize()
        return _player_name

    def getQualityScore(self, player_name):
        score = input(f"\033[1;34mInput Quality Points for {player_name} (example input: 112N, 100, 97U): ")
        score = score.strip().split(",")
        self.quality_points[player_name] = [point.strip() for point in score]

    def askIfMore(self) -> bool:
        _choice =  input("\033[1;34mWould you like to add another Quality Point Score? (y/n): ").lower()
        while _choice != "y" and _choice != "n":
            print("\033[1;31mplease enter a valid input!")
            _choice =  input("\033[1;34mWould you like to add another Quality Point Score? (y/n): ").lower()    
        if _choice == "y":
            return True
        return False
