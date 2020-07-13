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
l1.pack()

a1=tk.Label(root,text="")
a1.pack()

c1=tk.Label(root,text="")
c1.pack()

s1=tk.Label(root,text="")
s1.pack()

b1=tk.Button(root,text="get turn",command=turn)
b1.pack()

root.mainloop()

