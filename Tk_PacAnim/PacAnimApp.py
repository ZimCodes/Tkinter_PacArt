from tkinter import ttk
from PacAnimation import PacAnimation
from DotAnimation import DotAnimation
#Manages the Application
class PacAnimApp():
    def __init__(self,master,canvas,dotspeed=15,pacspeed=10,minlimit=1,maxlimit=50):
        self.master = master
        self.canvas = canvas
        self.dotanim = DotAnimation(canvas,dotspeed)
        self.pacanim = PacAnimation(canvas,pacspeed,minlimit,maxlimit)
        self.activated = True

    def playanims(self):
        '''Plays all animations'''
        if self.activated:
            self.pacanim.play()
            self.dotanim.play()
            self.activated = False
        else:
            self.pacanim.stop_anim()
            self.dotanim.stop_anim()
            self.activated = True

    def startapp(self):
        '''Starts the Application'''
        self.canvas.bind('<ButtonPress>',lambda e: self.playanims())
        ttk.Label(self.master, text='Click to play!', font=('', 18, 'bold'),foreground='blue').pack()