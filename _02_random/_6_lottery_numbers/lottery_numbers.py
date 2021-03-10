import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    s = ""
    for i in range(6):
        i = random.randint(0,99)
        if i<10:
            s += "0" + str(i)
        else:
            s += str(i)
        if i!=5:
            s += " "
    messagebox.showinfo("Narnia Lottery", s)

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
