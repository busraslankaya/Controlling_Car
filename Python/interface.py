import os
from tkinter import *
from tkinter.ttk import *

window=Tk()

window.title("Controlling car with Image Processing")
window.geometry('1000x700')
 
def run():
    os.system('main.py')
Label(window, text = 'OPEN THE CAMERA', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Label(window, text = '--Show your hand-- \n\n1:Forward  2:Backward \n3:Right      4:Left \n5:Stop   ', font =(
  'Verdana', 10)).pack(side = BOTTOM, pady = 10)
photo = PhotoImage(file = r"C:\Users\HP\Desktop\3.png")

Button(window, text = 'Click Me !', image = photo,command=run).pack(side = TOP)

 
window.mainloop() 

