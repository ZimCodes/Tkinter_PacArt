from Animation import Animation
from PacMan import PacMan
#Implements a Pacman object with animations
class PacAnimation(Animation):
    def __init__(self,canvas,animspeed=10,minlimit=1,maxlimit=50):
        super(PacAnimation, self).__init__(canvas,animspeed)
        self.minlimit = minlimit
        self.maxlimit = maxlimit
        self.pacman = PacMan(canvas).pacman
        self.speed = 1.0


    def play(self):
        '''Plays the animation'''
        startarc = float(self._canvas.itemcget(self.pacman, 'start'))
        endarc = float(self._canvas.itemcget(self.pacman, 'extent'))
        if startarc == self.minlimit or startarc == self.maxlimit:
            self.speed = -1.0 * self.speed

        self.pacanim_move(startarc, endarc)
        self.start_anim(self.play)


    def pacanim_move(self,startarc, endarc):
        '''Controls the mouth of Pacman '''
        self._canvas.itemconfig(self.pacman, start=startarc + self.speed, extent=endarc - self.speed * 2.0)
