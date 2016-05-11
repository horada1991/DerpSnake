#Moving Snake's parts' coordinates
import curses
screen = curses.initscr()


def MovingCoords(CoordList, y, x, edge_y, edge_x):
    if y < edge_y and x < edge_x and (x not in CoordList[2:] and y not in CoordList[2:]):
        for element in range(len(CoordList)-1, 1, -1):
            CoordList[element] = CoordList[element-2]
        CoordList[0] = y
        CoordList[1] = x
        return(CoordList)
    else:
        return 0


def Eat(CoordList, food_y, food_x):
    if CoordList[0] == food_y and CoordList[1] == food_x:
        if CoordList[-2] == CoordList[-4]:
            CoordList.extend([CoordList[-2], CoordList[-1] * 2 - CoordList[-3]])
        elif CoordList[-1] == CoordList[-3]:
            CoordList.extend([CoordList[-2] * 2 - CoordList[-4], CoordList[-1]])
        return(CoordList)
    else:
        return 0

def DelSnake(CoordList):
    global screen
    for i in range(0, len(CoordList) - 1):
        screen.delch(CoordList[0], CoordList[1])

def PrintSnake(CoordList):
    global screen
    for i in range(0, len(CoordList)-1, 2):
        screen.addch(CoordList[i], CoordList[i+1], "@")

#TEST LINES
"""List1 = [2, 1, 2, 2, 2, 3, 2, 4, 2, 5]
PrintSnake(List1)
screen.getch()
DelSnake(List1)
screen.getch()
curses.endwin()"""
