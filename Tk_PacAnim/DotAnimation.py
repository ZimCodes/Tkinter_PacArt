from Animation import Animation
from Dot import Dot
#Implements a Dot object with animations
class DotAnimation(Animation):
    def __init__(self,canvas,animspeed=15):
        super(DotAnimation, self).__init__(canvas,animspeed)
        self.dot = Dot(canvas).dot

    def play(self):
        '''Plays the animation for the Dot object'''
        if self._canvas.coords(self.dot)[0] <= 270.0:
            self._canvas.coords(self.dot, 640, 190, 720, 270)
        else:
            self._canvas.move(self.dot, -1, 0)
        self.start_anim(self.play)
