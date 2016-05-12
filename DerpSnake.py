import curses
import time
import random
import piton
import environment

curses.noecho()
curses.curs_set(0)
screen = curses.initscr()
screen.nodelay(1)
screen.keypad(1)
dims = screen.getmaxyx()

FoodCoords = environment.Food()
Coords = [4, 13, 4, 12, 4, 11]
move_y = 0
move_x = 1
q = -1
screen.border()

while q != ord("q"):
    q = screen.getch()
    screen.addch(FoodCoords[0], FoodCoords[1], "✪")
    food_y = FoodCoords[0]
    food_x = FoodCoords[1]
    EatCoords = piton.Eat(Coords, food_y, food_x)
    if EatCoords != 0:
        screen.addch(Coords[-2], Coords[-1], "▪")
        FoodCoords = environment.Food()
        Coords = EatCoords
    if q == curses.KEY_UP and move_y != 1:
        move_y, move_x = -1, 0
    elif q == curses.KEY_DOWN and move_y != -1:
        move_y, move_x = 1, 0
    elif q == curses.KEY_LEFT and move_x != 1:
        move_y, move_x = 0, -1
    elif q == curses.KEY_RIGHT and move_x != -1:
        move_y, move_x = 0, 1
    y_head = Coords[0] + move_y
    x_head = Coords[1] + move_x
    Coords = piton.MovingCoords(Coords, y_head, x_head)
    if Coords == 0:
        screen.clear()
        environment.GameOver()
        q = ord("q")
    else:
        screen.clear()
        screen.addch(FoodCoords[0], FoodCoords[1], "✪")
        piton.PrintSnake(Coords)
        screen.border()
    time.sleep(0.1)

screen.nodelay(0)
screen.getch()
curses.endwin()

""" Levels()
    Score()
    Move

"""
