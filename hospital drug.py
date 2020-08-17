import tkinter as tk
import tkinter.ttk as ttk
#############################################################
root = tk.Tk()
note = ttk.Notebook(root)
note.grid(row=0, column = 0)
#############################################################
timer = tk.Frame()
patient = tk.Frame()
#############################################################
note.add(timer , text = "timer")
note.add(patient,text = "patient")
##timer#########################################################################################################
b1= tk.StringVar()
b1.set("patient1")
tk.Label(timer,textvariable=b1).grid(row=0,column=0)
#############################################################
b2= tk.StringVar()
b2.set("patient2")
tk.Label(timer,textvariable=b2).grid(row=0,column=1)
#############################################################
b3= tk.StringVar()
b3.set("patient3")
tk.Label(timer,textvariable=b3).grid(row=0,column=2)
#############################################################

root.mainloop()

