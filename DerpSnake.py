import curses
import time
import random
import os
import piton
import environment

curses.noecho()
curses.curs_set(0)
screen = curses.initscr()
screen.nodelay(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
screen.keypad(1)
dims = screen.getmaxyx()
Score = 0

# Starting parameters
food_coords = environment.food()
coords = [4, 13, 4, 12, 4, 11]
move_y = 0
move_x = 1
q = -1
score_message = "  Score:   "
screen.border()
screen.addstr(0, 5, score_message)

level = environment.start_game()
if level == 1:
    speed = 0.12
elif level == 2:
    speed = 0.07
elif level == 3:
    speed = 0.03

while q != ord("q"):
    q = screen.getch()
    screen.addch(food_coords[0], food_coords[1], "$")
    eat_coords = piton.eat(coords, food_coords[0], food_coords[1])
    # If piton.eat() doesn't returns 0 (== snake eats and grow):
    if eat_coords != 0:
        screen.addch(coords[-2], coords[-1], "O", curses.color_pair(1))
        food_coords = environment.food()
        coords = eat_coords
        Score += 1
        score_message = "  Score: " + str(Score) + " "
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
    if (screen.inch(coords[0], coords[1]) != ord(" ")) and \
            (screen.inch(coords[0], coords[1]) != ord("$")):
        try:
            with open("highscore.md", "r+") as f:
                highscore = f.readlines()
                if int(highscore[int(level) - 1]) < Score:
                    highscore[int(level) - 1] = str(Score) + "\n"
                f.seek(0)
                for line in highscore:
                    f.write(line)
        except FileNotFoundError:
            with open("highscore.md", "w") as f:
                    f.write(str(Score) + "\n" + str(Score) + "\n" +
                            str(Score) + "\n")
        screen.clear()
        environment.game_over(level)
        message2 = 'You got ' + str(Score) + ' points'
        screen.addstr(int(dims[0]/2), int((dims[1]-len(message2))/2), message2)
        screen.border()
        screen.refresh()
        while q not in [32, 10]:
            q = screen.getch()
        # Start new game:
        if q == 32:
            screen.clear()
            screen.border()
            level = environment.start_game()
            if level == 1:
                speed = 0.12
            elif level == 2:
                speed = 0.07
            elif level == 3:
                speed = 0.03
            screen.clear()
            food_coords = environment.food()
            coords = [4, 13, 4, 12, 4, 11]
            move_y = 0
            move_x = 1
            Score = 0
            score_message = "  Score:   "
        else:
            q = ord('q')
    # Snake goes forward 1 step
    else:
        screen.clear()
        screen.addch(food_coords[0], food_coords[1], "$", curses.color_pair(3))
        piton.print_snake(coords)
        screen.border()
        screen.addstr(0, 5, score_message)
    time.sleep(speed)
curses.endwin()
