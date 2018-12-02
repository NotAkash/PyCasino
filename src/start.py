#Import Root Files
while True:                         #This is used in case start.py is ran locally
    try:                            #and not ran from casino.py
        from src.play import *
    except ModuleNotFoundError:
        from play import *
        break
    else:
        break

#Start Up Game (Moved To Seperate File To Keep usr() updated
    
def start_game():
    while True:  # Keep repeating until user is logged in
        try:
            print("Welcome To The Casino")
            user = input("Are You An 'Existing' User Or A 'New' User?: ")
        except ValueError:  # Error Hashes
            print("No Value Entered")                          
            continue
        except KeyboardInterrupt:
            print("Force Exiting Game.", end='')
            print(".", end='')
            print(".", end='')
            exit()
        if (user.lower() != "existing" and user.lower() != "new"):  # Repeat till user answer is Valid
            print("Please Try Again")
            continue
        elif (user.lower() == "existing"):  # If existing
            while True:
                try:
                    name = input("What Is Your Name: ")  # Get User-Name

                except KeyboardInterrupt:
                    print("Force Exiting Game.", end='')
                    print(".", end='')
                    print(".", end='')
                    exit()
                if name == '':
                    print("Invalid Value")
                    continue
                else:
                    break
            if (str(player_cont(name))=='False'): #If Balance Is 'False'
                print("User Does Not Exist, Try Again")
                continue  # Else, Repeat Till Validated
            elif (player_cont(name) > 0):  # Unless False Is Returned
                print(player_cont(name))
                print("Welcome Back", name, "Current Balance: ", player_cont(name))
                money = player_cont(name)  # Show User Value
                break
            else:
                print("User Does Not Exist, Try Again")
                continue  # Else, Repeat Till Validated
        elif (user.lower() == "new"):  # If New,
            print("Welcome To The Casino!")
            while True:
                try:
                    name = input("Welcome! What Is Your Name?: ")  # Get User-Name
                except KeyboardInterrupt:
                    print("Force Exiting Game.", end='')
                    print(".", end='')
                    print(".", end='')
                    exit()
                if name == '':
                    print("Invalid Value, Try Again")
                    continue
                else:
                    break
            if (player_init(name) != False):  # Initialise Name Unless False Returned
                print("Welcome!", name, "Starting Balance: ", player_cont(name))
                money = player_cont(name)  # Get Account Balance
                break
            else:
                print("User Exists, Try Again")
                continue
    return(str(name))
