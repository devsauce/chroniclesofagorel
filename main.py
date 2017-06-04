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

def norl(mainc):
    r = raw_input("[N]ew or [L]oad? ")
    if (r == 'n' or r == 'N'):
        startgame()
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
