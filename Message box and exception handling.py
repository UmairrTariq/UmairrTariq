import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win = tk.Tk()
label_frame = ttk.LabelFrame(win,text = 'Contact Details')
label_frame.grid(row=0,column=0,padx=40,pady=10)
name_label = ttk.Label(label_frame,text= 'Enter your name Please...',font=('Times New Roman',15))
age_label = ttk.Label(label_frame,text= 'Enter your age Please...',font=('Times New Roman',15))
name_var=tk.StringVar()
age_var=tk.StringVar()
name_entry = ttk.Entry(label_frame,width = 36,textvariable = name_var)
age_entry = ttk.Entry(label_frame,width = 36,textvariable = age_var)
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    n = name_var.get()
    age = age_var.get()
    if n == '' or age == '':
        m_box.showerror("Error",'Please Enter both name and age: ')
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('title','Only digits are allowed in age')
        else:
            if age<18:
                m_box.showwarning('Warning','You are not allowed!!')
            else:
                print(f'{n} : {age}')
                        
submit_btn = ttk.Button(win,text='Submit',command = submit)
submit_btn.grid(row = 1,columnspan = 2,padx = 40)
win.mainloop()


