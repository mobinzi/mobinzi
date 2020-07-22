import tkinter as tk
from datetime import datetime


def turn():
    global n
    n += 1
    numbers.append(n + 1)
    print(numbers)
    d = datetime.now()
    l1.config(text=d.strftime("%B-%d-%Y"))
    a1.config(text=d.strftime("%H:%M:%S"))
    c1.config(text=d.strftime("%A"))
    s1.config(text='number of your turn : ' + str(numbers[-1]))
    s2.config(text="left:"+str(len(numbers)-1))
    line ="{},{},{}\n".format(numbers[-1],
                              d.strftime("%H:%M:%S"),
                              d.strftime("%d-%d-%Y"))
    with open("turns.csv","a") as file:
        file.write(line)

def append_csv(number,operator) :
    d=datetime.now()
    line = "{},{},{},operator{}\n".format(number,
                                          d.strftime("%H:%M:%S"),
                                          d.strftime("%d-%d-%Y"),
                                          operator)
    with open("operators.csv", "a") as file:
        file.write(line)


def op1():
    if numbers:
        number = numbers.pop(0)
        k1.config(text=number)
        append_csv(number,1)


def op2():
    if numbers:
        number = numbers.pop(0)
        p1.config(text=number)
        append_csv(number, 2)



def op3():
    if numbers:
        number = numbers.pop(0)
        j1.config(text=number)
        append_csv(number, 3)

root = tk.Tk()
n = -1
numbers = []

l1 = tk.Label(root, text="")
l1.grid(row=0, column=0)

a1 = tk.Label(root, text="")
a1.grid(row=1, column=0)

c1 = tk.Label(root, text="")
c1.grid(row=2, column=0)

s1 = tk.Label(root, text="")
s1.grid(row=3, column=0)

s2 = tk.Label(root, text="")
s2.grid(row=4, column=0)

b1 = tk.Button(root, text="get turn", command=turn)
b1.grid(row=5, column=0)

tp = tk.Toplevel(root)

k1 = tk.Label(tp, text="")
k1.grid(row=1, column=0)

w1 = tk.Button(tp, text="op1", command=op1)
w1.grid(row=0, column=0)

p1 = tk.Label(tp, text="")
p1.grid(row=1, column=1)

z1 = tk.Button(tp, text="op2", command=op2)
z1.grid(row=0, column=1)

j1 = tk.Label(tp, text="")
j1.grid(row=1, column=2)

m1 = tk.Button(tp, text="op3", command=op3)
m1.grid(row=0, column=2)

root.mainloop()
