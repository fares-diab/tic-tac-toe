import tkinter as tk
from tkinter import messagebox

main = tk.Tk()
main.title("Tic Tac Toe Game")
main.geometry("300x300")
currentp = "X"
board = [""] * 9

turn_label = tk.Label(main, text="Current Player: X", font=("Arial", 14))
turn_label.grid(row=3, columnspan=3)


def reset():
    global board, currentp
    board = [""] * 9
    currentp = "X"
    turn_label.config(text="Current Player: X")
    for button in buttons:
        button.config(text="", bg="light blue")

def winner():
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            for index in (a, b, c):
                buttons[index].config(bg="green")
            messagebox.showinfo("", f"{board[a]} wins")
            reset()
            return True
    
    if "" not in board:
        messagebox.showinfo("", "Draw")
        reset()
        return True
    
    return False

def click(cell):
    global currentp
    if board[cell] == "":
        board[cell] = currentp
        buttons[cell].config(text=currentp)
        turn_label.config(text=f"Current Player: {currentp}")
        
        if not winner():
            currentp = "O" if currentp == "X" else "X"
            turn_label.config(text=f"Current Player: {currentp}")

buttons = [tk.Button(main, text="", font=("Arial", 24), width=5, height=2, bg="light blue", command=lambda i=i: click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

main.mainloop()
