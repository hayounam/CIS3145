# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import datetime
from db import db
from objects import *

class Display:
    def __init__(self):
        self.positions_list = ("C", "1B", "2B", "3B", "SS", "LF", "C", "RF", "P")

    def menu(self):
        print("\nMENU OPTIONS")
        print("1 - Display Lineup")
        print("2 - Add Player")
        print("3 - Remove Player")
        print("4 - Move Player")
        print("5 - Edit player position")
        print("6 - Edit Player stats")
        print("7 - Exit Program\n")
        print("POSITIONS")
        print(self.position_list())
        print("================================================================\n")

    def position_list(self):
        """
        Use tuple
        """
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(*self.positions_list)

    def get_name(self):
        first_name = str(input("Enter Name(First name): "))
        last_name = str(input("Enter Name(Last name): "))
        return first_name, last_name

    def get_position(self):
        while (True):
            position = input("Position: ").strip().upper()
            if position not in self.positions_list:
                print("ERROR - Invalid position. Try again.")
                continue
            break
        return position

    def get_at_bats(self):
        at_bats = 0
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

    def get_hits(self, at_bats):
        hits = 0
        while (True):
            try:
                hits = int(input("Hits: "))
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

    def add_player(self):
        first_name, last_name = self.get_name()
        position = self.get_position()
        at_bats = self.get_at_bats()
        hits = self.get_hits(at_bats)
        return Player(first_name, last_name, position, at_bats, hits)

    def get_number(self, prompt = ""):
        number = 0
        while (True):
            try:
                number = int(input(prompt))
                if (number < 0):
                    print("ERROR - Don't put negative number. Try Again.")
                    continue
                break
            except ValueError:
                print("ERROR - Don't put string. Try again.")
        return number

def game_date():
    valid_date = False
    todays_date = datetime.date.today()
    print("CURRENT DATE:\t{}".format(todays_date))
    user_date = input("GAME DATE:\t")

    if user_date == "":
        return

    game_day = 0
    while not valid_date:
        try:
            game_day = datetime.date(int(user_date[0:4]), int(user_date[5:7]), int(user_date[8:]))
            valid_date = True
        except ValueError:
            print("Enter a valid date.")
            user_date = (input("GAME DATE:\t"))
            if user_date == '':
                continue  

    days_until = int((game_day - todays_date).days)
    if days_until > 0:
        print("DAYS UNTIL GAME:" + str(days_until))

def main():
    team = Display()
    data_driver = db()

    #########################################
    # RESET DATA BASE
    #data_driver.csv_to_db("players.csv")
    #########################################

    database = data_driver.load_from_db()
    if (len(database) == 0):
        return

    lineup  = Lineup()
    for data in database:
        first_name, last_name = data[0].split()
        position = data[1]
        at_bats = int(data[2])
        hits = int(data[3])
        player = Player(first_name, last_name, position, at_bats, hits)
        lineup.add(player)

    print ("================================================================")
    print ("Baseball Team Manager\n")

    game_date()
    team.menu()

    while (True):
        choice = 0
        try:
            choice = int(input("\nMenu option: "))
        except Exception:
            print("\nInvalid Choice")
            continue

        if (choice == 1):
            lineup.display_lineup()
        elif (choice == 2):
            lineup.add(team.add_player())
        elif (choice == 3):
            lineup.remove(team.get_number("Number: "))
        elif (choice == 4):
            number1 = team.get_number("Current lineup number: ")
            number2 = team.get_number("New lineup number: ")
            lineup.move(number1, number2)
        elif (choice == 5):
            number = team.get_number("Lineup number: ")
            position = team.get_position()
            lineup.edit_player_position(number, position)
        elif (choice == 6):
            number = team.get_number("Lineup number: ")
            at_bats = team.get_at_bats()
            hits = team.get_hits(at_bats)
            lineup.edit_player_stats(number, at_bats, hits)
        elif (choice == 7):
            data_driver.save_to_db(lineup.get_players_db())
            print ("Bye!")
            break
        else:
            print ()
            print ("Invalid option. Try again!")        

if __name__ == "__main__":
    main()
