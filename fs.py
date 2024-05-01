import pickle
from os.path import join
from os import listdir
from os import path
import re

def checkWad():
    if not path.exists('data.wad'):
        open('data.wad', 'x')
        with open('data.wad', 'wb') as f:
            pickle.dump(wad(), f)
class wad:
    def __init__(self, oldWad = {}):
        self.bookLines = oldWad
        self.ao3Remotes = []

def getFics():
    with open("data.wad", "rb") as f:
        x = f.read()
        x = pickle.loads(x)
        if x.ao3Remotes:
            return x.ao3Remotes.copy()
        else: return []

def addFic(fic):
    x = None
    with open("data.wad", "rb") as f:
        x = f.read()
        x = pickle.loads(x)
        x.ao3Remotes = fic
    
    with open("data.wad", "wb") as f:
        x = pickle.dumps(x)
        f.write(x)


def listBooks():
    books = listdir("books")
    return books

def getBook(fileName):
    with open(join("books",fileName), "rt") as f:
        v = f.read()
        v = re.split(r' *[\.\?!][\'"\)\]]* *', v)
        return v

def readLine(book):
    with open("data.wad", "rb") as f:
        x = f.read()
        x = pickle.loads(x)
        if book in x.bookLines:
            return x.bookLines[book]
        else: return 0

def setLine(book, line):
    x = None
    with open("data.wad", "rb") as f:
        x = f.read()
        x = pickle.loads(x)
        x.bookLines[book] = line
    
    with open("data.wad", "wb") as f:
        x = pickle.dumps(x)
        f.write(x)
