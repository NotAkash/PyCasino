#Give players a higher chance of winning 
#after a certain number of games have been played
#because, we are nice
def goffsetline():
    gplay= open("src/gplist.txt","r+")
    offsetline=[]
    offset = 0
    for line in gplay:
        offsetline.append(offset)
        offset += len(line)
    gplay.close()
    return(offsetline)



def goffset():
    #used to find the last line
    gplay= open("src/gplist.txt","r+")
    offsetline=[]
    offset = 0
    for line in gplay:
        offsetline.append(offset)
        offset += len(line)
    gplay.close()
    return(offset)

def ngame(game):

    gplay= open("src/gplist.txt","r+")
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
    gplay.write("\n\n%s\n0" %game)
                          

def gplayed(game):
    gplay= open("src/gplist.txt","r")
    lnum=0
    for i in goffsetline():
            
        if gplay.readline() ==(game+"\n"):
            tplayed= int(next(gplay))
            tplayed+=1    
            return tplayed     
