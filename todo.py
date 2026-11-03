import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To-do list")
root.geometry("350x350")

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

    statuslbl.config(text=activity+" has been added")
    if totalamount>=60:
        totaltime.config(text="Total Time Required is " + str(ttlhours) + "Hours"+ str(ttlmins)+"Mins")
    else:
        totaltime.config(text="Total Time Required is " + str(totalamount)+ " Mins")


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

activitylbl = tk.Label(root, text = "Activity Name:", font=("Arial", 10))
activitylbl.pack()
entry = tk.Entry(root, font=("Arial",10), width=30)
entry.pack(pady=2)

timelbl = tk.Label(root, text = "Time in Mins:", font=("Arial", 10))
timelbl.pack()
timeentry = tk.Entry(root, font=("Arial",10), width=10)
timeentry.pack(pady=2)

#label = tk.Label(root, text="", font=("Arial",14))
#label.pack(pady=5)

statuslbl = tk.Label(root, text="", font=("Arial",14))
statuslbl.pack(pady=5)

button = Button(root,text='Add New Activity')
button.pack()
button.config(command=adder)

finish = Button(root, text='Finish!!!', command = done)
finish.pack(pady=5)

totaltime = tk.Label(root, text="Total Time Required: 0 mins", font = ("Arial", 11))
totaltime.pack(pady=5)

lister = tk.Listbox(root, font=("Times New Roman",12), width=40, height = 10)
lister.pack(pady=5)

root.mainloop()