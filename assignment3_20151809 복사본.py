import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
                    break
        elif parse[0] == 'inc':
            for i in (0, len(scdb)):
                    print('Score', + i)
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = [ {'Name':'Lee', 'Score':30, 'Age':18},
    {'Name':'Kim', 'Score':40, 'Age':19},
    {'Name':'Park', 'Score':50, 'Age':23},
    {'Name':'Choi', 'Score':90, 'Age':18}]

def findScoreDB(scdb, keyname):
    for i in range(0, len(scdb)):
        if (keyname == scdb[i]['Name']):
            return i
    return ()

name = input("find name: ")
idx = findScoreDB(scoredb, name)
if idx >= 0:
    print(scoredb[idx])
else:
    print("No Such Name")

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
