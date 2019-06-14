#Creates a Dot object
class Dot():
    def __init__(self,canvas):
        self.dot = canvas.create_oval(640,190,720,270,fill='grey50')
