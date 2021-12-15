# Author: Ryan Gallagher
# Date: 12/15/2021
# Description: Following along with a tutorial to build tic tac toe.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# X starts so true
clicked = True
count = 0
winner = False


# Check to see if someone won
def checkifwon():
    """Checks to see if a player has won."""
    """Checks to see if a player has won."""
    global winner

    # disable all the buttons
    def disable_all_buttons():
        """Disables all buttons after a win or after a stalemate."""
        pass

    # horizontal wins
    if b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X':
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    elif b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X':
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    elif b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    # vertical wins
    elif b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X':
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    elif b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X':
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    elif b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X':
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    # diagonal wins
    elif b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

    elif b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X':
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, X wins!")
        disable_all_buttons()

# Button clicked function
def b_click(b):
    """Allows a button to be clicked"""
    global clicked, count

    if b["text"] == " " and clicked is True:
        b["text"] = "X"
        clicked = False
        count += 1

    elif b["text"] == " " and clicked is False:
        b["text"] = "O"
        clicked = True
        count += 1

    else:
        messagebox.showerror("Tick-Tac-Toe", "That box has already been selected\nPick another box...")


# Build buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b9))

# Grid our buttons to screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
