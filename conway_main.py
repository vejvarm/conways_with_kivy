import numpy as np
import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.clock import Clock
from kivy.uix.button import Label

SIZE = 50
GRID = np.zeros((SIZE, SIZE), dtype='bool')


class MyLayout(BoxLayout):
    pass


class MyWidget(Widget):

    def update_canvas(self):
        global GRID

        horpos = 0
        verpos = 0
        pad = 1
        self.size = self.size
        horsize = self.size[0] - pad
        versize = self.size[1] - pad

        self.canvas.clear()

        with self.canvas:
            for i in range(SIZE):
                for j in range(SIZE):
                    if GRID[i, j]:
                        Color(1, 1, 1, 1)  # colour of the live cells
                    else:
                        Color(0.1, 0.1, 0.1, 1)  # colour of the dead cells
                    Rectangle(pos=(horpos, verpos), size=(horsize // SIZE, versize // SIZE))
                    verpos += versize // SIZE + pad
                horpos += horsize // SIZE + pad
                verpos = 0

    def generate_random(self):
        global GRID

        rand_grid = np.random.randint(0, 2, (10, 10), dtype='bool')
        GRID[SIZE//2-5:SIZE//2+5, SIZE//2-5:SIZE//2+5] = rand_grid

        self.update_canvas()

    def next_generation(self, dt=0.1, run=True):
        global GRID

        # dead cell with 3 live around -- alive
        # live cell with 2 or 3 live around -- alive
        # else cell -- dead
        for i in range(SIZE):
            for j in range(SIZE):
                live_cells = np.sum(GRID[max(i - 1, 0):i + 2, max(j - 1, 0):j + 2]) - 1 if GRID[i, j] else np.sum(
                    GRID[max(i - 1, 0):i + 2, max(j - 1, 0):j + 2])
                if live_cells == 3:
                    GRID[i, j] = True
                elif GRID[i, j] and live_cells == 2:
                    GRID[i, j] = True
                else:
                    GRID[i, j] = False

        self.update_canvas()

    def schedule_generation(self, run=True):
        if run:
            self.EVENT = Clock.schedule_interval(self.next_generation, 0.1)
        else:
            self.EVENT.cancel()

    def clear_canvas(self):
        global GRID

        GRID = np.zeros((SIZE, SIZE), dtype='bool')
        self.update_canvas()

class ConwayApp(App):

    def build(self):
        self.mL = MyLayout()
        self.mL.mywidge.update_canvas()
        return self.mL


conApp = ConwayApp()
conApp.run()
