import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()


def level1():
    global dims
    global screen

    screen.addstr(int(dims[0]/2), int(dims[1]/6), "X" * int(dims[1]*4/6+1))
    for i in range(int(dims[0]/6), int(dims[0]*5/6 + 1)):
        screen.addch(i, int(dims[1]/2), "X")


def level2():
    global dims
    global screen

    level1()
    for i in range(int(dims[0]/4), int(dims[0]*3/4)):
        screen.addch(i, int(dims[1]/6), "X")
        screen.addch(i, int(dims[1]*5/6), "X")

# def level3():


# level2()
# q = screen.getch()
