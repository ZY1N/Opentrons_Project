from tkinter import *

HEIGHT = 1000
WIDTH = 1000
 
from tkinter import ttk
 
window = Tk()

window.geometry("800x1000") 
window.title("42 Opentrons App")

tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Main')
 
tab_control.add(tab2, text='Camera')
 
lbl1 = Label(tab1, text= 'label1')
 
lbl1.grid(column=0, row=0)
 
lbl2 = Label(tab2, text= 'label2')
 
lbl2.grid(column=0, row=0)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()
