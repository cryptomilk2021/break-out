from turtle import Turtle

ROWS = 5
COLUMNS = 10

class Tiles(Turtle):

    def __init__(self):
        super().__init__()
        self.all_tiles = []
        self.create_tiles(6, 11)

    def create_tiles(self, rows, columns):
        x_offset = -354
        y_offset = 280
        x_buffer = 70
        y_buffer = 30
        colour = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        for i in range(columns):
            for j in range(rows):
                new_tile = Turtle("square")
                new_tile.color(colour[j])
                new_tile.shapesize(stretch_wid=1, stretch_len=3)
                new_tile.penup()
                y_offset = y_offset - y_buffer
                new_tile.goto(x_offset, y_offset)
                self.all_tiles.append(new_tile)
                # print(f'i = {i}, j = {j}, x_offset = {x_offset}, y_offset = {y_offset}')

            x_offset = x_offset + x_buffer
            y_offset = 280
