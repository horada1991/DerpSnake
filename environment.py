import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()

def Food():
    global screen
    global dims
    y1 = 0
    y2 = dims[0] - 1
    x1 = 0
    x2 = dims[1] - 1
    y = random.randrange(y1, y2)
    x = random.randrange(x1, x2)
    screen.addch(y, x, '#')
    FoodCoords = [y, x]
    return(FoodCoords)

"""screen.addstr(0, 5, "   Score:   ")"""



"""Food()
screen.getch()
curses.endwin()"""
