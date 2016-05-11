import curses
import time
import random
import piton
import environment

curses.noecho()
screen = curses.initscr()
screen.nodelay(1)
screen.keypad(1)
dims = screen.getmaxyx()

Coords = [int(dims[0] / 2), int(dims[1] / 2), int(dims[0] / 2), int(dims[1] / 2-1),
                int(dims[0] / 2), int(dims[1] / 2-2)]
move_y = 0
move_x = 0
q = -1
screen.border()
screen.addstr(0, 5, "   Score:   ")

while q != ord("q"):
    q = screen.getch()
    if q == curses.KEY_UP:
        move_y, move_x = 1, 0
    elif q == curses.KEY_DOWN:
        move_y, move_x = -1, 0
    elif q == curses.KEY_LEFT:
        move_y, move_x = 0, -1
    elif q == curses.KEY_RIGHT:
        move_y, move_x = 0, 1
    y_head = Coords[0] + move_y
    x_head = Coords[1] + move_x
    piton.DelSnake(Coords)
    Coords = piton.MovingCoords(Coords, y_head, x_head)
    if Coords == 0:
        screen.addstr(5, 5, "GAME OVER")
        q = ord("q")
    else:
        piton.PrintSnake(Coords)
        piton.Eat(Coords, x_head, y_head)
        time.sleep(0.1)

screen.nodelay(0)
screen.getch()
curses.endwin()

""" Levels()
    Score()
    Move

"""
