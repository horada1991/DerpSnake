import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()


def level2():
    global dims
    global screen

    screen.addstr(int(dims[0]/2), int(dims[1]/6), "X" * int(dims[1]*4/6+1), curses.color_pair(3))
    for i in range(int(dims[0]/6), int(dims[0]*5/6 + 1)):
        screen.addch(i, int(dims[1]/2), "X", curses.color_pair(2))


def level3():
    global dims
    global screen

    level2()
    for i in range(int(dims[0]/4), int(dims[0]*3/4)):
        screen.addch(i, int(dims[1]/6), "X", curses.color_pair(2))
        screen.addch(i, int(dims[1]*5/6), "X", curses.color_pair(2))
