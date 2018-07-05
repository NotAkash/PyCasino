# Casino Games

# Import Files
from src.games import *
from src.play import *
from src.start import *
print('---| PyCasino |  https://github.com/NotAkash/PyCasino ---|')
print('---| PyCasino | Build[0.5.7] | Dev: Akash 10C|        ---|')#fix  [Known Bugs=0]
print('---| PyCasino | Check README.md For Changelog|11/11/17---|')
print('---| PyCasino | Whats New: New Start File To Shorten Code On Main File|')
print('---| PyCasino | Bugs Fixed:Play file fixed (again), Changed Backend Database From .txt To .csv|')
fexit = 0 #force exit
# Start Up User Profile
name= start_game()
while True:
    try:
        fexit = 0
        input("Press 'ENTER' To Continue")
        menuitems = ['Account Balance', 'Slot Machine', 'Roulette', 'Blackjack', 'Change User', 'Quit']
        print("What Would You Like To Do?")
    except KeyboardInterrupt:
        fexit = 1
        print("\nForce Exiting Game.", end='')
        print(".", end='')
        print(".")
        exit()
    else:
        break


def to_cont(menu):
    while True:
        cgame = False
        try:
            cgame = input("Continue With Selected Option? 'YES'/'NO': ")
        except ValueError:  # Error Hashes
            print("Invalid Value, Insert Positive Integers Only")
            continue
        except KeyboardInterrupt:
            fexit = 1
            print("Force Exitting Game.", end='')
            print(".", end='')
            print(".")
            break
        if (cgame.upper() != "YES" and cgame.upper() != "NO"):
            print("'YES' or 'NO' only")
            continue
        else:
            break

    if cgame.upper() == "YES":
        return True
    else:
        return False


# This is the main part of the game
while True:
    choption = False
    try:
        noption = 1  # No Of Options Start At 1
        # List Of Items
        print("ACCOUNT NAME: " + name)
        for i in menuitems:
            print("Option", noption, "Is:", i)
            noption += 1  # Give Options With Option Codes (1,2,3 ETC)
        try:
            fexit = 0
            print("Options= '1' to '%s' " %len(menuitems))
            uoption = int(input("Option Number?: "))
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("Force Exitting Game.", end='')
            print(".", end='')
            print(".", end='')
            break
        for i in menuitems:
            if i == menuitems[uoption - 1]:
                print("Ok... Setting Up,", i)
                choption = True
                menu = i
                break
            else:
                continue
        if choption == False:
            print("Please Try Again")
            continue
        name = name
    except ValueError:
        print("Invalid Value Entered")
        continue
    else:
        while True:
            if menu.title() == 'Account Balance':
                print(balance(name), "Is Balance")

            if menu.title() == 'Slot Machine':
                while True:
                    if player_cont(name) == 0:
                        print("ERROR: NO BALANCE LEFT")
                        break
                    try:
                        gamble = int(input("How Much Would You Like To Bet?: "))
                    except ValueError:
                        print("Invalid Value Entered, Please Insert Positive Integers Only")
                        continue
                    except KeyboardInterrupt:
                        fexit = 1
                        print("Force Exitting Game.", end='')
                        print(".", end='')
                        print(".", end='')
                        break
                    if (gamble > 0 and gamble <= balance(name)):
                        pbal_update(name, slots(gamble))
                        break
                    else:
                        print("Gamble Can't Be Less Than 1 Or More Than,", player_cont(name))
                        continue

            if menu == 'Roulette':
                if player_cont(name) == 0:
                    print("ERROR: NO BALANCE LEFT")
                    break
                red = [1, 4, 7, 10, 13, 16, 19, 22]
                black = [2, 5, 8, 11, 14, 17, 20, 23]
                green = [3, 6, 9, 12, 15, 18, 21, 24]
                even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
                odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
                print(" Win By Getting The Number In Your Bet Pool ")
                print("|||Red  |||", red, "||| 33.3% Chance To Win")
                print("|||Black|||", black, "||| 33.3% Chance To Win")
                print("|||Green|||", green, "||| 33.3% Chance To Win")
                print("|||Winning From The Pools Above Results In A Reward Of 3 Times The Gamble")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                print("||| Odd||| ", odd, "||| 50% Chance To Win")
                print("|||Even|||", even, "||| 50% Chance To Win")
                print("Winning From The Pools Above Result In A Reward Of 2 Times The Gamble")
                while True:
                    try:
                        choice = input("Which Pool Would You Like To Choose From?: ")
                    except ValueError:
                        print("Invalid Choice, Try Again")
                        continue
                    except KeyboardInterrupt:
                        fexit = 1
                        print("Force Exitting Game.", end='')
                        print(".", end='')
                        print(".", end='')
                        break
                    if choice.capitalize() == 'Red' or choice.capitalize() == 'Black' or choice.capitalize() == 'Green' or choice.capitalize() == 'Even' or choice.capitalize() == 'Odd':
                        break
                    else:
                        print("Invalid Pool Selected, Please Try Again")
                        print("Valid Choices= 'Red' or 'Black' or 'Green' or 'Even' or 'Odd'")
                        continue
                if fexit == 1:
                    break
                while True:
                    try:
                        gamble = int(input("How Much Would You Like To Gamble?: "))
                    except ValueError:
                        print("Invalid Gamble, Try Again")
                        continue
                    except KeyboardInterrupt:
                        fexit = 1
                        print("Force Exitting Game.", end='')
                        print(".", end='')
                        print(".", end='')
                        break

                    if gamble != 0:
                        if (gamble > 0 and gamble <= balance(name)):
                            break
                        else:
                            print("Gamble Can't Be 0 Or More Than,", player_cont(name))
                            continue
                    if fexit == 1:
                        break
                if fexit != 1:
                    fexit = 0
                    pbal_update(name, roulette(choice, gamble))

            if menu == 'Blackjack':
                gamble = int(input("Inital Gamble: "))
                blackjack(gamble)
            if menu == 'Change User':
                name = usr()
            if menu == 'Quit':
                print("Exitting.", end='')
                print(".", end='')
                print(".", end='')
                print(".", end='')
                print(".")
                doexit()
            if fexit == 1:
                break
            if (to_cont(menu) == True):
                continue
            else:
                break
