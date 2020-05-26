# import everything from the microbit module
from microbit import *

NORTH = [0, -1]
SOUTH = [0, 1]
EAST = [1, 0]
WEST = [-1, 0]
DIRECTIONS = [EAST, NORTH, WEST, SOUTH]
SPEED = 1
KAREL_EAST = Image("00999:09009:99009:09990:00900")
KAREL_NORTH = Image("99900:90090:90099:09990:00900")
KAREL_WEST = Image("00900:09990:90099:90090:99900")
KAREL_SOUTH = Image("00900:09990:99009:09009:00999")
KAREL_DIRS = [KAREL_EAST, KAREL_NORTH, KAREL_WEST, KAREL_SOUTH]


class Karel:

    def __init__(self):
        self.x = 0
        self.y = 4
        self.facing = EAST
        self.beepers = 26
        display.show(KAREL_EAST)
        sleep(1000)
        display.clear()
        display.set_pixel(self.x, self.y, 9)

    def turn_left(self):
        display.clear()
        i = DIRECTIONS.index(self.facing)
        display.show(KAREL_DIRS[i])
        sleep(500)
        display.clear()
        i = (i + 1) % 4
        display.show(KAREL_DIRS[i])
        sleep(500)
        display.clear()
        self.facing = DIRECTIONS[i]
        display.set_pixel(self.x, self.y, 9)

    def move(self):
        moved_from = [self.x, self.y]

        self.x += self.facing[0]
        if self.x > 4 or self.x < 0:
            raise Exception("Karel Out of Bounds")
        self.y += self.facing[1]
        if self.y > 4 or self.y < 0:
            raise Exception("Karel Out of Bounds")

        display.set_pixel(moved_from[0], moved_from[1], 0)
        display.set_pixel(self.x, self.y, 9)

        sleep(1000 / SPEED)

    def place_beeper(self):
        beeper = Beeper(self.x, self.y)

    def pick_beeper(self):
        if display.get_pixel(self.x, self.y) == 5:
            display.set_pixel(self.x, self.y, 0)
        else:
            raise Exception("No beepers present")


class Beeper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        display.set_pixel(self.x, self.y, 5)


def main():
    karel = Karel()

    def turn_right():
        karel.turn_left()
        karel.turn_left()
        karel.turn_left()

    karel.move()
    karel.move()
    karel.turn_left()
    karel.move()
    karel.move()
    turn_right()
    karel.move()
    karel.move()
    karel.move()


if __name__ == "__main__":
    main()
