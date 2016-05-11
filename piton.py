#Moving Snake's parts' coordinates
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







#TEST LINES
"""List1 = [1,2,3,4,5,6,2,3,3,3]
print(List1)
print("\n", Eat(List1, 1, 2))"""
