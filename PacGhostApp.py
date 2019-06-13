from GhostBuilder import Ghostbuilder
from tkinter import *
from tkinter import ttk
class PacGhostApp():
    def __init__(self,master,ghostcolor='magenta',eyecolor='blue'):
        self._master = master
        self._canvas = Canvas(master, width=400,height=350,relief=SUNKEN,background='white')
        self._canvas.grid(column=0,row=0,columnspan=3)
        self._ghostbuilder = Ghostbuilder(master,self._canvas,ghostcolor,eyecolor)
        self._entrytxt = None
        self._entrytxttwo = None
        self._checkbox =None
        self._checkvar = BooleanVar()
        self._leftstem = None
        self._rightstem = None
        self._mostachebase = None

    def StartApp(self):
        '''Starts the application
        :return:
        '''
        self._ghostbuilder.ConstructGhost()
        ttk.Label(self._master, text="Change Body Color:").grid(row=1, column=0)
        self._entrytxt = ttk.Entry(self._master, width=15)
        self._entrytxt.grid(row=2, column=0)

        self._ghostbuilder.ConstructGhost()
        ttk.Label(self._master, text="Change Eye Color:").grid(row=1, column=2)
        self._entrytxttwo = ttk.Entry(self._master, width=15)
        self._entrytxttwo.grid(row=2, column=2)

        button = ttk.Button(self._master, text="submit",command=self._ChangeBodyColor)
        button.grid(row=3, column=0, pady=10)
        button = ttk.Button(self._master, text="submit",command=self._ChangeEyeColor)
        button.grid(row=3, column=2, pady=10)

        self._checkbox = ttk.Checkbutton(self._master,text="moustache",variable=self._checkvar,onvalue=True,offvalue=False,command=self._Moustache)
        self._checkbox.grid(row=2,column=1)

    def _ChangeBodyColor(self):
        '''
        Event Command to change the body color of ghost
        :return:
        '''
        newcolor = self._entrytxt.get()
        for x in self._ghostbuilder.GetBodyAssets():
            self._canvas.itemconfig(x, fill=newcolor)

    def _ChangeEyeColor(self):
        '''
        Event Command to change the eye color of ghost
        :return: None
        '''
        newcolor = self._entrytxttwo.get()
        for x in self._ghostbuilder.GetEyeAssets():
            self._canvas.itemconfig(x, fill=newcolor)

    def _Moustache(self):
        '''
        Event Command to add/remove moustache on ghost
        :return:
        '''
        if self._checkvar.get() == True:
            self._leftstem = self._canvas.create_arc(150, 200, 250, 300, start=180, extent=45, fill='grey7')
            self._rightstem = self._canvas.create_arc(150, 200, 250, 300, extent=-45, fill='grey7')
            self._mostachebase = self._canvas.create_arc(150, 200, 250, 300, extent=180, fill='black')
        else:
            self._canvas.delete(self._leftstem,self._rightstem,self._mostachebase)
