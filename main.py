import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize game variables
current_player = "X"
board = [" " for _ in range(9)]
game_over = False

# Create game functions
def check_win():
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False

def check_draw():
    return " " not in board

def handle_click(index):
    global current_player, game_over

    if board[index] == " " and not game_over:
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

# Create and configure buttons
buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=" ", font=("Helvetica", 20), width=8, height=3,
                      command=lambda i=i: handle_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Start the game
root.mainloop()

