import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Left player").grid(row=0, column=0)
tk.Label(root, text="Right PLayer").grid(row=0, column=1)

l_timer = tk.StringVar()
l_timer.set("20:00")
tk.Label(root, textvariable=l_timer).grid(row=1, column=0)

r_timer = tk.StringVar()
r_timer.set("20:00")
tk.Label(root, textvariable=r_timer).grid(row=1, column=1)

tk.Button(root, text="stop").grid(row=2, column=0)
tk.Button(root, text="stop").grid(row=2, column=1)

c1 = tk.Button(root, text="start")
c1.grid(row=3, column=0, columnspan=2)

d1 = tk.Button(root, text="cancel")
d1.grid(row=4, column=0, columnspan=2)

root.mainloop()
