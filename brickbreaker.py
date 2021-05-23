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

# Constants for the ball
BALL_SIZE = 40
CHANGE_X_START = 10
CHANGE_Y_START = 7

# Constants for the paddle
PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 80

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "J's Brick Breaker")

    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_brick(canvas, row, col)

    load_ball(canvas)
    canvas.mainloop()

def draw_brick(canvas, row, col):
    x = col * BRICK_WIDTH
    y = row * BRICK_HEIGHT
    color = get_color(row, col)
    canvas.create_rectangle(x + SPACING, y + SPACING, x + BRICK_WIDTH, y + BRICK_HEIGHT, fill=color)

def get_color(row, col):
    return int_to_color(col * row * row)

def int_to_color(value):
    # white is the largest value one can represent
    white_dec = int('ffffff', 16)
    # change your value into "hexadecimal" representation
    hex_str = format(value % white_dec, 'x')
    # add 0s to the end until its the right length
    while len(hex_str) < 6:
        hex_str += '0'
    # you now have a color!
    return '#' + hex_str

def load_ball(canvas):
    # Ball
    ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill='green', outline='green')
    change_x = CHANGE_X_START
    change_y = CHANGE_Y_START
    while True:
        # update world
        canvas.move(ball, change_x, change_y)
        # if hit left or right wall, bounce off
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            change_x *= -1
        # NEED TO UPDATE: if hit a brick, break it and bounce back
        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            change_y *= -1
        # NEED TO UPDATE: if hit bottom wall, game over

        # NEED TO UPDATE: if hit paddle, bounce back

        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50)

    # canvas.mainloop()

def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas of the given int size
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    # canvas.bind("<Motion>", mouse_moved)
    return canvas

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT

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

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]

# def mouse_moved(event):
#     print('x = ' + str(event.x), 'y = ' + str(event.y))


if __name__ == '__main__':
    main()
