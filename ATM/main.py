import tkinter as tk
import tkinter.ttk as ttk
import hashlib
import json
import datetime
from tkinter import messagebox
import random

def deposite():
    dps = Toplevel()
    tk.Label(dps, text="amount").grid(row=0,column=0)
    deposite_amount= tk.IntVar()
    tk.Entry(dps,textvariable=deposite_amount).grid(row=0,column=1)
    tk.Button(dps, text="deposite").grid(row=1,column=0,columnspan=2)
    tk.Button(dps, text="close").grid(row=2,column=0,columnspan=2)
    
    
def get_card_number():
    last = read_json("names.json")
    if not last:
        return random.randint(6000000000000000,7000000000000000)
    else:
        return last[-1]["card_number"] + random.randint(1000,9999)


def get_datetime():
    frm = "%A,  %H::%M:%S,  %B-%d-%Y"
    return datetime.datetime.now().strftime(frm)


def read_json(address):
    with open(address)as file:
        return json.load(file)



def write_json(address,data):      
    with open(address,"w",encoding="utf-8")as file:
        json.dump(data,file,ensure_ascii=False,indent=4)


def to_sha1(password):
    return hashlib.sha1(password.encode("utf-8")).hexdigest()


def register():
    input_user = form_user.get()
    file= read_json("names.json")
    all_user=[]
    for person in file:
        all_users.append(person["username"])
    if not input_user:
        messagebox.showerror("username Error , Please enter a username ")    
    elif input_user not in all_user:
        if not form_pass.get():
             messagebox.showerror("Password Error , Please enter a password ")
        else:
            input_pass = to_sha1(form_pass.get())

            form_user.set("")
            form_pass.set("") 
            file=read_json("names.json")
            data={
            "username":input_user,
            "password":input_pass,
            "created":get_datetime(),
            "card_number":get_card_number(),
            }
            file.append(data)
            write_json("names.json",file)
    else:
       messagebox.showerror("Username Error","This username is not available ")   

def find_person(file,username):
    for person in file:
        if person["username"] == username:
            return person
    messagebox.showerror("Username Erorr","Entered inavalid username")       
    return None

def login():
    username= login_user.get()
    password= to_sha1(login_pass.get())
    file= read_json("names.json")
    person = find_person(file,username)
    if person is None:
        pass
    else:
        if person["password"]== password:
            top.deiconify()
            root.withdraw()
        else:
            messagebox.showerror("password Erorr","Entered inavalid password")  



root=tk.Tk()
root.title("Bank")

top=tk.Toplevel()
top.title("main menu")
top.withdraw()
note= ttk.Notebook()
register_form= tk.Frame()
login_form=tk.Frame()
note.add(register_form,text="Register")
note.add(login_form,text="Log In")

note.grid(row=0,column=0)
#####################register##########################
tk.Label(register_form,text="UserName:").grid(row=0,column=0)
tk.Label(register_form,text="Password").grid(row=1,column=0)
form_user=tk.StringVar()
form_pass=tk.StringVar()
tk.Entry(register_form,textvariable=form_user).grid(row=0,column=1)
tk.Entry(register_form,textvariable=form_pass,show="*").grid(row=1,column=1)
tk.Button(register_form,text="Register",command=register).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)
######################################################
#####################Login############################
tk.Label(login_form,text="UserName:").grid(row=0,column=0)
tk.Label(login_form,text="Password").grid(row=1,column=0)
login_user=tk.StringVar()
login_pass=tk.StringVar()
tk.Entry(login_form,textvariable=login_user).grid(row=0,column=1)
tk.Entry(login_form,textvariable=login_pass).grid(row=1,column=1)
tk.Button(login_form,text="login",command=login).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)
###############toplevel#######################################
tk.Button(top,text="transfer",command=login).grid(row=0,column=0,sticky=tk.W+tk.E)
tk.Button(top,text="deposite",command=deposite).grid(row=0,column=1,sticky=tk.W+tk.E)
tk.Button(top,text="balance",command=login).grid(row=1,column=0,sticky=tk.W+tk.E)
tk.Button(top,text="change paswword",command=login).grid(row=1,column=1,sticky=tk.W+tk.E)
tk.Button(top,text="+1000",command=root.destroy).grid(row=2,column=0,sticky=tk.W+tk.E)
tk.Button(top,text="Exit",command=root.destroy).grid(row=2,column=1,columnspan=2,sticky=tk.W+tk.E)

root.mainloop()
