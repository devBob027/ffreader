import pyttsx3
import fs

def exportAudio(book):
    engine = pyttsx3.init()
    engine.save_to_file(fs.getBook(book)[fs.readLine(book):len(fs.getBook(book))], book[0:len(book)-4]+".mp3")
    engine.runAndWait()

class tts:
    def __init__(self):
        self.engine = pyttsx3.init()

    def setBook(self, book):
        self.book = book
        self.text = fs.getBook(book)
        self.line = fs.readLine(book)
        
    def readLine(self):
        if self.line == len(self.text): return False
        self.engine.say(self.text[self.line])
        print(f"{fs.readLine(self.book)}/{len(self.text)}| {self.text[self.line]}")
        self.engine.runAndWait()
        self.line += 1
        fs.setLine(self.book, self.line)
        return True