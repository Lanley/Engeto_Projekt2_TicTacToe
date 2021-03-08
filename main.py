# Author: Pavel Baranek

def welcome_phrase():
    welcome = "Welcome in the game of TicTacToe!!!"
    welcome1 = welcome.center(75)
    print(len(welcome1) * "*")
    print(welcome1)
    print(len(welcome1) * "*")


def show_rules():
    rules = """

                        THE RULES OF THE GAME ARE:
    Two players are putting the symbols of "X" and "O" on the 3x3 game plan.
    To win, one of the players have to connect the line of 3 symbols in a row.
    First player who connects the line wins. 
    (Player "X" starts the game). 

                        THE GAME MAP GOES LIKE THIS:  
                                - 7|8|9 -
                                - 4|5|6 -
                                - 1|2|3 - 

    """
    print(rules)
    starter = "--> LET THE GAME BEGIN <--"
    starter1 = starter.center(75)
    print(len(starter1) * "*")
    print(starter1)
    print(len(starter1) * "*")


def game_plan(value):
    print("\n")
    print("\t     |     |")
    print(f"\t  {value[6]}  |  {value[7]}  |  {value[8]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {value[3]}  |  {value[4]}  |  {value[5]}")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print(f"\t  {value[0]}  |  {value[1]}  |  {value[2]}")
    print("\t     |     |")
    print("\n")


win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (6, 4, 2), (8, 4, 0))



def empty_check(value, chosen):
    if value[chosen] == " ":
      return True

def update_(value, player, chosen):
    value[chosen] = player

def win_check(value, player):
    for a, b, c in win:
        if player == value[a] and player == value[b] and player == value[c]:
            return True
    else:
        return False


def tie_check(value):
    if " " not in value:
        return True


def player_input(player):
    while True:
        print(f"Player {player} |", end = " ")
        choice = input("Chosen place on game plan: ")
        if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            choice1 = int(choice)
            return choice1 - 1
        elif choice is not int:
            print("Error! Choose number between 1-9!!!")
            continue
        else:
            print("Error! Choose number between 1-9!!!")
            continue


def play_game():
    game = True
    players = ["X", "O"]

    value = [" " for i in range(9)]


    welcome_phrase()
    show_rules()
    game_plan(value)

    while game == True:

        for player in players:

            while True:
                chosen_place = player_input(player)
                if not empty_check(value, chosen_place):
                    print("Choose an empty spot please!!!")
                    continue
                break

            update_(value, player, chosen_place)

            game_plan(value)

            if win_check(value, player) == True:
                gratulation = f"Congratulations!!! Player {player} wins the game!"
                gratulation1 = gratulation.center(65)
                print(len(gratulation1) * "*")
                print(gratulation1)
                print(len(gratulation1) * "*")
                game = False
                break

            if tie_check(value) == True:
                print("It's a TIE, nobody wins! :( ")
                game = False
                break


if __name__ == "__main__":
    play_game()

