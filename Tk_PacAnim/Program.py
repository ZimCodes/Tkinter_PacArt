from tkinter import *
#Similar to public static void Main(string[] args)
from PacAnimApp import PacAnimApp

root = Tk()
canvas = Canvas(root,width=640,height=480,background='grey2')
canvas.pack()
app = PacAnimApp(root,canvas)
app.startapp()
root.mainloop()