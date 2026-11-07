import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

root = tk.Tk()
root.title("To-do list")
root.geometry("350x550")
root.configure(bg='#747eed')
totalamount = 0
tasktimes = []
darkon = False

comptasks = 0
ttltasks = 0

def themer():
    global darkon
    darkon = not darkon
    if darkon == True:
        root.configure(bg = "#010b73")
        activitylbl.config(bg = "#010b73", fg = "#747eed")
        timelbl.config(bg = "#010b73", fg = "#747eed")
        statuslbl.config(bg = "#010b73", fg = "#747eed")
        prioritylbl.config(bg = "#010b73", fg = "#747eed")
        totaltime.config(bg = "#010b73", fg = "#747eed")
        actleft.config(bg = "#010b73", fg = "#747eed")
        entry.config(bg = "#010b73", fg = "#747eed")
        timeentry.config(bg = "#010b73", fg = "#747eed")
        lister.config(bg = "#010b73", fg = "#747eed")
        buttonframe.config(bg = "#010b73")
        buttonframe2.config(bg = "#010b73")
        themebutton.config(text="Light Mode")
    else:
        root.configure(bg ="#747eed")
        activitylbl.config(bg = "#747eed", fg = "#010b73")
        timelbl.config(bg = "#747eed", fg = "#010b73")
        statuslbl.config(bg = "#747eed", fg = "#010b73")
        prioritylbl.config(bg = "#747eed", fg = "#010b73")
        totaltime.config(bg = "#747eed", fg = "#010b73")
        actleft.config(bg = "#747eed", fg = "#010b73")
        entry.config(bg = "#747eed", fg = "#010b73")
        timeentry.config(bg = "#747eed", fg = "#010b73")
        lister.config(bg = "#747eed", fg = "#010b73")
        buttonframe.config(bg = "#747eed")
        buttonframe2.config(bg = "#747eed")
        themebutton.config(text="Dark Mode")



def adder():
    global totalamount
    global ttltasks
    
    activity = entry.get()
    time = timeentry.get()
    priority = priorityentry.get()

    t=int(time)


    tasktimes.append(t)
    totalamount += t

    ttltasks += 1
    progress.config(maximum=ttltasks)


    ttlhours = totalamount // 60
    ttlmins = totalamount % 60

    total =priority +" - "+ activity +" - "+ time + " mins"
    
    lister.insert(tk.END, total)

    entry.delete(0, tk.END)
    timeentry.delete(0, tk.END)

    statuslbl.config(text=activity+" has been added")
    if totalamount>=60:
        totaltime.config(text="Total Time Required is " + str(ttlhours) + "Hours"+ str(ttlmins)+"Mins")
    else:
        totaltime.config(text="Total Time Required is " + str(totalamount)+ " Mins")
    
    actleft.configure(text = "Total # Of Tasks Remaining are: " + str(lister.size()))


def done():
    global totalamount
    global comptasks

    select = lister.curselection()

    index=select[0]

    totalamount -= tasktimes[index]
    tasktimes.pop(index)
    
    ttlhours = totalamount // 60
    ttlmins = totalamount % 60


    lister.delete(index)
    statuslbl.config(text="Task has Been Finished!!!")

    comptasks += 1
    progress.config(value=comptasks)

    if totalamount>=60:
        totaltime.config(text="Total Time Required is " + str(ttlhours) + "Hours"+ str(ttlmins)+"Mins")
    else:
        totaltime.config(text="Total Time Required is " + str(totalamount)+ " Mins")
    actleft.configure(text = "Total # Of Tasks Remaining are: " + str(lister.size()))
    if lister.size() ==0:
        statuslbl.config(text="All Done! Proud of You!", fg = "#010b73", font = ("Segoe UI", 14))

def clear():
    global totalamount
    totalamount = 0
    tasktimes.clear()
    lister.delete(0, tk.END)
    totaltime.config(text="Total Time Required = 0 mins")
    actleft.config(text="Total Amount of Tasks Left: 0")
    if lister.size() ==0:
        statuslbl.config(text="All Done! Proud of You!", fg = "#010b73", font = ("Segoe UI", 14))
def randomizer():
    ttltasks = lister.size()
    num = random.randint(0, ttltasks-1)
    chose = lister.get(num)
    statuslbl.config(text="Do this next " + chose)

activitylbl = tk.Label(root, text = "Activity Name:", font=("Segoe UI", 10), bg='#747eed')
activitylbl.pack()
entry = tk.Entry(root, font=("Segoe UI",10), width=30, bg="#cfd3fc")
entry.pack(pady=2)

timelbl = tk.Label(root, text = "Time in Mins:", font=("Segoe UI", 10), bg='#747eed')
timelbl.pack()
timeentry = tk.Entry(root, font=("Segoe UI",10), width=10, bg="#cfd3fc")
timeentry.pack(pady=2)

#label = tk.Label(root, text="", font=("Segoe UI",14))
#label.pack(pady=5)

statuslbl = tk.Label(root, text="", font=("Segoe UI",14), bg='#747eed')
statuslbl.pack(pady=5)

entry.bind("<Return>", lambda event: adder())
timeentry.bind("<Return>", lambda event: adder())

prioritylbl = tk.Label(root, text="Priority Level:", font = ("Segoe UI",10), bg='#747eed')
prioritylbl.pack()

priorityentry = tk.StringVar(root)
priorityentry.set("Medium")
prioritydrop = tk.OptionMenu(root, priorityentry, "High", "Medium", "Low")
prioritydrop.config(bg="#cfd3fc", font = ("Segoe UI",14), width=10, height = 1)
prioritydrop.pack(pady=2)

root.bind("<q>", lambda event: done())
#timeentry.bind("<q>", lambda event: done())

buttonframe = tk.Frame(root, bg='#747eed')
buttonframe.pack(pady=5)

buttonframe2 = tk.Frame(root, bg='#747eed')
buttonframe2.pack(pady=5)

button = Button(buttonframe,text='Add New Activity', bg="#9fa7fc")
button.pack(side=tk.LEFT, padx=5)
button.config(command=adder)

finish = Button(buttonframe, text='Finish!!!', command = done, bg="#9fa7fc")
finish.pack(side = tk.LEFT, padx=5)

rand = Button(buttonframe, text = "Pick a Random Task for Me", command = randomizer, bg="#9fa7fc")
rand.pack(side = tk.LEFT, padx=5)

root.bind("<r>", lambda event: randomizer())


clearall = Button(buttonframe2, text="Clear All Tasks", bg = "#9fa7fc")
clearall.config(command=clear)
clearall.pack(side = tk.LEFT,padx=5)

totaltime = tk.Label(root, text="Total Time Required: 0 mins", font = ("Segoe UI", 11), bg='#747eed')
totaltime.pack(pady=5)

lister = tk.Listbox(root, font=("Times New Roman",12), width=40, height = 10, bg="#cfd3fc")
lister.pack(pady=5)

actleft = tk.Label(root, text = "Total # Of Tasks Left: 0", font = ("Segoe UI", 14), bg='#747eed')
actleft.pack(pady=5)

themebutton = Button(buttonframe2, text = "Dark Mode", command = themer, bg = "#9fa7fc")
themebutton.pack(side = tk.LEFT, padx = 5)

progress = ttk.Progressbar(root, orient = "horizontal", length = 260, mode = "determinate")
progress.pack(pady=5)

root.mainloop()