#Give players a higher chance of winning 
#after a certain number of games have been played
#because, we are nice
def goffsetline():
    while True:
        try:
            gplay= open("src/gplist.txt","r+")              #This algorithm validates where the file is opening gplist.txt from
        except FileNotFoundError:                           #if it's being opened from parent, then open from "src/gplist.txt"
            gplay= open("gplist.txt","r+")                       #if being opened from sub then open from "gplist.txt"
            break
        else:
            break
    offsetline=[]
    offset = 0
    for line in gplay:
        offsetline.append(offset)
        offset += len(line)
    gplay.close()
    return(offsetline)



def goffset():
    #used to find the last line
    while True:
        try:
            gplay= open("src/gplist.txt","r+")              #This algorithm validates where the file is opening gplist.txt from
        except FileNotFoundError:                           #if it's being opened from parent, then open from "src/gplist.txt"
            gplay= open("gplist.txt","r+")                       #if being opened from sub then open from "gplist.txt"
            break
        else:
            break
    offsetline=[]
    offset = 0
    for line in gplay:
        offsetline.append(offset)
        offset += len(line)
    gplay.close()
    return(offset)

def ngame(game):
    while True:
        try:
            gplay= open("src/gplist.txt","r+")              #This algorithm validates where the file is opening gplist.txt from
        except FileNotFoundError:                           #if it's being opened from parent, then open from "src/gplist.txt"
            gplay= open("gplist.txt","r+")                       #if being opened from sub then open from "gplist.txt"
            break
        else:
            break
    lnum=0
    for i in goffsetline():
            
        if gplay.readline() ==(game+"\n"):
            tplayed= int(next(gplay))
            tplayed+=1
                
            offset=goffsetline()
            gplay.seek(offset[lnum+1])
            gplay.write(str(tplayed))
                
            return

        else:
            lnum=lnum+1
        
    gplay.seek(goffset())
    gplay.readline()
    gplay.write("\n\n%s\n1" %game)
                          

def gplayed(game):
    while True:
        try:
            gplay= open("src/gplist.txt","r+")              #This algorithm validates where the file is opening gplist.txt from
        except FileNotFoundError:                           #if it's being opened from parent, then open from "src/gplist.txt"
            gplay= open("gplist.txt","r+")                       #if being opened from sub then open from "gplist.txt"
            break
        else:
            break
    lnum=0
    for i in goffsetline():
            
        if gplay.readline() ==(game+"\n"):
            tplayed= int(next(gplay))
            tplayed+=1    
            return tplayed     
