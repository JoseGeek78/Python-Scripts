from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init()
        self.shape('square')
        