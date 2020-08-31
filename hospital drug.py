import tkinter as tk
import tkinter.ttk as ttk
################################################################################################################
def callback1(arg1,arg2,arg3):
    p1.set(n_p_1.get())

def start():
    pass

##################################################################################################################
root = tk.Tk()
note = ttk.Notebook(root)
note.grid(row=0, column = 0)
##############################################################
timer = tk.Frame()
patient = tk.Frame()
##############################################################
note.add(timer , text = "timer")
note.add(patient,text = "patient")
##timer##########################################################################################################
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
################################################################################################################
t1= tk.StringVar()
t1.set("00:00")
tk.Label(timer,textvariable=t1).grid(row=1,column=0)
#############################################################
t2= tk.StringVar()
t2.set("00:00")
tk.Label(timer,textvariable=t2).grid(row=1,column=1)
#############################################################
t3= tk.StringVar()
t3.set("00:00")
tk.Label(timer,textvariable=t3).grid(row=1,column=2)
#button########################################################################################################
tk.Button(timer,text="start",command=start).grid(row=2,column=0)
############################################################
tk.Button(timer,text="start",command=start).grid(row=2,column=1)
############################################################
tk.Button(timer,text="start",command=start).grid(row=2,column=2)
##############################################3#############
tk.Button(timer,text="cancel",command=root.destroy).grid(row=3,column=0,columnspan=3,sticky=tk.E+tk.W)
##patient tab##################################################################################################
patient1=tk.LabelFrame(patient,text="patient1")
patient1.grid(row=0,column=0,padx=10)

tk.Label(patient1,text="Name").grid(row=0,column=0)
tk.Label(patient1,text="Timer").grid(row=1,column=0)

n_p_1 = tk.StringVar()
n_p_1.trace("w",callback1)
tk.Entry(patient1,textvariable=n_p_1).grid(row=0,column=1)

h_p_1 = tk.StringVar()
h_p_1.set("12")
m_p_1 = tk.StringVar()
m_p_1.set("30")
s_p_1 = tk.StringVar()
s_p_1.set("30")
f1=tk.Frame(patient1)
f1.grid(row=1,column=1)
tk.Spinbox(f1,
          from_=0,
          to=23,
          wrap=True,
          textvariable=h_p_1,
          width=2,
          state="readonly").grid(row=0,column=0)

root.mainloop()

