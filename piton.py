import curses
screen = curses.initscr()
dims = screen.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


# Moving Snake's parts' coordinates
def moving_coords(coord_list, y, x):
    global dims
    for element in range(len(coord_list)-1, 1, -1):
        coord_list[element] = coord_list[element-2]
    coord_list[0] = y
    coord_list[1] = x
    return(coord_list)


# If eat food, then grow in length
def eat(coord_list, food_coords, poison_food_coords, hp_food_coords):
    if coord_list[0] == food_coords[0] and coord_list[1] == food_coords[1]:
        if coord_list[-2] == coord_list[-4]:
            coord_list.extend([coord_list[-2], coord_list[-1] * 2 - coord_list[-3]])
        elif coord_list[-1] == coord_list[-3]:
            coord_list.extend([coord_list[-2] * 2 - coord_list[-4],
                              coord_list[-1]])
        return(coord_list)
    if coord_list[0] == poison_food_coords[0] and coord_list[1] == poison_food_coords[1]:
        return(2)
    if coord_list[0] == hp_food_coords[0] and coord_list[1] == hp_food_coords[1]:
        return(3)
    else:
        return(0)


# print snake on new coords
def print_snake(coord_list):
    global screen
    for i in range(0, len(coord_list)-1, 2):
        screen.addch(coord_list[i], coord_list[i+1], "O", curses.color_pair(1))
    screen.addch(coord_list[0], coord_list[1], "@", curses.color_pair(2))


def speed_raise(score, speed):
    if score % 5 == 0:
        speed -= 0.005
    return speed
