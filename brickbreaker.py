"""
File: brickbreaker.py
----------------
The classic Brick Breaker game
"""

import tkinter
import time
import random

# The playing area
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 800

# Constants for the bricks
N_ROWS = 8
N_COLS = 10
# Space between bricks
SPACING = 5
# The y coordinate of the top-most brick
BRICK_START_Y = 50
# brick height in pixels
BRICK_HEIGHT = 20
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS+1) * SPACING) / N_COLS

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "J's Brick Breaker")
    #
    canvas.mainloop()


def get_top_y(canvas, object):
    """
    Returns the y coordinate of the top of an object.
    canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 1 is the top-y
    """
    return canvas.coords(object)[1]

def get_left_x(canvas, object):
    """
    Returns the x coordinate of the left of an object.
    canvas.coords(object) returns a list of the object
    bounding box: [x_1, y_1, x_2, y_2]. The element at index 0 is the left-x
    """
    return canvas.coords(object)[0]

def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas of the given int size
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()
