#Moving Snake's parts' coordinates
def MovingCoords(List, y, x, edge_y, edge_x):
    if y < edge_y and x < edge_x:
        for element in range(len(List)-1, 1, -1):
            List[element] = List[element-2]
        List[0] = y
        List[1] = x
        return(List)
    else:
        return 0


#TEST LINES
"""List1 = [x for x in range(1, 101)]
print(List1)
ListShift(List1, 200, 200)
print(List1)"""
