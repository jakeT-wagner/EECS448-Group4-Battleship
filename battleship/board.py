#	Author: Umar Khan
#	Date: 2/14/2021
#   Start: 8:40 PM

from .constants import *
from .ship import *


class Board:
    def __init__(self, win, player0ships, player1ships):  # p0ships, p1ships
        # self.p0ships = p0ships
        # self.p1ships = p1ships
        self.grid_width = 500
        self.grid_height = 500  # buffer of 200 for the labels and gaps in between the two different grids
        self.win = win
        self.draw_background()
        ###could combine both of them into a single grid where you initialize say self.p0_hits_misses = [0,0,1,2, ....]
        ###where a 0 would be nothing has happened here, a 1 was a miss and a 2 was a hit. This would make for much
        ###easier printing
        ###there is also not one user as there is player 0 and player 1. So, you would be designating one of the players as
        ###an enemy which is fine, but seems to be more confusing. There will only be one board class
        # 0 = nothing, 1 = hit, 2 = miss
        self.p0_hit_misses = []
        self.player0ships = player0ships
        self.p1_hit_misses = []
        self.player1ships = player1ships

    def draw_background(self):
        self.win.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf',
                                32)  # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        text = font.render('Select the location you wish to hit', True, WHITE, RED)
        textRect = text.get_rect()
        # textRect.center = (300,50)
        textRect.center = ((WIDTH / 2) - 100, 50)
        self.win.blit(text, textRect)
        ###constants here with the padding, explained in draw_grid
        pygame.draw.rect(self.win, GRAY, (0, 100, 500, 500))
        pygame.draw.rect(self.win, GRAY, (700, 100, 500, 500))  # hardcoded of course
        self.draw_grid()

    def draw_grid(self):
        for i in range(10):
            ###Would it be possible to make constants here. I.e. WIDTH_PADDING = 200, HEIGHT_PADDING = 100
            ###I was also thinking it would be cool to have the grids like this:
            ###  _| 1 | 2 | 3 | 4 | ...
            ###  A|
            ###  B|
            ###  C|
            ###which would affect the padding but could also be accounted for with a constant where a box with label A would just be the
            ###same size as a normal box
            pygame.draw.line(self.win, WHITE, (0, HEIGHT - self.grid_height + i * SQUARE_SIZE),
                             (self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE), 3)
            pygame.draw.line(self.win, WHITE, (WIDTH - self.grid_width, HEIGHT - self.grid_height + i * SQUARE_SIZE),
                             (WIDTH, HEIGHT - self.grid_width + i * SQUARE_SIZE), 3)
            pygame.draw.line(self.win, WHITE, (0 + i * SQUARE_SIZE, HEIGHT - self.grid_height),
                             (0 + i * SQUARE_SIZE, HEIGHT), 3)
            pygame.draw.line(self.win, WHITE, (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT - self.grid_height),
                             (self.grid_width + 200 + i * SQUARE_SIZE, HEIGHT), 3)

    def draw(self, player):
        ###Basically I believe it shoudl go like this.
        ### draw_background()
        ###if player == 0:
        ###     print that players ships on the right hand grid.
        ###     for ship in self.player0ships:
        ###         ship.draw()
        ###     for loc in player0_hits_misses:
        ###         if loc == 1:# miss
        ###             draw small black circle in center of square
        ###         if loc == 2: # hit
        ###             draw small red circle in center of square(which will go over top of the ship if there is one there)
        ###else:
        ### do for player 2

        self.draw_background()

        if player == 0:
            # for ship in self.player0ships.ship:
            #     self.player0ships.ship.draw(self.win)
            self.player0ships.draw(self.win)
        else:
            # for ship in self.player1ships.ship:
            #     self.player0ships.ship.draw(self.win)
            self.player1ships.draw(self.win)

        for row, col, state in self.p0_hit_misses:
            # miss
            if state == 1:
                center_x = row * SQUARE_SIZE + (SQUARE_SIZE / 2)
                center_y = col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE + (SQUARE_SIZE / 2)
                pygame.draw.circle(self.win, BLACK, (center_x, center_y), SQUARE_SIZE / 2)
                # pygame.draw.rect(self.win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # hit
            elif state == 2:
                center_x = row * SQUARE_SIZE + (SQUARE_SIZE / 2)
                center_y = col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE + (SQUARE_SIZE / 2)
                pygame.draw.circle(self.win, RED, (center_x, center_y), SQUARE_SIZE / 2)
                # pygame.draw.rect(self.win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pass

        for row, col, state in self.p1_hit_misses:
            # miss
            if state == 1:
                center_x = row * SQUARE_SIZE + 700 + (SQUARE_SIZE / 2)
                center_y = col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE +  (SQUARE_SIZE / 2)
                pygame.draw.circle(self.win, BLACK, (center_x, center_y), SQUARE_SIZE / 2)
                # pygame.draw.rect(self.win, BLACK, (
                # row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # hit
            elif state == 2:
                center_x = row * SQUARE_SIZE + 700 + (SQUARE_SIZE / 2)
                center_y = col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE +  (SQUARE_SIZE / 2)
                pygame.draw.circle(self.win, RED, (center_x, center_y), SQUARE_SIZE / 2)
                # pygame.draw.rect(self.win, RED, (
                # row * SQUARE_SIZE, col * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pass

    ###the GAME class would be attempting a hit on a square row and col, but it would not know if there is a ship there. So it can not pass ship
    ### hit_ship(self, player, row, col)
    def hit_ship(self, player, row, col):
        ###first determine which player it is
        ###then you may have to loop through the ships and their locations
        ###if any of the ships contain a row,col == row and col that were passed.
        ###     Then grab that ship and do ship.hit(row,col)
        ###     mark a hit for that player in playerxhits_misses
        ###     return True
        ###else
        ###     mark a miss and return False

        if player == 0:
            for ship_row, ship_col, state in self.player1ships.ship:
                if ship_row == row and ship_col == col:
                    self.player0ships.mark_hit(row, col)
                    self.p0_hit_misses.append(tuple((row, col, 2)))
                    print(f'(PLAYER 0) Hit/Miss List: {self.p0_hit_misses}')
                    print(f'(PLAYER 0) Successful attack at: ({row}, {col})')
                    return
            self.p0_hit_misses.append(tuple((row, col, 1)))
            print(f'(PLAYER 0) Hit/Miss List: {self.p0_hit_misses}')
            print(f'(PLAYER 0) Missed attack at: ({row}, {col})')
        else:
            for ship_row, ship_col, state in self.player0ships.ship:
                if ship_row == row and ship_col == col:
                    self.player1ships.mark_hit(row, col)
                    self.p1_hit_misses.append(tuple((row, col, 2)))
                    print(f'(PLAYER 1) Hit/Miss List: {self.p1_hit_misses}')
                    print(f'(PLAYER 1) Successful attack at: ({row}, {col})')
                    return
            self.p1_hit_misses.append(tuple((row, col, 1)))
            print(f'(PLAYER 1) Hit/Miss List: {self.p1_hit_misses}')
            print(f'(PLAYER 1) Missed attack at: ({row}, {col})')

    def info(self):
        print(f'Player 0 ships: {self.player0ships.ship}')
        print(f'Player 0 hit/misses: {self.p0_hit_misses}')
        print(f'Player 1 ships: {self.player1ships.ship}')
        print(f'Player 1 hit/misses: {self.p1_hit_misses}')
