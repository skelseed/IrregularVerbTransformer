import tkinter as tk
from tkinter import *
from matrix import verbs

root = Tk()
root.title("Irregular Verb Transformer")
root.geometry('500x400')

# Setea el background
try:
    bg = PhotoImage(file = "./background.png")
    lblBg = Label(root, image = bg)
    lblBg.place(x = -40, y = -4)
except:
    pass  # Continue even if background image is missing

# White text title in big font - Comic Sans
title_label = Label(root, text="Edward's Wonderful Irregular Verb Transformer !!", 
                    font=("Comic Sans MS", 14, "bold"), fg="white", bg="black")
title_label.pack(pady=10)

# Label before the Entry
lblVerbInstruction = Label(root, text="Verb (Infinitive pls)", 
                           font=("Comic Sans MS", 10, "bold"))
lblVerbInstruction.pack(pady=(10, 0))

# Entry for verb input
txtVerb = Entry(root, width=40, font=("Comic Sans MS", 10))
txtVerb.pack(pady=5)

def busqueda(verb):
    for row in verbs:
        if row[0] == verb:
            return row
    return None

def search():
    verb = txtVerb.get().strip().lower()
    result = busqueda(verb)
    
    clear()  # Clear previous results
    
    if result:
        txtPastSimple.insert(1.0, result[0])  # Past participle form
        txtPastParticiple.insert(1.0, result[1])  # Using past participle
        txtSpanish.insert(1.0, result[2])
    else:
        txtPastSimple.insert(1.0, "Not an Irregular Verb")
        txtPastParticiple.insert(1.0, "Not an Irregular Verb")
        txtSpanish.insert(1.0, ">:V")

def clear():
    txtPastSimple.delete(1.0, END)
    txtPastParticiple.delete(1.0, END)
    txtSpanish.delete(1.0, END)
    txtVerb.delete(0, END)

# Button frames for better layout
button_frame = Frame(root)
button_frame.pack(pady=10)

btnSearch = Button(button_frame, text="Search", command=search, width=15,
                   font=("Comic Sans MS", 10))
btnSearch.pack(side=LEFT, padx=5)

btnClear = Button(button_frame, text="Clear", command=clear, width=15,
                  font=("Comic Sans MS", 10))
btnClear.pack(side=LEFT, padx=5)

# Labels for the text boxes
Label(root, text="Past Simple:", font=("Comic Sans MS", 10, "bold")).pack()
txtPastSimple = Text(root, height=1, width=40, font=("Comic Sans MS", 10, "bold"))
txtPastSimple.pack(pady=5)

Label(root, text="Past Participle:", font=("Comic Sans MS", 10, "bold")).pack()
txtPastParticiple = Text(root, height=1, width=40, font=("Comic Sans MS", 10, "bold"))
txtPastParticiple.pack(pady=5)

Label(root, text="Spanish Translation:", font=("Comic Sans MS", 10, "bold")).pack()
txtSpanish = Text(root, height=1, width=40, font=("Comic Sans MS", 10, "bold"))
txtSpanish.pack(pady=5)

root.mainloop()
