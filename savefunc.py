def load():
    f = open("save/pc.cf", 'r')
    return f
def save(mainc):
    f = open("save/pc.cf", 'w')
    ts = "name: " + mainc.name + '\n' + "hp: " + str(mainc.mhp)+ '\n' + "strn: " + str(mainc.strn) + '\n' + "defn: " + str(mainc.defn) + '\n'
    f.write(ts)
    f.close()
    return
