#New CSV Supporting Database, To Compensate For The Senseless Newline (\r\n) On Windows
#Reworked The Entire Database On .csv (Comma Seperated Values)
#Import Files
import csv

#Open files
def openfile():
    while True:
        try:
            player = open("src/plist.csv","r+")              #This algorithm validates where the file is opening plist.csv from
        except FileNotFoundError:                           #if it's being opened from parent, then open from "src/plist.csv"            player= open("plist.csv","r+")
            while True:
                try:
                    player= open("plist.csv","r+")
                except FileNotFoundError:
                    gplay = open("plist.csv","w")
                    gplay.close()
                    player=open("plist.csv","r+")
                    break
                else:
                    break
            break
        else:
            break
    return(player)


def writeinfile():
    try:
        player = open('src/plist.csv',"w", newline='')  # This algorithm validates where the file is opening plist.csv from
    except FileNotFoundError:                        # if it's being opened from parent, then open from "src/plist.csv"
        player = open("plist.csv","w", newline='')
    return(player)

#Init User
def player_init(name):
    player= openfile()
    readfile = csv.reader(player)
    rows=[]
    for row in readfile:
        rows.append(row)
        for entity in row:
            if entity==name:
                player.close()
                return(False)
    player.close()
    player= writeinfile()
    writer= csv.writer(player)

    writer.writerows(rows)
    names=[]
    names.append(name)
    names.append("500.00")
    name=names
    writer.writerow([""])
    writer.writerow(name)
    player.close()

    return

#Returning User
def player_cont(name):
    player = openfile()
    readfile = csv.reader(player)
    for row in readfile:
        while True:
            try:
                if row[0]==name:

                    money = row[1]
                    player.close()
                    money= float(money)
                    return money
            except IndexError:
                break
            else:
                break
    player.close()
    return False

#Update User
def pbal_update(name,win):
    player= openfile()
    readfile = csv.reader(player)

    rows = []

    for row in readfile:
        rows.append(row)
    money= player_cont(name) + win
    player = writeinfile()
    writer = csv.writer(player)
    player= writeinfile()

    a=0

    for i in rows:
        b = 0
        for j in i:
            while True:
                try:
                    if j==name:
                        rows[a][b+1]=money
                    b += 1
                except IndexError:
                    break
                else:
                    break
        a += 1
    writer.writerows(rows)
    player.close()
    return(float(money))