#Super class for Animations
class Animation:
    def __init__(self, canvas, animspeed):
        self._canvas = canvas
        self._animspeed = animspeed
        self._timer = None

    def stop_anim(self):
        '''Stops an animation loop'''
        self._canvas.after_cancel(self._timer)

    def start_anim(self,func):
        '''Starts an animation loop'''
        self._timer = self._canvas.after(self._animspeed,func)
