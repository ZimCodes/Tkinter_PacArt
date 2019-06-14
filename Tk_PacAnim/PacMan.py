
#Creates a Pacman object
class PacMan():
    def __init__(self,canvas):
        self.pacman = canvas.create_arc(260,180,360,280,start=40,extent=280,fill='yellow')
