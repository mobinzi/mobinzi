import tkinter as tk
from tkinter import Frame
import tkinter.ttk as ttk


def start():
    pass

def callback1(arg1, arg2, arg3):
    p1.set(n_p_1.get())

def callback2(arg1, arg2, arg3):
    p1.set(n_p_2.get())

def callback3(arg1, arg2, arg3):
    p1.set(n_p_3.get())
###############################################
def callback_t_1(arg1, arg2, arg3):
    t1.set("%02d:%02d:%02d"%(int(h_p_1.get()),int(m_p_1.get()),int(s_p_1.get()))) 

def callback_t_2(arg1, arg2, arg3):
    t2.set("%02d:%02d:%02d"%(int(h_p_2.get()),int(m_p_2.get()),int(s_p_2.get()))) 

def callback_t_3(arg1, arg2, arg3):
    t3.set("%02d:%02d:%02d"%(int(h_p_3.get()),int(m_p_3.get()),int(s_p_3.get()))) 


root = tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)

timer = tk.Frame()
patient = tk.Frame()

note.add(timer, text='Timer')
note.add(patient, text='Patient')

# ############### Timer First Row ############## #
p1 = tk.StringVar()
p1.set('Patient1')
tk.Label(timer, textvariable=p1).grid(row=0, column=0)
p2 = tk.StringVar()
p2.set('Patient2')
tk.Label(timer, textvariable=p2).grid(row=0, column=1)
p3 = tk.StringVar()
p3.set('Patient3')
tk.Label(timer, textvariable=p3).grid(row=0, column=2)
# ############## Timer Second Row ############## #
t1 = tk.StringVar()
t1.set('00:00:00')
tk.Label(timer, textvariable=t1).grid(row=1, column=0)
t2 = tk.StringVar()
t2.set('00:00:00')
tk.Label(timer, textvariable=t2).grid(row=1, column=1)
t3 = tk.StringVar()
t3.set('00:00:00')
tk.Label(timer, textvariable=t3).grid(row=1, column=2)
# ########### Timer Third Row Buttons ########## #
tk.Button(timer, text='Start', command=start).grid(row=2, column=0)
tk.Button(timer, text='Start', command=start).grid(row=2, column=1)
tk.Button(timer, text='Start', command=start).grid(row=2, column=2)
# ######## Timer Last Row Cancel Button ######## #
tk.Button(timer, text='Cancel', command=root.destroy).grid(row=3, column=0, columnspan=3, sticky=tk.E+tk.W)
# ############ Patient 1 Name Timer ############ #
patient1 = tk.LabelFrame(patient, text='Patient1')
patient1.grid(row=0, column=0, padx=10)

tk.Label(patient1, text='Name').grid(row=0, column=0)
tk.Label(patient1, text='Timer').grid(row=1, column=0)
n_p_1 = tk.StringVar()
n_p_1.trace('w', callback1)
tk.Entry(patient1, textvariable=n_p_1).grid(row=0, column=1)
# ------------------Timer-------------------- #
h_p_1 = tk.StringVar()
h_p_1.set('00')
m_p_1 = tk.StringVar()
m_p_1.set('00')
s_p_1 = tk.StringVar()
s_p_1.set('00')
f1 = tk.Frame(patient1)
f1.grid(row=1, column=1)
tk.Spinbox(f1,
           from_=0,
           to=23,
           wrap=True,
           textvariable=h_p_1,
           width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f1,
           from_=0,
           to=59,
           wrap=True,
           textvariable=m_p_1,
           width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f1,
           from_=0,
           to=59,
           wrap=True,
           textvariable=s_p_1,
           width=2,
           state="readonly").grid(row=0, column=2)
############################################################################################
patient2 = tk.LabelFrame(patient, text='Patient2')
patient2.grid(row=1, column=0, padx=10)

tk.Label(patient2, text='Name').grid(row=0, column=0)
tk.Label(patient2, text='Timer').grid(row=1, column=0)
n_p_2 = tk.StringVar()
n_p_2.trace('w', callback2)
tk.Entry(patient2, textvariable=n_p_2).grid(row=0, column=1)

h_p_2 = tk.StringVar()
h_p_2.set('00')
m_p_2 = tk.StringVar()
m_p_2.set('00')
s_p_2 = tk.StringVar()
s_p_2.set('00')
f2 = tk.Frame(patient2)
f2.grid(row=1, column=1)
tk.Spinbox(f2,
           from_=0,
           to=23,
           wrap=True,
           textvariable=h_p_2,
           width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f2,
           from_=0,
           to=59,
           wrap=True,
           textvariable=m_p_2,
           width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f2,
           from_=0,
           to=59,
           wrap=True,
           textvariable=s_p_2,
           width=2,
           state="readonly").grid(row=0, column=2)
################################################################################################
patient3 = tk.LabelFrame(patient, text='Patient3')
patient3.grid(row=2, column=0, padx=10)

tk.Label(patient3, text='Name').grid(row=0, column=0)
tk.Label(patient3, text='Timer').grid(row=1, column=0)
n_p_3 = tk.StringVar()
n_p_3.trace('w', callback3)
tk.Entry(patient3, textvariable=n_p_3).grid(row=0, column=1)

h_p_3 = tk.StringVar()
h_p_3.set('00')
m_p_3 = tk.StringVar()
m_p_3.set('00')
s_p_3 = tk.StringVar()
s_p_3.set('00')
f3 = tk.Frame(patient3)
f3.grid(row=1, column=1)
tk.Spinbox(f3,
           from_=0,
           to=23,
           wrap=True,
           textvariable=h_p_3,
           width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f3,
           from_=0,
           to=59,
           wrap=True,
           textvariable=m_p_3,
           width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f3,
           from_=0,
           to=59,
           wrap=True,
           textvariable=s_p_3,
           width=2,
           state="readonly").grid(row=0, column=2)

h_p_1.trace("w",callback_t_1)
m_p_1.trace("w",callback_t_1)
s_p_1.trace("w",callback_t_1)
h_p_2.trace("w",callback_t_2)
m_p_2.trace("w",callback_t_2)
s_p_2.trace("w",callback_t_2)
h_p_3.trace("w",callback_t_3)
m_p_3.trace("w",callback_t_3)
s_p_3.trace("w",callback_t_3)


root.mainloop()