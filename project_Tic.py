import tkinter as tk
from tkinter import messagebox
import random

class GameBoard:
    def __init__(self):
        self.board = [""] * 9

    def update(self, index, player):
        if self.board[index] == "":
            self.board[index] = player
            return True
        return False

    def is_full(self):
        return "" not in self.board

    def get_board(self):
        return self.board

    def check_winner(self):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for combo in combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]], combo

        if self.is_full():
            return "Draw", None

        return None, None
    
class AIPlayer:
    def __init__(self, board_obj):
        self.board_obj = board_obj

    def minimax(self, board, is_ai):
        result, _ = self.check_winner_static(board)

        if result == "O":
            return 1
        elif result == "X":
            return -1
        elif result == "Draw":
            return 0

        if is_ai:
            best = -float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, False)
                    board[i] = ""
                    best = max(best, score)
            return best
        else:
            best = float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, True)
                    board[i] = ""
                    best = min(best, score)
            return best

    def check_winner_static(self, board):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for combo in combos:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                return board[combo[0]], combo

        if "" not in board:
            return "Draw", None

        return None, None

    def get_best_move(self):
        board = self.board_obj.get_board()
        best_score = -float('inf')
        move = -1

        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = self.minimax(board, False)
                board[i] = ""
                if score > best_score:
                    best_score = score
                    move = i

        return move

class UIManager:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.buttons = [
            tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                      command=lambda i=i: self.controller.handle_click(i))
            for i in range(9)
        ]

        for i, btn in enumerate(self.buttons):
            btn.grid(row=i//3, column=i%3)

        self.label = tk.Label(root, text="Mahesh turn 🧑", font=('Arial', 14))
        self.label.grid(row=3, column=0, columnspan=3)

    def update_button(self, index, player):
        self.buttons[index]['text'] = player

    def set_turn(self, text):
        self.label.config(text=text)

    def highlight_draw(self):
        for btn in self.buttons:
            btn.config(bg="lightblue")

    def celebrate_ai(self):
        colors = ["pink", "lightpink", "hotpink", "magenta"]

        def flash(count=0):
            if count > 6:
                return
            for btn in self.buttons:
                btn.config(bg=random.choice(colors))
            self.root.after(200, flash, count + 1)

        flash()

    def celebrate_user(self):
        colors = ["lightgreen", "green", "lime", "springgreen"]

        def flash(count=0):
            if count > 6:
                return
            for btn in self.buttons:
                btn.config(bg=random.choice(colors))
            self.root.after(200, flash, count + 1)

        flash()

    def show_message(self, msg):
        messagebox.showinfo("Game Over", msg)

class GameController:
    def __init__(self, root):
        self.root = root
        self.board = GameBoard()
        self.ai = AIPlayer(self.board)
        self.ui = UIManager(root, self)
        self.game_over = False

    def handle_click(self, index):
        if self.game_over:
            return

        if self.board.update(index, "X"):
            self.ui.update_button(index, "X")

            result, combo = self.board.check_winner()
            if result:
                self.end_game(result, combo)
                return

            self.ui.set_turn("AI turn 🤖")
            self.root.after(500, self.ai_turn)

    def ai_turn(self):
        move = self.ai.get_best_move()

        if move != -1:
            self.board.update(move, "O")
            self.ui.update_button(move, "O")

        result, combo = self.board.check_winner()
        if result:
            self.end_game(result, combo)
            return

        self.ui.set_turn("Mahesh turn 🧑")

    def end_game(self, result, combo):
        self.game_over = True

        if result == "Draw":
            self.ui.highlight_draw()
            self.ui.show_message("It's a Draw!")
            return

        if result == "O":
            self.ui.celebrate_ai()
        elif result == "X":
            self.ui.celebrate_user()

        self.ui.show_message(f"{result} wins!")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic-Tac-Toe AI OOP")

    game = GameController(root)

    root.mainloop()