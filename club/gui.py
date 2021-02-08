import tkinter as tk


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Label(self,text="First name").grid(row=0,column=0)
        name = tk.StringVar()
        tk.Entry(self).grid(row=0,column=1)
        

    def main(self):
        self.mainloop()

