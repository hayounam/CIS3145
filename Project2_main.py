import csv
from db import db
import datetime

global hits
global at_bats
global names
global positions_list

class Baseball:
    def __init__(files):
        files.data_driver = db()
        files.database = files.data_driver.load_from_file("players.csv")
        files.amount = len(files.database)

        global at_bats
        global hits
        for i in range(files.get_amount()):
            at_bats = int(files.database[i][2])
            hits = int(files.database[i][3])
            files.database[i].append(files.get_AVG())

    def position_list(files):
        """
        Use tuple
        """
        global positions_list
        positions_list = ("C", "1B", "2B", "3B", "SS", "LF", "C", "RF", "P")
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        positions_list[0], positions_list[1], positions_list[2], positions_list[3], positions_list[4],
        positions_list[5], positions_list[6], positions_list[7], positions_list[8])

    def menu(files):
        print("\nMENU OPTIONS")
        print("1 - Display Lineup")
        print("2 - Add Player")
        print("3 - Remove Player")
        print("4 - Move Player")
        print("5 - Edit player position")
        print("6 - Edit Player stats")
        print("7 - Exit Program\n")
        print("Positions")
        print(files.position_list())
        print("================================================================\n")
        print("Menu option: ", end="")

    def get_name(files):
        global names
        names = str(input("Enter Name: "))
        return names

    def get_POS(files):
        while (True):
            positions = input("Position: ").strip()
            positions = positions.upper()
            if positions not in positions_list:
                print("ERROR - Invalid position. Try again.")
                continue
            break
        return positions

    def get_AB(files):
        global at_bats
        while (True):
            try:
                at_bats = input("At bats: ")
                if (at_bats == "zero"):
                    at_bats = 0
                    print("Using At bats amount of 0")
                    break
                at_bats = int(at_bats)
                if (at_bats < 0):
                    print("ERROR - Don't put negative number. Try Again")
                    continue
                break
            except ValueError:
                print("ERROR - Don't put string. Try again.")

        return at_bats
    
    def get_Hits(files):
        global hits
        while (True):
            try:
                hits = input("Hits: ")
                hits = int(hits)
                if (hits < 0):
                    print("ERROR - Don't put negative number. Try Again.")
                    continue

                if hits > at_bats:
                    print("ERROR - Player cannot have more hits than at bats.")
                    continue
                break
            except ValueError:
                print("ERROR - Don't put string. Try again.")
        return hits
    
    def get_AVG(files):
        if at_bats == 0:
            average = 0
        elif at_bats == 0 and hits == 0:
            average = 0
        else:
            average = hits / at_bats
        return round(average, 3)

    def get_amount(files):
        return files.amount

    def add(files):
        player = []
        player.append(files.get_name())
        player.append(files.get_POS())
        player.append(files.get_AB())
        player.append(files.get_Hits())
        player.append(files.get_AVG())
        files.database.append(player)
        files.amount += 1
        print("{} was added".format(names))

    def check_index(files, prompt):
        try:
            ind = int(input(prompt)) - 1
            if (ind < files.get_amount() and ind >= 0):
                return ind
            else:
                print("\n Invalid")
        except Exception:
            print ("")
        return -1

    def get_index(files, prompt):
        ind = files.check_index(prompt)
        while (ind < -1):
            print("\nInvalid Index")
            ind = files.check_index(prompt)
        return ind

    def remove(files):
        ind = files.get_index("Number: ")
        new_name = files.database[ind][0]
        del (files.database[ind])
        files.amount -= 1
        print(new_name, "was deleted.")
        return files
    
    def move_player(files):
        ind = files.get_index("Current lineup number: ")
        print(files.database[ind][0], "Was selected")
        new_ind = files.get_index("New lineup number: ")

        temp = files.database[ind]
        files.database[ind] = files.database[new_ind]
        temp = files.database[new_ind][0] 
        print(temp, "Was moved")

    def edit_player_position(files):
        ind = files.get_index("Lineup number: ")
        print("You selected {0} POS = {1}".format(files.database[ind][0], files.database[ind][1]))
        positions = files.get_POS()
        files.database[ind][1] = positions
        print(files.database[ind][0], "Was updated.")

    def edit_player_stats(files):
        ind = files.get_index("Lineup number: ")
        print("You selected {0}, At bats = {1}, Hits = {2}".format(files.database[ind][0], files.database[ind][2], files.database[ind][3]))
        at_bats = files.get_AB()
        hits = files.get_Hits()
        average = files.get_AVG()
        files.database[ind][2] = at_bats
        files.database[ind][3] = hits
        files.database[ind][4] = average
        print("Edit stats")

    def get_choice(files):
        files.menu()
        try:
            choice = int(input(""))
            return choice
        except Exception:
            print("Invalid Choice")
            return -1

    def display(files):
        print("	 Player	 POS 	 AB 	 H 	 AVG\n")
        print("================================================================")
        for i in range(0, files.get_amount()):
            print(i + 1, end=" \t ")          
            for j in range(len(files.database[i])):
                print("%-20s%-7s%-7s\n"%(files.database[i][0],files.database[i][1],files.database[i][2],files.database[i][3]))
            print("")

def game_date():
    valid_date = False
    todays_date = datetime.date.today()
    print ("CURRENT DATE: ", todays_date)
    user_date = input("GAME DATE: ")

    if user_date == "":
        return

    while not valid_date:
        try:
            game_day = datetime.date(int(user_date[0:4]), int(user_date[5:7]), int(user_date[8:]))
            valid_date = True
        except ValueError:
            print("Enter a valid date.")
            user_date = (input("Game Date:\t\t"))
            if user_date == '':
                continue  

    days_until = int((game_day - todays_date).days)
    if days_until > 0:
        print("DAYS UNTIL GAME:" + str(days_until))
            

def main():
    team = Baseball()
    choice = 1
    print ("================================================================")
    print ("Baseball Team Manager\n")
    game_date()
    while (choice != 7):
        choice = team.get_choice()
        if (choice == 1):
            team.display()
        elif (choice == 2):
            team.add()
        elif (choice == 3):
            team.remove()
        elif (choice == 4):
            team.move_player()
        elif (choice == 5):
            team.edit_player_position()
        elif (choice == 6):
            team.edit_player_stats()
        elif (choice == 7):
            print ("Bye!")
            break
        else:
            print ()
            print ("Invalid option. Try again!")


if __name__ == "__main__":
    main()
