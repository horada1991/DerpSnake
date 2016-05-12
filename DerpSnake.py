import curses
import time
import random
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

#Starting parameters
FoodCoords = environment.Food()
Coords = [4, 13, 4, 12, 4, 11]
move_y = 0
move_x = 1
q = -1
ScoreMessage = "  Score:   "
screen.border()
screen.addstr(0, 5, ScoreMessage)

while q != ord("q"):
    q = screen.getch()
    screen.addch(FoodCoords[0], FoodCoords[1], "✪")
    EatCoords = piton.Eat(Coords, FoodCoords[0], FoodCoords[1])
    #If piton.Eat() doesn't return 0 (== snake eats and grow):
    if EatCoords != 0:
        screen.addch(Coords[-2], Coords[-1], "▪", curses.color_pair(1))
        FoodCoords = environment.Food()
        Coords = EatCoords
        Score += 1
        ScoreMessage = "  Score: " + str(Score) + " "
    #Handle Key push events
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
    #If piton.MovingCoords() return 0 (==wall or hit itself):
    if Coords == 0:
        with open("highscore.md", "r+") as f:
            highscore = int(f.read())
            if highscore < Score:
                f.seek(0)
                f.write(str(Score))
        screen.clear()
        environment.GameOver()
        message2 = 'You got ' + str(Score) + ' points'
        screen.addstr(int(dims[0]/2), int((dims[1]-len(message2))/2), message2)
        screen.refresh()
        while q not in [32, 10]:
            q = screen.getch()
        if q == 32:
            screen.clear()
            FoodCoords = environment.Food()
            Coords = [4, 13, 4, 12, 4, 11]
            move_y = 0
            move_x = 1
            Score = 0
            ScoreMessage = "  Score:   "
        else:
            q = ord('q')
    #Snake goes forward 1 step
    else:
        screen.clear()
        screen.addch(FoodCoords[0], FoodCoords[1], "✪", curses.color_pair(3))
        piton.PrintSnake(Coords)
        screen.border()
        screen.addstr(0, 5, ScoreMessage)
    time.sleep(0.15)
curses.endwin()
