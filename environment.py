import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()
def Food():
    global screen
    global dims
    y1 = 0
    y2 = dims[0] - 2
    x1 = 0
    x2 = dims[1] - 2
    y = random.randrange(y1, y2)
    x = random.randrange(x1, x2)
    screen.addch(y, x, '#')


Food()
screen.getch()
curses.endwin()
