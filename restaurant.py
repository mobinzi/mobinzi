import tkinter as tk
import tkinter.ttk as ttk


bgc = {
    'bg': '#64ffda'
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
tk.Label(f1, text="akbar chicken",bg="#ff3d00").grid(row=0, column=0)
tk.Label(f1,text="★★★★★",cnf=bgc).grid(row=1,column=0)
tk.Label(f1,text="2$$$$",cnf=bgc).grid(row=2,column=0)
####################
 

root.mainloop()
