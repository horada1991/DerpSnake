import curses
screen = curses.initscr()
dims = screen.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

#Moving Snake's parts' coordinates
def MovingCoords(CoordList, y, x):
    global dims
    if y < dims[0] and x < dims[1] and y > 0 and x > 0:
        for i in range(2, len(CoordList)-1, 2):
            if CoordList[i] == y and CoordList[i+1] == x:
                return 0
        for element in range(len(CoordList)-1, 1, -1):
            CoordList[element] = CoordList[element-2]
        CoordList[0] = y
        CoordList[1] = x
        return(CoordList)
    else:
        return 0

#If eat food, then grow in length
def Eat(CoordList, food_y, food_x):
    if CoordList[0] == food_y and CoordList[1] == food_x:
        if CoordList[-2] == CoordList[-4]:
            CoordList.extend([CoordList[-2], CoordList[-1] * 2 - CoordList[-3]])
        elif CoordList[-1] == CoordList[-3]:
            CoordList.extend([CoordList[-2] * 2 - CoordList[-4], CoordList[-1]])
        return(CoordList)
    else:
        return 0

#print snake on new coords
def PrintSnake(CoordList):
    global screen
    for i in range(0, len(CoordList)-1, 2):
        screen.addch(CoordList[i], CoordList[i+1], "▪", curses.color_pair(1))
    screen.addch(CoordList[0], CoordList[1], "▪", curses.color_pair(2))
