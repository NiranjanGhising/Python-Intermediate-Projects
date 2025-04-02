class Board:

    def __init__(self):

        self.board = [' ',' ',' ',
                      ' ',' ',' ',
                      ' ',' ',' ']

    def print_result(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def update_board(self,position,type):
        try:
            if self.board[position-1] == ' ':
                self.board[position-1] = type
                return True
            else:
                print("the position you are trying to put in already fillup...")
                return False
        except:
            print("Invalid position, select another position...")
        
        
     # If three symbols appears in a row, returning True
    def check_winner(self, type):
        if (self.board[0] == type and self.board[1] == type and self.board[2] == type) or \
           (self.board[3] == type and self.board[4] == type and self.board[5] == type) or \
           (self.board[6] == type and self.board[7] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[3] == type and self.board[6] == type) or \
           (self.board[1] == type and self.board[4] == type and self.board[7] == type) or \
           (self.board[2] == type and self.board[5] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[4] == type and self.board[8] == type) or \
           (self.board[2] == type and self.board[4] == type and self.board[6] == type):
            return True
        else:
            return False

    # If all fields are selected and there is no winner, it's draw
    # Returning True if it's draw
    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False


class Player:
    
    #type - used for symbol either 'X' or 'O'
    def __init__(self,type):
        self.type = type
        self.player_name = self.player_name()
        
    
    def player_name(self):
        if self.type == 'X':
            name = input("Player X , enter your name: ")
        else:
            name = input("Player O, enter your name:")
        return name

        

class Game:
    
    def __init__(self):
        
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')

        self.current_player = self.player1

    def play(self):
        

        while True:
            try:
                message = (f"{self.current_player.player_name}, please enter the position you want to mark 1-9:")
                position = int(input(message))

                #insert the mark in the board if the position is not fillup
                if self.board.update_board(position,self.current_player.type):
                    self.board.print_result()

                #check winner

                if self.board.check_winner(self.current_player.type):
                    print(self.current_player.player_name, "winssss!!")
                    break
                
                elif self.board.check_draw():
                    print("its draw")
                    break

                #update the player after the other enter their position
                else:
                    if self.current_player == self.player1:
                        self.current_player = self.player2
                    else:
                        self.current_player = self.player1
            except:
                print("invalid input!! Enter the position between 1-9...")




def main():
    g=Game()
    g.play()

main()
    


    

