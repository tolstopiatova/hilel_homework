import random

class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.piece_symbols = ['♚', '♛', '♜', '♝', '♞', '♟']

    def place_random_pieces(self):
        for symbol in self.piece_symbols:
            row, col = random.randint(0, 7), random.randint(0, 7)
            while self.board[row][col] != ' ':
                row, col = random.randint(0, 7), random.randint(0, 7)
            self.board[row][col] = symbol

    def draw_board(self):
        print("  a b c d e f g h")
        print(" ┌─┬─┬─┬─┬─┬─┬─┬─┐")
        for i in range(8):
            print(f"{8-i}|", end="")
            for j in range(8):
                print(f" {self.board[i][j]}|", end="")
            print("\n ├─┼─┼─┼─┼─┼─┼─┼─┤")
        print(" └─┴─┴─┴─┴─┴─┴─┴─┘")

# Створення об'єкту дошки
board1 = ChessBoard()

# Розташування фігур та намалювання дошки
board1.place_random_pieces()
board1.draw_board()

# Повторення ще двічі
for _ in range(2):
    print("\n---------------------\n")
    board = ChessBoard()
    board.place_random_pieces()
    board.draw_board()
