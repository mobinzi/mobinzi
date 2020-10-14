import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage

bgc = {
    'bg': '#64ffda'
}

def cnt(sign,j):
    j=int(j)
    
    if sign == "+":
        d[j][]
    else:
        print("-",j)
    count[j].set

i = {
    "1":{"name": "akbar chicken",
         "rating":5,
         "review":128,
         "price":2,
         "img":"images/e.gif"},
    "2":{"name": "akbar chicken",
         "rating":5,
         "review":128,
         "price":2,
         "img":"images/e.gif"},
}

d= {
     0:{"name": "cola",
           "price":2},
     1:{"name": "istak",
            "price":3}      

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
for j in range(len(i)):
    f1 = tk.Frame(food,bg='#64ffda')
    f1.grid(row=j, column=0)

    name = i["1"]["name"]
    tk.Label(f1, text=name,bg="#ff3d00").grid(row=0, column=0)

    rating = i["1"]["rating"] * "★" + "("+str(i["1"]["review"])+")"
    tk.Label(f1,text=rating,cnf=bgc).grid(row=1,column=0)

    price = str(i["1"]["rating"]) +"$"
    tk.Label(f1,text=price,cnf=bgc).grid(row=2,column=0)

    img = PhotoImage(file=i["1"]["img"]).subsample(2)
    tk.Label(f1,image=img).grid(row=0,column=1,rowspan=3)
    
    tk.Label(food,text=i[j]["count"],font=("times",15),bg="#ffc107").grid(row=0,column=1,sticky=tk.s)
    tk.Button(food,text="+",command=lambda x=str(j):cnt("+",x)).grid(row=0,column=2)
    tk.Button(food,text="-",command=lambda y=str(j):cnt("-",x)).grid(row=0,column=3)

    des = i[j]["des"]
    tk.Message(f1,
       
           
    
    )
####################
for s in range(len(d)):
    food1 = tk.Frame(drink , cnf=bgc ) 
    food1.grid(row=s , column = 0 , sticky = tk.E+tk.W)

    name = d[s]["name"]
    tk.Label(food1, text = name, cnf=bgc ).grid(row = 0 , column = 0 , pady = 5 , padx = 5 )

    
    price = str(d[s]["price"]) + "$"
    tk.Label(food1, text = price , cnf=bgc ).grid(row = 2 , column = 0 , pady = 5 )

root.mainloop()
