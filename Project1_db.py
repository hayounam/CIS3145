class db:
    def __init__(files):
        
        files.positions = ("C", "1B", "2B", "3B", "SS", "LF" , "CF", "RF", "P")
       
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
            if(len(player) == 5):
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
                valid = files.valid_AVG(player[4])
                if(not valid):
                    if(allow):
                        print("Error(s) Occured in Player with details:",line)
                    print("Average is Invalid")
                    allow = False
                if(allow):
                    database.append(player)
     
            else:
                print("Invalid no.of fileds are there for player with details:",line)
            line = inp.readline()
        inp.close()
        return database

    def write_to_file(files, FILE_NAME, database):
        f = open(FILE_NAME,"w")
        f.write("Player,POS,AB,H,AVG\n")
        for player in database:
            for i in range(5):
                f.write(player[i])
                if(i < 4):
                    f.write("")
            f.write("\n")
        f.close()
