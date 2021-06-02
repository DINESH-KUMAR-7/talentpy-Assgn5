"""
Board Class:
    1. Constructor which takes positions_of_snakes (dictionary where head is key, tail is value),
    positions_of_ladders (dictionary where key is start of ladder, value is end of ladder)
    2. Method is_snake(position) -> Return True if it is snake box else return False.
    3. Method is_ladder(position) -> Return True if it is ladder box else return False.
    4. Method climb_ladder(ladder_start_box) -> Return the respective index to jump using
    position_of_ladders.
    5. Method go_down(snake_position) -> Return the respective index to go down using
    positions_of_snakes.
    6.
Player Class:
    1. Constructor which takes name of player, initialise current position as 1 (as player need to
    start from 1)
    2. roll_dice() method, which will roll dice, on rolling dice it should return random number
    between 1 to 6.
Game Class:
    1. Create a method start_game() inside which create 2 player objects (say player_1 and
    player_2) and board class.
    2. Put a while loop and check whether any of the player reaches the box 100, if not continue
    the loop, roll dice for player_1, player_2, player_1, player_2 and so on….(check for snake
    and ladders using Board class and perform ups and downs accordingly) Until any one
    player reaches the box 100. If reached 100, print the winner declaration. Saying “Player
    <Player name> wins the game!”.
    3. Note that: If player is in 96th box, and his roll gives 5 then 96+5 = 101 (Invalid) at this time,
    you should not declare him as winner! He has to exactly to go to 100th box to become
    winner.
"""
import random
import time

class Board:
    lad_start=0
    snake_start =0
    def __init__(self,positions_of_snakes,positions_of_ladders):
        self.positions_of_ladders = positions_of_ladders
        self.positions_of_snakes = positions_of_snakes

    def is_snake(self,position):
        for _ in self.positions_of_snakes:
            if(position==_):
                return True
            else:
                return False

    def is_ladder(self,position):
        for _ in self.positions_of_ladders:
            if(position==_):
                return True
            else:
                return False

    def climb_ladder(self,ladder_start_box):
        for _,j in self.positions_of_ladders.items():
            if ladder_start_box==_:
                return j
            else:
                return ladder_start_box

    def go_down(self,snake_position):
        for _,j in self.positions_of_snakes.items():
            if snake_position==_:
                return j
            else:
                return snake_position


class Player:
    def __init__(self,name_of_player,player_position=1):
        self.name_of_player = name_of_player
        self.player_position = player_position
        self.player_position = 1

    def roll_dice(self):
        return random.randint(1,6)

class Game:
    def start_game(self):
        SLEEP_TIME = 1
        CS = '\x1b[2;30;44m'
        CE = '\x1b[0m'
        ladder_color = '\x1b[1;34;40'
        snake_color = '\x1b[1;31;40'
        rules ="""
        1. Initally both the players are at starting position is 1.
        2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
        3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
        4. The first player to get to the FINAL position is the winner.
        """

        player_1 = Player("Hari")
        player_2 = Player("Ganesh")
        positions_of_snakes = {5: 1, 35 : 3}
        positions_of_ladders = {7 : 81, 41 : 53}
        board = Board(positions_of_snakes, positions_of_ladders)
        print("\x1b[6;30;42m        Snake & Ladder          \x1b[0m","\n")
        print("\x1b[2;34;40m        Rules  \x1b[0m")
        print("\x1b[1;32;40m"+rules+"\x1b[0m")
        print("\t","\x1b[1;30;47m"+player_1.name_of_player,"Vs",player_2.name_of_player+"\x1b[0m","\n")

        time.sleep(SLEEP_TIME)
        while(player_1.player_position != 100 or player_2.player_position != 100):

            val1 = player_1.roll_dice()
            val2 = player_2.roll_dice()

            if player_1.player_position == 95 and val1>5:
                continue
            elif player_1.player_position == 96 and val1>4:
                continue
            elif player_1.player_position == 97 and val1>3:
                continue
            elif player_1.player_position == 98 and val1>2:
                continue
            elif player_1.player_position == 99 and val1>1:
                continue

            if player_2.player_position == 95 and val2>5:
                continue
            elif player_2.player_position == 96 and val2>4:
                continue
            elif player_2.player_position == 97 and val2>3:
                continue
            elif player_2.player_position == 98 and val2>2:
                continue
            elif player_2.player_position == 99 and val2>1:
                continue


            player_1.player_position += val1
            print(player_1.name_of_player,"Rolled dice",val1,"moved",player_1.player_position,"\n")
            time.sleep(SLEEP_TIME)
            player_2.player_position += val2
            print(player_2.name_of_player,"Rolled dice",val2,"moved",player_2.player_position,"\n")


            if board.is_ladder(player_1.player_position) == True:
                ladder = board.climb_ladder(player_1.player_position)
                player_1.player_position = ladder
                print(player_1.name_of_player,"on the ladder",player_1.player_position)


            elif board.is_snake(player_1.player_position) == True:
                snake = board.go_down(player_1.player_position)
                player_1.player_position = snake
                print("snake got",player_1.name_of_player,"moved down to",player_1.player_position)

            if board.is_ladder(player_2.player_position) == True:
                ladder = board.climb_ladder(player_2.player_position)
                player_2.player_position = ladder
                print(player_2.name_of_player,"on the ladder","going up..",player_2.player_position)

            elif board.is_snake(player_2.player_position) == True:
                snake = board.go_down(player_2.player_position)
                player_2.player_position = snake
                print("snake got",player_2.name_of_player,"moved down to",player_2.player_position)


            if player_1.player_position == 100:
                print("\x1b[1;31;40m *\x1b[0m","\x1b[1;34;40m *\x1b[0m","\x1b[1;32;40m *\x1b[0m",CS+player_1.name_of_player,"Winner"+CE,"\x1b[1;31;40m *\x1b[0m","\x1b[1;34;40m *\x1b[0m","\x1b[1;32;40m *\x1b[0m")
                break
            elif player_2.player_position == 100:
                print("\x1b[1;31;40m *\x1b[0m","\x1b[1;34;40m *\x1b[0m","\x1b[1;32;40m *\x1b[0m",CS+player_2.name_of_player,CS+"Winner"+CE,"\x1b[1;31;40m *\x1b[0m","\x1b[1;34;40m *\x1b[0m","\x1b[1;32;40m *\x1b[0m")
                break

dice_game = Game()
dice_game.start_game()


"""
Output:
/GitHub/talentpy-Assgn5/snake_ladder.py
        Snake & Ladder

        Rules

        1. Initally both the players are at starting position is 1.
        2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
        3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
        4. The first player to get to the FINAL position is the winner.

         Hari Vs Ganesh

Hari Rolled dice 4 moved 5

Ganesh Rolled dice 3 moved 4

snake got Hari moved down to 1
Hari Rolled dice 4 moved 5

Ganesh Rolled dice 5 moved 9

snake got Hari moved down to 1
Hari Rolled dice 6 moved 7

Ganesh Rolled dice 1 moved 10

Hari on the ladder 81
Hari Rolled dice 6 moved 87

Ganesh Rolled dice 1 moved 11

Hari Rolled dice 3 moved 90

Ganesh Rolled dice 4 moved 15

Hari Rolled dice 5 moved 95

Ganesh Rolled dice 4 moved 19

Hari Rolled dice 2 moved 97

Ganesh Rolled dice 1 moved 20

Hari Rolled dice 2 moved 99

Ganesh Rolled dice 1 moved 21

Hari Rolled dice 1 moved 100

Ganesh Rolled dice 5 moved 26

 *  *  * Hari Winner  *  *  *
"""