#Moving Snake's parts' coordinates
def ListShift(List, y, x):
    for element in range(len(List)-1, 1, -1):
        List[element] = List[element-2]
    List[0] = y
    List[1] = x
    return(List)



#TEST LINES
"""List1 = [x for x in range(1, 101)]
print(List1)
ListShift(List1, 200, 200)
print(List1)"""
