import curses
import time
import random
import os
import piton
import environment
import maps

curses.noecho()
curses.curs_set(0)
screen = curses.initscr()
screen.nodelay(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
screen.keypad(1)
dims = screen.getmaxyx()
score = 0
hp = 3


# Starting parameters
food_coords, poison_food_coords, hp_food_coords = environment.start_food()
coords = [4, 13, 4, 12, 4, 11]
move_y = 0
move_x = 1
q = -1
i = 0
random_food_replace_time = random.randrange(50, 91)
score_message = "  score: " + str(score) + " "
life_message = "  life: " + str(hp) + " "
screen.border()
screen.addstr(0, 5, score_message)
screen.addstr(0, dims[1]-15, life_message)


def place_food(food_coords, poison_food_coords, hp_food_coords):
    global screen

    screen.addch(food_coords[0], food_coords[1], "$", curses.color_pair(1))
    screen.addch(poison_food_coords[0], poison_food_coords[1], "☢", curses.color_pair(3))
    screen.addch(hp_food_coords[0], hp_food_coords[1], "♥", curses.color_pair(2))


def get_level():
    level, speed = environment.start_game()
    if level == 1:
        return("".lower, level, speed)
    elif level == 2:
        return(maps.level2, level, speed)
    elif level == 3:
        return(maps.level3, level, speed)

map_layout, level, speed = get_level()


while q != ord("q"):
    q = screen.getch()
    # random timer for spec foods replacement
    i += 1
    if i > random_food_replace_time:
        food_coords, poison_food_coords, hp_food_coords = \
            environment.food(2, food_coords, poison_food_coords, hp_food_coords)
        food_coords, poison_food_coords, hp_food_coords = \
            environment.food(3, food_coords, poison_food_coords, hp_food_coords)
        i = 0
        random_food_replace_time = random.randrange(50, 91)
    place_food(food_coords, poison_food_coords, hp_food_coords)
    eat_coords = piton.eat(coords, food_coords, poison_food_coords, hp_food_coords)

    # If piton.eat() doesn't returns 0, 2, 3 (== snake eats and grow):
    if eat_coords not in [0, 2, 3]:
        screen.addch(coords[-2], coords[-1], "O", curses.color_pair(1))
        food_coords, poison_food_coords, hp_food_coords = \
            environment.food(1, food_coords, poison_food_coords, hp_food_coords)
        coords = eat_coords
        score += 1
        speed = piton.speed_raise(score, speed)
        score_message = "  score: " + str(score) + " "

    # elIf snake eat other kind of foods:
    elif eat_coords == 2:
        hp -= 1
        life_message = "  life: " + str(hp) + " "
        food_coords, poison_food_coords, hp_food_coords = \
            environment.food(2, food_coords, poison_food_coords, hp_food_coords)
    elif eat_coords == 3:
        if hp < 3:
            hp += 1
        life_message = "  life: " + str(hp) + " "
        food_coords, poison_food_coords, hp_food_coords = \
            environment.food(3, food_coords, poison_food_coords, hp_food_coords)

    # Handle Key push events
    if q == curses.KEY_UP and move_y != 1:
        move_y, move_x = -1, 0
    elif q == curses.KEY_DOWN and move_y != -1:
        move_y, move_x = 1, 0
    elif q == curses.KEY_LEFT and move_x != 1:
        move_y, move_x = 0, -1
    elif q == curses.KEY_RIGHT and move_x != -1:
        move_y, move_x = 0, 1
    y_head = coords[0] + move_y
    x_head = coords[1] + move_x
    coords = piton.moving_coords(coords, y_head, x_head)

    # If There's the wall in (coords[0] and coords[1]):
    if ((screen.inch(coords[0], coords[1]) != ord(" ")) and
       coords[:2] != food_coords and
       coords[:2] != hp_food_coords and
       coords[:2] != poison_food_coords) or hp == 0:
        try:
            with open("highscore.md", "r+") as f:
                highscore = f.readlines()
                if int(highscore[int(level) - 1]) < score:
                    highscore[int(level) - 1] = str(score) + "\n"
                f.seek(0)
                for line in highscore:
                    f.write(line)
        except FileNotFoundError:
            with open("highscore.md", "w") as f:
                    f.write(str(score) + "\n" + str(score) + "\n" +
                            str(score) + "\n")
        screen.clear()
        environment.game_over(level)
        message2 = 'You got ' + str(score) + ' points'
        screen.addstr(int(dims[0]/2), int((dims[1]-len(message2))/2), message2)
        screen.border()
        screen.refresh()
        while q not in [32, 10]:
            q = screen.getch()

        # Start new game:
        if q == 32:
            screen.clear()
            screen.border()
            map_layout, level, speed = get_level()
            map_layout()
            screen.clear()
            food_coords, poison_food_coords, hp_food_coords = environment.start_food()
            coords = [4, 13, 4, 12, 4, 11]
            move_y = 0
            move_x = 1
            score = 0
            hp = 3
            score_message = "  score: " + str(score) + " "
            life_message = "  life: " + str(hp) + " "
            speed = 0.08
        else:
            q = ord('q')

    # Snake goes forward 1 step
    else:
        screen.clear()
        place_food(food_coords, poison_food_coords, hp_food_coords)
        piton.print_snake(coords)
        map_layout()
        screen.border()
        screen.addstr(0, 5, score_message)
        screen.addstr(0, dims[1]-15, life_message)
    time.sleep(speed)
curses.endwin()
