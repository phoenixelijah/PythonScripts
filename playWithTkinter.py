import tkinter
# from tkinter import *

# tkinter._test()
# print(tkinter.TkVersion)

mainWindow = tkinter.Tk()

mainWindow.title("HammahTime")
mainWindow.geometry('640x480')

label = tkinter.Label(mainWindow, text="howdy")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')


mainWindow.mainloop()