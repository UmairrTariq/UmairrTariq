import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title(' TAB CONTROL')
nb = ttk.Notebook(win)
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
nb.add(p1,text = 'ONE')
nb.add(p2,text = 'TWO')
nb.pack(expand = True,fill = 'both')
label1 = ttk.Label(p1,text = 'This is Label: ')
label1.grid(row = 0,column = 0)
e1 = ttk.Entry(p1,width = 26)
e1.grid(row = 0,column = 1)
label2 = ttk.Label(p2,text = 'This is Label: ')
label2.grid(row = 0, column = 0)
e2 = ttk.Entry(p2,width = 26)
e2.grid(row = 0,column = 1)

win.mainloop()