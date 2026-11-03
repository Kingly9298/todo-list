import tkinter as tk
from tkinter import *

def adder():
    statuslbl.config(text="Activity Has Been Added")


root = tk.Tk()
root.title("To-do list")
root.geometry("500x300")

label = tk.Label(root, text="Get Organized", font=("Arial",14))
label.pack(pady=5)

statuslbl = tk.Label(root, text="", font=("Arial",14))
statuslbl.pack(pady=5)

button = Button(root,text='Add New Activity')
button.pack()
button.config(command=adder)

root.mainloop()