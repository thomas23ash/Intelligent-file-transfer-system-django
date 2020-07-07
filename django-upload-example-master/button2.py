from tkinter import *
from tkFileDialog import askopenfilename
import os
import MalwareDetection as MD
window = tk() # user input window

MyText= StringVar()

def open_file(Var):
    global content


    filename = askopenfilename()
   # infile = open(filename, 'r')
    #content = infile.read()
    Var.set(filename)
    return content
def process_file(content):
    print (content)


window.title('Antivirus using MISP')
window.geometry("598x120+250+100")

mf = Frame(window)
mf.pack()


f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()

Label(f1,text="Select Your File (Only txt files)").grid(row=0, column=0, sticky='e')
Button(f1, text='Browse', command=open_file(MyText)).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
Entry(f1, textvariable = MyText).grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f2, text='Process Now', command=lambda :MD.driver(content)).grid(sticky='ew', padx=10, pady=10)

window.mainloop()
