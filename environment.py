import curses
import random
screen = curses.initscr()
dims = screen.getmaxyx()


# map selecting
def start_game():
    global screen
    global dims
    speed = 0.1
    q = 0
    fullscreen = 'Please press F11 for better gaming experience'
    level = 'Choose a level!'
    level1 = 'Press 1 for level1'
    level2 = 'Press 2 for level2'
    level3 = 'Press 3 for level3'
    screen.addstr(int(dims[0]/2-3), int((dims[1]-len(fullscreen))/2), fullscreen)
    screen.addstr(int(dims[0]/2-1), int((dims[1]-len(level))/2), level)
    screen.addstr(int(dims[0]/2), int((dims[1]-len(level1))/2), level1)
    screen.addstr(int(dims[0]/2+1), int((dims[1]-len(level2))/2), level2)
    screen.addstr(int(dims[0]/2+2), int((dims[1]-len(level3))/2), level3)
    while q not in [49, 50, 51]:
        q = screen.getch()
    if q == 49:
        return(1, speed)
    elif q == 50:
        return(2, speed)
    elif q == 51:
        return(3, speed)


# food placement during the game
def food(n, food_coords, poison_food_coords, hp_food_coords):
    global screen
    global dims
    food_coords_local = []
    for food in range(3):
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
        food_coords_local.extend([y, x])
    if n == 2:
        poison_food_coords = food_coords_local[2:4]
    elif n == 3:
        hp_food_coords = food_coords_local[-2:]
    else:
        food_coords = food_coords_local[:2]
    return(food_coords, poison_food_coords, hp_food_coords)


# initial food placement
def start_food():
    global screen
    global dims
    food_coords = []
    for food in range(3):
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
        food_coords.extend([y, x])
    poison_food_coords = food_coords[2:4]
    hp_food_coords = food_coords[-2:]
    food_coords = food_coords[:2]
    return(food_coords, poison_food_coords, hp_food_coords)


# Game ending message
def game_over(level):
    global screen
    global dims
    message1 = 'GAME OVER'
    message3 = 'Press Space to play again'
    message4 = 'Press Enter to quit'
    with open("highscore.md", "r") as f:
        highscore = f.readlines()
        message5 = "Highscore: " + highscore[int(level) - 1]
    screen.addstr(int(dims[0]/2-1), int((dims[1]-len(message1))/2), message1)
    screen.addstr(int(dims[0]/2+2), int((dims[1]-len(message3))/2), message3)
    screen.addstr(int(dims[0]/2+3), int((dims[1]-len(message4))/2), message4)
    screen.addstr(int(dims[0]/2+1), int((dims[1]-len(message5))/2), message5)
