from tkinter import *
from tkinter import filedialog
import button2new as bt

window = Tk() # user input window

MyText= StringVar()



b=Button(window, text='CHECK', command=bt.driver(),state=DISABLED)
b.pack()


Button(window, text='UPDATE', command=window.destroy).pack()

window.mainloop()