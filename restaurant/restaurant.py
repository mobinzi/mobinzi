import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage

bgc = {
    'bg': '#64ffda'
}

i = {
    "1":{"name": "akbar chicken",
         "rating":5,
         "review":128,
         "price":2,
         "img":"restaurant/images/e.gif"},
}

root = tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)

food = tk.Frame()
drink = tk.Frame()
rescipt = tk.Frame()

note.add(food, text="Food")
note.add(drink, text="Drinks")
note.add(rescipt, text="Rescipt")

# ###################foods################### #
f1 = tk.Frame(food,bg='#64ffda')
f1.grid(row=0, column=0)

name = i["1"]["name"]
tk.Label(f1, text=name,bg="#ff3d00").grid(row=0, column=0)

rating = i["1"]["rating"] * "★" + "("+str(i["1"]["review"])+")"
tk.Label(f1,text=rating,cnf=bgc).grid(row=1,column=0)

price = str(i["1"]["rating"]) +"$"
tk.Label(f1,text=price,cnf=bgc).grid(row=2,column=0)

img = PhotoImage(file=i["1"]["img"]).subsample(2)
tk.Label(f1,image=img).grid(row=0,column=1,rowspan=3)
####################


root.mainloop()
