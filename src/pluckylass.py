import pyglet
from src.shapes import *

class PluckyLass(object):
    def __init__(self):
        self.position = Vect(32, 32)
        self.direction = None
        self.delta = Vect()
        self.hue = 'G'

    def mupdate(self, dt):
        if self.direction == 'N':
            self.delta = Vect(y=1)
        elif self.direction == 'E':
            self.delta = Vect(x=1)
        elif self.direction == 'S':
            self.delta = Vect(y=-1)
        elif self.direction == 'W':
            self.delta = Vect(x=-1)
        else:
            self.delta = Vect()

class PluckyLassView(object):
    def __init__(self, model):
        self.model = model
        self.grid = pyglet.image.ImageGrid(pyglet.resource.image('basictiles.png'), 15, 8)[32:40]
        self.image = self.grid[0]

    def setup(self):
        self.sprite = pyglet.sprite.Sprite(self.image)

    def vupdate(self, screen_offset):
        self.sprite.position = self.model.position * 15 + screen_offset
        if self.model.direction == 'N':
            self.image = self.grid[4]
        elif self.model.direction == 'E':
            self.image = self.grid[2]
        elif self.model.direction == 'S':
            self.image = self.grid[0]
        elif self.model.direction == 'W':
            self.image = self.grid[6]
        self.sprite.image = self.image