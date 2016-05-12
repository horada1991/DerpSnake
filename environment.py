import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()

def Food():
    global screen
    global dims
    y1 = 1
    y2 = dims[0]
    x1 = 1
    x2 = dims[1]
    y = random.randrange(y1, y2)
    x = random.randrange(x1, x2)
    FoodCoords = [y, x]
    return(FoodCoords)

"""screen.addstr(0, 5, "   Score:   ")"""

def GameOver():
    global screen
    global dims
    screen.border()
    message1 = 'GAME OVER'
    message3 = 'Press Space to play again'
    message4 = 'Press Enter to quit'
    screen.addstr(int(dims[0]/2-1), int((dims[1]-len(message1))/2), message1)
    screen.addstr(int(dims[0]/2+1), int((dims[1]-len(message3))/2), message3)
    screen.addstr(int(dims[0]/2+2), int((dims[1]-len(message4))/2), message4)


"""Food()
>>>>>>> 63578988eaf789c8345c841efe21eb0c970fcaa8
screen.getch()
curses.endwin()"""
