#Uses Builder Pattern
class Ghostbuilder():
    def __init__(self,master,canvas,ghostcolor,eyecolor):
        self._bodyComp = list()
        self._eyeComp = list()
        self._canvas = canvas
        self._headlowerbody = 250
        self._pointyfeetlength = 40
        self._ghostcolor = ghostcolor
        self._eyecolor = eyecolor
        self._feetsize = self._headlowerbody + self._pointyfeetlength

    def ConstructGhost(self):
        '''Builds a Ghost'''
        self._buildBody()
        self._buildHead()
        self._buildFeet()
        self._buildEyes()

    def _buildBody(self):
        '''Construct a body'''
        squarebody = self._canvas.create_rectangle(100,100,300,self._headlowerbody,fill=self._ghostcolor)
        self._bodyComp.append(squarebody)

    def _buildHead(self):
        '''Construct a head'''
        #Head
        archead = self._canvas.create_arc(100,10,300,190,extent=180,fill=self._ghostcolor)
        self._bodyComp.append(archead)
        #Head&body mask
        ovalmask = self._canvas.create_oval(101,50,299,150,fill=self._ghostcolor,width=0.0)
        self._bodyComp.append(ovalmask)
    def _buildFeet(self):
        '''Construct feet'''
        # Feet
        trifoot = self._canvas.create_polygon(100, self._headlowerbody, 125, self._feetsize, 150, self._headlowerbody, fill=self._ghostcolor,outline='black')
        self._bodyComp.append(trifoot)
        trifoot2 = self._canvas.create_polygon(150, self._headlowerbody, 175, self._feetsize, 200, self._headlowerbody, fill=self._ghostcolor,outline='black')
        self._bodyComp.append(trifoot2)
        trifoot3 = self._canvas.create_polygon(200, self._headlowerbody, 225, self._feetsize, 250, self._headlowerbody, fill=self._ghostcolor,outline='black')
        self._bodyComp.append(trifoot3)
        trifoot4 = self._canvas.create_polygon(250, self._headlowerbody, 275, self._feetsize, 300, self._headlowerbody, fill=self._ghostcolor,outline='black')
        self._bodyComp.append(trifoot4)
        # Body&Feet mask
        linemask = self._canvas.create_line(102, self._headlowerbody, 299, self._headlowerbody, width=4.0, fill=self._ghostcolor)
        self._bodyComp.append(linemask)
    def _buildEyes(self):
        '''Construct eyes'''
        # Left Eye
        lefteye = self._canvas.create_oval(110, 100, 195, 185, fill='grey96')
        leftlens = self._canvas.create_oval(140, 125, 180, 165, fill=self._eyecolor)
        self._eyeComp.append(leftlens)
        leftglow = self._canvas.create_oval(140, 130, 165, 150, fill='white')
        # Right Eye
        righteye = self._canvas.create_oval(290, 100, 205, 185, fill='grey96')
        rightlens = self._canvas.create_oval(270, 125, 230, 165, fill=self._eyecolor)
        self._eyeComp.append(rightlens)
        rightglow = self._canvas.create_oval(255, 130, 230, 150, fill='white')

    def GetBodyAssets(self):
        '''
        :return: a list of body components for the ghost
        '''
        return self._bodyComp

    def GetEyeAssets(self):
        '''
        :return: a list of eye components for the ghost
        '''
        return self._eyeComp


