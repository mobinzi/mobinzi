import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()

food = tk.Frame()
drink = tk.Frame()
rescipt = tk.Frame()

note = ttk.Notebook()
note.grid(row=0,column=0)

note.add(food, text="Food")
note.add(drink, text="Drinks")
note.add(rescipt, text="Rescipt")


root.mainloop()
