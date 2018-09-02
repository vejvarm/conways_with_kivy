import numpy as np

from collections import namedtuple
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.clock import Clock

field = namedtuple('field', ['rows', 'cols'])
FIELD = field(30, 60)


class UILayout(BoxLayout):

    def __init__(self):
        super().__init__()


class Grid(GridLayout):
    cells = np.zeros((FIELD.rows, FIELD.cols), dtype='bool')
    neighbours = {(i, j): 0 for i in range(FIELD.rows) for j in range(FIELD.cols)}
    Colours = {False: (0.1, 0.1, 0.1, 1), True: (1, 0, 0, 1)}
    event = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cols = FIELD.cols
        # fill the grid
        for row in range(FIELD.rows):
            for col in range(FIELD.cols):
                self.grid_entry = GridEntry(coords=(row, col))
                self.grid_entry.bind(on_release=self.button_pressed)
                self.add_widget(self.grid_entry)

    def button_pressed(self, button):
        row, col = button.coords

        # update the cell's state in the cells list:
        self.cells[row, col] = not self.cells[row, col]

        # change the button colour
        button.background_color = self.Colours[self.cells[row, col]]

    def neighbourhoods(self):
        # update neighbours
        for row in range(FIELD.rows):
            for col in range(FIELD.cols):
                if self.cells[row, col]:  # if cell is alive subtract 1
                    self.neighbours[(row, col)] = np.sum(
                        self.cells[max(row - 1, 0):row + 2, max(col - 1, 0):col + 2]) - 1
                else:
                    self.neighbours[(row, col)] = np.sum(self.cells[max(row - 1, 0):row + 2, max(col - 1, 0):col + 2])

    def next_generation(self, dt=0):
        # update neighbours dictionary
        self.neighbourhoods()

        # update the cell states in cells array
        for row in range(FIELD.rows):
            for col in range(FIELD.cols):
                if self.neighbours[(row, col)] == 3:
                    self.cells[row, col] = True
                elif self.cells[row, col] and self.neighbours[(row, col)] == 2:
                    self.cells[row, col] = True
                else:
                    self.cells[row, col] = False

                # update the colour of the Cells depending on their state
                self.children[-FIELD.cols * row - col - 1].background_color = self.Colours[self.cells[row, col]]

    def clear(self):
        self.cells = np.zeros((FIELD.rows, FIELD.cols), dtype='bool')
        self.neighbours = {(i, j): 0 for i in range(FIELD.rows) for j in range(FIELD.cols)}
        # update the colour of the Cells depending on their state
        for child in self.children:
            child.background_color = self.Colours[False]

    def random(self):
        self.cells = np.random.choice(a=[False, True], size=(FIELD.rows, FIELD.cols), p=[0.8, 0.2])

        # update the colour of the Cells depending on their state
        for row in range(FIELD.rows):
            for col in range(FIELD.cols):
                self.children[-FIELD.cols * row - col - 1].background_color = self.Colours[self.cells[row, col]]

    def auto_run(self):
        if not self.event and self.tgl.state == 'down':
            self.event = Clock.schedule_interval(self.next_generation, 0.1)
        elif self.event and self.tgl.state == 'normal':
            self.event.cancel()
            self.event = None


class GridEntry(Button):
    coords = ListProperty([0, 0])


class Menu(BoxLayout):
    pass


class ConwayApp(App):

    def build(self):
        return UILayout()


if __name__ == '__main__':
    conApp = ConwayApp()
    conApp.run()
