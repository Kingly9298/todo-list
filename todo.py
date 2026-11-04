import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To-do list")
root.geometry("350x500")
root.configure(bg='#747eed')
totalamount = 0
tasktimes = []


def adder():
    global totalamount

    
    activity = entry.get()
    time = timeentry.get()

    t=int(time)


    tasktimes.append(t)
    totalamount += t

    ttlhours = totalamount // 60
    ttlmins = totalamount % 60

    total = activity +" - "+ time + " mins"
    
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

    select = lister.curselection()

    index=select[0]

    totalamount -= tasktimes[index]
    tasktimes.pop(index)
    
    ttlhours = totalamount // 60
    ttlmins = totalamount % 60


    lister.delete(index)
    statuslbl.config(text="Task has Been Finished!!!")

    if totalamount>=60:
        totaltime.config(text="Total Time Required is " + str(ttlhours) + "Hours"+ str(ttlmins)+"Mins")
    else:
        totaltime.config(text="Total Time Required is " + str(totalamount)+ " Mins")
    actleft.configure(text = "Total # Of Tasks Remaining are: " + str(lister.size()))

def clear():
    global totalamount
    totalamount = 0
    tasktimes.clear()
    lister.delete(0, tk.END)
    totaltime.config(text="Total Time Required = 0 mins")
    actleft.config(text="Total Amounf of Tasks Left: 0")

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

root.bind("<q>", lambda event: done())
#timeentry.bind("<q>", lambda event: done())

buttonframe = tk.Frame(root, bg='#747eed')
buttonframe.pack(pady=5)

button = Button(buttonframe,text='Add New Activity', bg="#9fa7fc")
button.pack(side=tk.LEFT, padx=5)
button.config(command=adder)

finish = Button(buttonframe, text='Finish!!!', command = done, bg="#9fa7fc")
finish.pack(side = tk.LEFT, padx=5)

clearall = Button(root, text="Clear All Tasks", bg = "#9fa7fc")
clearall.config(command=clear)
clearall.pack(pady=5)

totaltime = tk.Label(root, text="Total Time Required: 0 mins", font = ("Segoe UI", 11), bg='#747eed')
totaltime.pack(pady=5)

lister = tk.Listbox(root, font=("Times New Roman",12), width=40, height = 10, bg="#cfd3fc")
lister.pack(pady=5)

actleft = tk.Label(root, text = "Total # Of Tasks Left: 0", font = ("Segoe UI", 14), bg='#747eed')
actleft.pack(pady=5)

root.mainloop()