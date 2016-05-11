import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()

def Food():
    global screen
    global dims
    y1 = 1
    y2 = dims[0] - 1
    x1 = 1
    x2 = dims[1] - 1
    y = random.randrange(y1, y2)
    x = random.randrange(x1, x2)
    screen.addch(y, x, '#')
    FoodCoords = [y, x]
    return(FoodCoords)

"""screen.addstr(0, 5, "   Score:   ")"""

def GameOver():
    global screen
    global dims
    screen.border()
    screen.addstr(0, 5, "   Score:   ")
    screen.addstr(int(dims[0]/2), int(dims[1]/2-8), " G A M E   O V E R ")


"""Food()
>>>>>>> 63578988eaf789c8345c841efe21eb0c970fcaa8
screen.getch()
curses.endwin()"""
