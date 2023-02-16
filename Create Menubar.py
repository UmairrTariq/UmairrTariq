import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Menubar Tutorial')

def func():
    print("Function called")
menu = tk.Menu(win)
menu.add_command(label='Save',command=func)
menu.add_command(label='Save as',command=func)
menu.add_command(label='Copy',command=func)
menu.add_command(label='Paste',command=func)

f = tk.Menu(menu,tearoff=0)
f.add_command(label='New Window',command=func)
f.add_command(label='New File',command=func)
f.add_separator()
f.add_command(label='Save File',command=func)

edit = tk.Menu(menu,tearoff=0)
edit.add_command(label='Redo',command=func)
edit.add_command(label='Undo',command=func)

menu.add_cascade(label='File',m=f)
menu.add_cascade(label='Edit',m=edit)


win.config(m=menu)
win.mainloop()