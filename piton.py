#Moving Snake's parts' coordinates
def MovingCoords(CoordList, y, x, edge_y, edge_x):
    if y < edge_y and x < edge_x:
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
            CoordList.extend([CoordList[-2],
              CoordList[-1] + (CoordList[-1] - CoordList[-3])])
        elif CoordList[-1] == CoordList[-3]:
            CoordList.extend(CoordList[-2] + (CoordList[-2] - CoordList[-4]),
              [CoordList[-1]])
    return(CoordList)



#TEST LINES
"""List1 = [x for x in range(1, 101)]
print(List1)
ListShift(List1, 200, 200)
print(List1)"""
