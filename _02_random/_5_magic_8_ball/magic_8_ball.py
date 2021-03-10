import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(None, "What question would you like to ask the Magic 8 Ball?")

    # Make a variable and initialize it to a random number between 0 and 3
    r = random.randint(0,3)
    # If the random number is 0
    if r == 0:
        messagebox.showinfo("The Most Amazing Answer", "Yes!")
        # tell the user "Yes"

    # If the random number is 1
    if r == 1:
        messagebox.showinfo("The Most Amazing Answer", "No.")

        # tell the user "No"

    # If the random number is 2
    if r == 2:
        messagebox.showinfo("The Most Amazing Answer", "Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if r == 3:
        messagebox.showinfo("The Most Amazing Answer", "Only if you change your name to Larry.")
        # write your own answer
