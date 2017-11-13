#New CSV Supporting Database, To Compensate For The Senseless Newline (\r\n) On Windows
#Reworked The Entire Database On .csv (Comma Seperated Values)


#Give players a higher chance of winning after a certain number of games have been played
#because, we are nice

#Import Files
import csv

#Open Files To Read
def openfile():
    while True:
        try:
            player = open("src/gplist.csv","r+")              #This algorithm validates where the file is opening gplist.csv from
        except FileNotFoundError:                           #if it's being opened from parent, then open from "src/gplist.csv"            player= open("gplist.csv","r+")
            while True:
                try:
                    player= open("gplist.csv","r+")
                except FileNotFoundError:
                    gplay = open("gplist.csv","w")
                    gplay.close()
                    player=open("gplist.csv","r+")
                    break
                else:
                    break
            break
        else:
            break
    return(player)

#Open Write File #Todo Test Games Without writeinfile()
def writeinfile():
    try:
        player = open('src/gplist.csv',"w", newline='')  # This algorithm validates where the file is opening gplist.csv from
    except FileNotFoundError:                        # if it's being opened from parent, then open from "src/gplist.csv"
        player = open("gplist.csv","w", newline='')
    return(player)

#List Games Played
def gplayed(game):
    player = openfile()
    readfile = csv.reader(player)
    for row in readfile:
        while True:
            try:
                if row[0]==game:
                    game = row[1]
                    player.close()
                    game= int(game)
                    return game
            except IndexError:
                break
            else:
                break
    player.close()
    return False

#New Game Played

def ngame(game):
    player= openfile()
    readfile = csv.reader(player)

    rows = []

    for row in readfile:
        rows.append(row)
    player = writeinfile()
    writer = csv.writer(player)
    player= writeinfile()

    a=0
    gplayed=0
    for i in rows:
        b = 0
        for j in i:
            while True:
                try:
                    if j==game:

                        rows[a][b+1]=str(int(rows[a][b+1])+1)
                        gplayed= int(rows[a][b+1])

                    b += 1
                except IndexError:
                    break
                else:
                    break
        a += 1

    writer.writerows(rows)
    if gplayed==0:
        ngame=[]
        ngame.append(game)
        ngame.append("1")
        writer.writerows("")
        writer.writerow(ngame)
        player.close()
        return(int(1))

    player.close()
    return(gplayed)
"""
$List Of The Games And How Much They Have Been Played
Game, Times Played

Akash,1
"""