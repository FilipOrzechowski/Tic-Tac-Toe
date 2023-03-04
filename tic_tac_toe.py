# A class that contains the variables and methods needed to generate the grid and to monitor the game status
class Grid():
    def __init__(self, player_1_name, player_2_name, player_1_mark, player_2_mark):
        self.active = 1
        self.round = 1
        self.draw = 0
        self.game_ended = False

        self.a1 = " " 
        self.a2 = " " 
        self.a3 = " " 
        self.b1 = " " 
        self.b2 = " " 
        self.b3 = " " 
        self.c1 = " " 
        self.c2 = " " 
        self.c3 = " "

        self.row_head = "      |  1  |  2  |  3  |"
        self.row_line = "-------------------------"
        self.list_of_choices =  ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

        self.p1_name = player_1_name
        self.p1_mark = player_1_mark
        self.p1_chosen_squares = []
        self.p1_wins = 0

        self.p2_name = player_2_name
        self.p2_mark = player_2_mark
        self.p2_chosen_squares = []
        self.p2_wins = 0

        self.win_combinations =[["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], ["A1", "B2", "C3"], ["A3", "B2", "C1"], ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"]]
