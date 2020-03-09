import random

class TicTacToe(object):
    def __init__(self):
        self.game = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.player1 = None
        self.player2 = None

    def board(self):
        print("                 ")
        print("     |     |     ")
        print(f"  {self.game[0]}  |  {self.game[1]}  |  {self.game[2]}  ")
        print(f"_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.game[3]}  |  {self.game[4]}  |  {self.game[5]}  ")
        print(f"_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.game[6]}  |  {self.game[7]}  |  {self.game[8]}  ")
        print("     |     |     ")
        print("                 ")

    def move(self, player: int):
        if player == 1:
            if self.player1 == 'player' or self.player1 == 'opponent':
                print("Please enter move position: ")
                move = int(input())
                print(f"You entered: {move}")
                self.game[move] = 'O'
            elif self.player1 == 'ai':
                move = self.computer_move()
                print(f"Computer move: {move}")
                self.game[move] = 'O'
        elif player == 2:
            if self.player2 == 'player' or self.player2 == 'opponent':
                print("Please enter move position: ")
                move = int(input())
                print(f"You entered: {move}")
                self.game[move] = 'X'
            elif self.player2 == 'ai':
                move = self.computer_move()
                print(f"Computer move: {move}")
                self.game[move] = 'X'
        else:
            raise ValueError(f"Player {player} is invalid.")

        self.board()
            
    def evaluate_column(self, col: int):
        if self.game[col] == self.game[col+3] == self.game[col+6]:
            return self.game[col]
        else:
            return None
    
    def evaluate_columns(self):
        for col in [0, 1, 2]:
            ev = self.evaluate_column(col)
            if ev:
                return ev
        return None
        
    def evaluate_row(self, row: int):
        if self.game[row] == self.game[row + 1] == self.game[row + 2]:
            return self.game[row]
        else:
            return None
    
    def evaluate_rows(self):
        for row in [0, 1, 2]:
            ev = self.evaluate_row(row)
            if ev:
                return ev
        return None

    def evaluate_diagonal(self, diag: int):
        if diag == 1:
            if self.game[diag] == self.game[diag + 4] == self.game[diag + 8]:
                return self.game[diag]
            else:
                return None
        elif diag == 2:
            if self.game[diag] == self.game[diag + 2] == self.game[diag + 4]:
                return self.game[diag]
            else:
                return None
        else:
            raise ValueError(f"Invalid value {diag} specified for diagnoal.")

    def evaluate_diagonals(self):
        for diag in [1, 2]:
            ev = self.evaluate_diagonal(diag)
            if ev:
                return ev
        return None

    def check_win(self, symbol: str):
        if symbol == "O":
            print("O is the winner!")
        elif symbol == "X":
            print("X is the winner!")
        else:
            raise ValueError(f"Symbol {symbol} cannot be identified.")
        
    def evaluate_board(self):
        row_check = self.evaluate_rows()
        col_check = self.evaluate_columns()
        diag_check = self.evaluate_diagonals()
        return row_check, col_check, diag_check

    def evaluate_win(self):
        row_check, col_check, diag_check = self.evaluate_board()

        if row_check:
            self.check_win(row_check)
            return row_check
        elif col_check:
            self.check_win(col_check)
            return col_check
        elif diag_check:
            self.check_win(diag_check)
            return diag_check
        else:
            return None
    
    def evaluate_draw(self):
        for val in self.game:
            if val != "X" or val != "O":
                return False
            else:
                pass
        return True

    def evaluate(self):
        verdict = self.evaluate_win()
        if verdict:
            print("Game over!")
            return True
        else:
            if self.evaluate_draw():
                print("Game draw!")
                return True
            else:
                print("Continue playing!")
        return False

    def assign_player(self):
        print("Please input your symbol of choice: (O/X)")
        symbol = input()
        if symbol == "X":
            self.player2 = 'player'
        elif symbol == "O":
            self.player1 = 'player'
        else:
            raise ValueError(f"Symbol {symbol} is invalid.")
    

    def versus(self):
        print("Would you like to play against the computer? (Y/N)")
        selection = input()
        if selection == "Y":
            if self.player1:
                self.player2 = 'ai'
            else:
                self.player1 = 'ai'
        elif selection == "N":
            if self.player1:
                self.player2 = 'opponent'
            else:
                self.player2 = 'opponent'
        else:
            raise ValueError(f'{selection} is not a valid option.')
        

    def get_valid_positions(self):
        return [i for i in self.game if i != "X" and i != "O"]

    def computer_move(self):
        positions = self.get_valid_positions()
        choice = random.choice(positions)
        return choice

    def play(self):
        print("Tic Tac Toe!")
        self.assign_player()
        self.versus()
        res = False
        while not res:
            print("Player 1 move: ")
            self.move(1)
            res = self.evaluate()
            if res:
                break
            print("Player 2 move: ")
            self.move(2)
            res = self.evaluate()
            if res:
                break

        print("Thank you for playing!")

def play():
    T = TicTacToe()
    T.play()

if __name__ == '__main__':
    play()