import tkinter as tk

root=tk.TK()

l1=tk.Label(root,text="L1",bg="yellow",font(times,20))
l1.grid(row=0,column=0,rowspan=3,sticky=tk.N+tk.S)

l2=tk.Label(root,text="L2",bg="black",font("times",20))
l2.grid(row=0,column=1,columnspan=3,sticky=tk.W+tk.E)

l3=tk.Label(root,text="L3",bg="yellow",font("times",20))
l3.grid(row=1,column=1,rowspan=2,sticky=tk.N+tk.S)


l4=tk.Label(root,text="L4",bg="green",font("times",20))
l4.grid(row=1,column=2,rowspan=2,sticky=tk.N+tk.S)

l5=tk.Label(root,text="L5",bg="red",font("times",20))
l5.grid(row=1,column=3)

l6=tk.Label(root,text="L6",bg="pink",font("times",20))
l6.grid(row=2,column=3)
