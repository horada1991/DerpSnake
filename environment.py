import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()

def Food():
    global screen
    global dims
    foodmade = False
    while not foodmade:
        y1 = 2
        y2 = dims[0]-1
        x1 = 2
        x2 = dims[1]-1
        y = random.randrange(y1, y2)
        x = random.randrange(x1, x2)
        if screen.inch(y, x) == ord(" "):
            foodmade = True
    FoodCoords = [y, x]
    return(FoodCoords)

def GameOver():
    global screen
    global dims
    message1 = 'GAME OVER'
    message3 = 'Press Space to play again'
    message4 = 'Press Enter to quit'
    with open("highscore.md", "r") as f:
        message5 ="Highscore: " + f.read()
    screen.addstr(int(dims[0]/2-1), int((dims[1]-len(message1))/2), message1)
    screen.addstr(int(dims[0]/2+2), int((dims[1]-len(message3))/2), message3)
    screen.addstr(int(dims[0]/2+3), int((dims[1]-len(message4))/2), message4)
    screen.addstr(int(dims[0]/2+1), int((dims[1]-len(message5))/2), message5)
