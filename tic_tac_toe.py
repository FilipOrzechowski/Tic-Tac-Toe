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

# This method is used to print the grid
    def print_grid(self):
        self.row_A = "|  A  |  {A1}  |  {A2}  |  {A3}  |".format(A1=self.a1, A2=self.a2, A3=self.a3)
        self.row_B = "|  B  |  {B1}  |  {B2}  |  {B3}  |".format(B1=self.b1, B2=self.b2, B3=self.b3)
        self.row_C = "|  C  |  {C1}  |  {C2}  |  {C3}  |".format(C1=self.c1, C2=self.c2, C3=self.c3)
        self.row_list = [self.row_A, self.row_B, self.row_C]
        print(self.row_head)
        print(self.row_line)
        for row in self.row_list:
            print(row)
            print(self.row_line)

# This method is used to mark squares chosen by the player and to change the turn
    def make_choice(self, player_name, player_mark, player_chosen_squares):
        choice = input(player_name + ", it is your turn: ").upper()
        while choice not in self.list_of_choices:
            if choice in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
                choice = input("This square has been marked! ").upper()
            
            else:
                choice = input("This square does not exist! ").upper()

        if choice in self.list_of_choices:
            self.list_of_choices.remove(str(choice))
            player_chosen_squares.append(choice)
            if choice == "A1":
                self.a1=str(player_mark)

            elif choice == "A2":
                self.a2=str(player_mark)
      
            elif choice == "A3":
                self.a3=str(player_mark)
      
            elif choice == "B1":
                self.b1=str(player_mark)
      
            elif choice == "B2":
                self.b2=str(player_mark)
      
            elif choice == "B3":
                self.b3=str(player_mark)
            
            elif choice == "C1":
                self.c1=str(player_mark)
      
            elif choice == "C2":
                self.c2=str(player_mark)
      
            elif choice == "C3":
                self.c3=str(player_mark)
            
            self.active = self.active*(-1)  
        
            
        self.print_grid() 
