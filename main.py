from tts import tts
from tts import exportAudio
import fs
from kbhit import KBHit
from termcolor import colored
from colorama import init
import command
from math import ceil
init()

kb = KBHit()
reader = tts()

# Wad Check 
fs.checkWad()

def export():
    books = fs.listBooks()
    i = 0
    pad = ceil(len(books)/10)

    for book in books:
        print(f"{str(i).rjust(pad, '0')} ({fs.readLine(book)}/{len(fs.getBook(book))}): {book[0:len(book)-4]}")
        i += 1
    print("q: Exit")

    bookNo = input("-> ")
    if bookNo == "q":
        return
    book = books[int(bookNo)]
    text = ""
    for line in book: text = text + line

    exportAudio(text)
    print("Exported audio file")

def readBook():
    books = fs.listBooks()
    i = 0
    pad = ceil(len(books)/10)

    for book in books:
        if fs.readLine(book) == 0:
            print(colored(f"{str(i).rjust(pad, '0')} ({fs.readLine(book)}/{len(fs.getBook(book))}): {book[0:len(book)-4]}", "green"))
        elif fs.readLine(book) == len(fs.getBook(book)):
            print(f"{str(i).rjust(pad, '0')} ({fs.readLine(book)}/{len(fs.getBook(book))}): {book[0:len(book)-4]}")
        else:
            print(colored(f"{str(i).rjust(pad, '0')} ({fs.readLine(book)}/{len(fs.getBook(book))}): {book[0:len(book)-4]}", "yellow"))
        i += 1
    print("q: Exit")

    bookNo = input("-> ")
    if bookNo == "q":
        return

    # And the Golden Shit award goes to...
    try:
        _ = int(bookNo)
    except:
        return

    book = books[int(bookNo)]
    reader.setBook(book)

    # Book reading loop
    print(f'Reading {book[0:len(book)-4]}. Press "Esc" and "Enter" to stop at the end of the line')
    while True:
        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break
        kb.set_normal_term()
    
        if not reader.readLine(): return

def manageFics():
    while True:
        fics = fs.getFics()
        print(colored(f'found {len(fics)} works synced with AO3:', 'blue'))
        i = 0
        for name, id in fics:
            print(f'{i}| ID:{id} Name:"{name}"')
            i += 1
        print()
        print('a: Add new synced AO3 fic')
        print('d: Delete sync')
        print('s: Sync fic(s)')
        print('q: Return to main menu')

        uin = input("-> ")
        if uin == "a":
            name = input('Fic name \n-> ')
            fId = int(input('Fic id \n-> '))
            fics.append((name, fId))
            fs.addFic(fics)
        elif uin == "d":
            fId = int(input('Sync ID\n-> '))
            fics.pop(fId)
            fs.addFic(fics)
        elif uin == "s":
            for name, id in fics:
                command.clear()
                command.scrapeWork(name, id)
                command.clear()
        elif uin == "q": return
        
while True:
    print(colored("Bob's fan fic reader rev 1", 'blue'))
    print('r: Read')
    print('m: Manage synced fics')
    print('e: Export audio')
    print('q: Quit')


    uin = input("-> ")
    command.clear()
    if uin == "r": readBook()
    elif uin == "e": export()
    elif uin == "m": manageFics()
    elif uin == "q": break
