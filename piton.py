#Moving Snake's parts' coordinates
import curses
screen = curses.initscr()
dims = screen.getmaxyx()

def MovingCoords(CoordList, y, x):
    global dims
    if y < dims[0]-1 and x < dims[1]-1 and (x not in CoordList[2:] and y not in CoordList[2:]):
        for element in range(len(CoordList)-1, 1, -1):
            CoordList[element] = CoordList[element-2]
        CoordList[0] = y
        CoordList[1] = x
        return(CoordList)
    else:
        return 0

#If eat food, than grow in length
def Eat(CoordList, food_y, food_x):
    if CoordList[0] == food_y and CoordList[1] == food_x:
        if CoordList[-2] == CoordList[-4]:
            CoordList.extend([CoordList[-2], CoordList[-1] * 2 - CoordList[-3]])
        elif CoordList[-1] == CoordList[-3]:
            CoordList.extend([CoordList[-2] * 2 - CoordList[-4], CoordList[-1]])
        return(CoordList)
    else:
        return 0

#del snake
def DelSnake(CoordList):
    global screen
    for i in range(0, len(CoordList) - 1, 2):
        screen.delch(CoordList[i], CoordList[i + 1])
        screen.addch(CoordList[i], CoordList[i + 1], " ")

#print snake on new coords
def PrintSnake(CoordList):
    global screen
    for i in range(0, len(CoordList)-1, 2):
        screen.addch(CoordList[i], CoordList[i+1], "@")



#TEST LINES
ist1 = [2, 1, 2, 2, 2, 3, 2, 4, 2, 5]
PrintSnake(List1)
screen.getch()
DelSnake(List1)
screen.getch()
curses.endwin()
