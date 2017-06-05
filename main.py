import savefunc
import ctypes
mainc = ctypes.entity()
def l2b(lfile, mainc):
    s = lfile.readline()
    mainc.name = s[6:-1]
    s = lfile.readline()
    mainc.mhp = int(s[4:-1])
    mainc.chp = int(s[4:-1])
    s = lfile.readline()
    mainc.strn = int(s[6:-1])
    s = lfile.readline()
    mainc.defn = int(s[6:-1])
def startgame(mainc):
    mainc.name = raw_input("What will your name be? ")
    c = 0
    while (not(c>0 and c<4)):
        try:
            c = int(raw_input("Warrior[1], Mage[2], or Rogue[3]? "))
        except:
            c = 0
    if (c==1):
        mainc.strn = 5
        mainc.defn = 3
        mainc.mhp = 20
    elif (c==2):
        mainc.strn = 3
        mainc.defn = 3
        mainc.mhp = 40
    else:
        mainc.strn = 3
        mainc.defn = 5
        mainc.mhp = 20
    mainc.chp = mainc.mhp
    return                                  ##PICK UP HERE##

def norl(mainc):
    r = raw_input("[N]ew or [L]oad? ")
    if (r == 'n' or r == 'N'):
        startgame(mainc)
        return
    if (r == 'l' or r == 'L'):
        lfile = savefunc.load()
        try:
            l2b(lfile, mainc)
        except:
            print("Load error; corrupt data")
            return
    else:
        norl(mainc)
    return
norl(mainc)
