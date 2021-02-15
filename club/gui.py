import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        tk.Label(self,text="First name").grid(row=0,column=0)
        self.name = tk.StringVar()
        tk.Entry(self, textvariable=self.name).grid(row=0,column=1)
        
        tk.Label(self,text="Last name").grid(row=1,column=0)
        self.last = tk.StringVar()
        tk.Entry(self,textvariable=self.last).grid(row=1,column=1)
        tk.Button(self,text="Create",command=self.create).grid(row=2,column=1)

        tk.Label(self,text="birth").grid(row=2,column=0)
        self.birth = tk.StringVar()        
        DateEntry(self,textvariable=self.birth,date_patttern="y-mm-dd",background="darkblue",foreground="white").grid(row=2,column=1)


    def create(self):
        print(self.name.get(),self.last.get())




        
    def main(self):
        self.mainloop()

