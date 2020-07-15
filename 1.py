import tkinter as tk
from datetime import datetime

def turn():
    numbers.append(len(numbers)+1)
    print(numbers)
    d=datetime.now()
    l1.config(text=d.strftime("%B-%d-%Y"))
    a1.config(text=d.strftime("%H:%M:%S"))
    c1.config(text=d.strftime("%A"))
    s1.config(text='number of your turn : ' + str(numbers[-1]))

root=tk.Tk()

numbers=[]

l1 = tk.Label(root,text="")
l1.grid(root,row=0,column=0)

a1=tk.Label(root,text="")
a1.grid(root,row=1,column=0)

c1=tk.Label(root,text="")
c1.grid(root,row=2,column=0)

s1=tk.Label(root,text="")
s1.grid(root,row=3,column=0)

b1=tk.Button(root,text="get turn",command=turn)
b1.grid(root,row=4,column=0)

tp=tk.Toplevel(root)

k1=tk.Label(tp,text="")
k1.grid(tp,row=1,column=0)

w1=tk.Button(tp,text="op1")
w1.grid(tp,row=0,column=0)

p1=tk.Label(tp,text="")
p1.grid(tp,row=1,column=1)

z1=tk.Button(tp,text="op2")
z1.grid(tp,row=0,column=1)


j1=tk.Label(tp,text="")
j1.grid(tp,row=1,column=2)

m1=tk.Button(tp,text="op3")
m1.grid(tp,row=0,column=2)


root.mainloop()

