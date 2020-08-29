# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import sqlite3

class db:
    def __init__(files):
        files.positions = ("C", "1B", "2B", "3B", "SS", "LF" , "CF", "RF", "P")
        try:
            files.conn = sqlite3.connect("player_db.sqlite")
            files.cur = files.conn.cursor()
        except sqlite3.Error as err:
            print(err)
            quit()

    def __del__(files):
        files.conn.close()
        
    def csv_to_db(files, FILE_NAME):
        try:
            files.cur.execute("DROP TABLE IF EXISTS players")
            files.cur.execute("CREATE TABLE players (name TEXT, pos TEXT, at_bats INTEGER, hits INTEGER)")
            with open(FILE_NAME , "r") as f:
                for line in f:
                    line = line.strip().split(',')
                    files.cur.execute("insert into players (name, pos, at_bats, hits) values ('{}','{}',{},{})".format(*line))
                files.conn.commit()
        except FileNotFoundError:
            print ("ERROR - Unable to open {}".format(FILE_NAME))
            quit()
        except sqlite3.Error as err:
            print(err)
            quit()

    def load_from_db(files):
        files.cur.execute("select * from players")
        lists = files.cur.fetchall()
        database = []
        for player in lists:
            if(len(player) == 4):
                valid = files.valid_POS(player[1])
                allow = True
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",player)
                    print("Position is Invalid")
                    allow = False
                valid = files.valid_at_bats(player[2])
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",player)
                    print("At bat is Invalid")
                    allow = False
                valid = files.valid_H(player[3])
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",player)
                    print("Invalid Hits")
                    allow = False
                    
                if(allow):
                    database.append(player)
            else:
                print("Invalid text:", player)
        return database

    def save_to_db(files, database):
        files.cur.execute("delete from players;",)
        files.conn.commit()
        for data in database:
            files.cur.execute("insert into players (name, pos, at_bats, hits) values ('{}','{}',{},{})".format(*data))
        files.conn.commit()
            
    def valid_Names(files, names):
        if(names in files.names):
            return True
        else:
            return False

    def valid_POS(files, pos):
        if(pos in files.positions):
            return True
        else:
            return False

    def valid_at_bats(files, at_bats):
        try:
            at_bats = int(at_bats)
            return True
        except Exception:
            return False

    def valid_H(files, hits):
        try:
            hits = int(hits)
            return True
        except Exception:
            return False

    def valid_AVG(files, average):
        try:
            average = float(average)
            return True
        except Exception:
            return False

    def load_from_file(files, FILE_NAME):
        try: 
            database = []
            inp = open(FILE_NAME , "r")
            line = inp.readline()
        except FileNotFoundError:
            print ("ERROR - Unable to open {}".format(FILE_NAME))
            quit()
            
        while(line):
            player = line.strip().split(",")
            if(len(player) == 4):
                valid = files.valid_POS(player[1])
                allow = True
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",line)
                    print("Position is Invalid")
                    allow = False
                valid = files.valid_at_bats(player[2])
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",line)
                    print("At bat is Invalid")
                    allow = False
                valid = files.valid_H(player[3])
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",line)
                    print("Invalid Hits")
                    allow = False
                valid = files.valid_AVG(player[3])
                    
                if(allow):
                    database.append(player)
      
            else:
                print("Invalid text:",line)
            line = inp.readline()
            
        inp.close()
        return database

    def save_to_file(files, FILE_NAME, database):
        try: 
            output = open(FILE_NAME , "w", encoding = "utf-8")
        except FileNotFoundError:
            print ("ERROR - Unable to open {}".format(FILE_NAME))
            quit()
            
        for data in database:
            data = ','.join(list(map(str, data)))
            print(data, file = output)

        output.close()
