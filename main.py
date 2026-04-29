import tkinter as tk
from tkinter import *
#matrix de verbos
from matrix import verbs

root = Tk()

root.title("Irregular Verb Transformer")
root.geometry('500x600')
# Setea el background
bg = PhotoImage(file = "./background.png")
lblBg = Label(root, image = bg)
lblBg.place(x = -40, y = -4)


txtVerb = Entry(root, height=1, width=40).pack(pady=10)
def busqueda(verb):
    for row in verbs:
        if row[0] == verb:
            return row
    return None


def clear():
    txtPastSimple.delete(1.0, END)
    txtPastParticiple.delete(1.0, END)
    txtSpanish.delete(1.0, END)


btnSearch = Button(root, text="Search", command=lambda: busqueda(txtVerb.get())).pack(pady=10)
txtPastSimple = Text(root,height=1, width=40).pack(pady=10)
txtPastParticiple = Text(root,height=1, width=40).pack(pady=10)
txtSpanish = Text(root,height=1, width=40).pack(pady=10)

root.mainloop()