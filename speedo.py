#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-= SPEEDO.py -=
A simple Speed Reader written in Python.
No other dependencies required.

written by Mario Kaufmann
"""

from Tkinter import *
import time

pause = False

class Book(object):
    """represents a book"""

    def __init__(self):
	    self.mark = 0
	    self.wpm = 400
	
	    with open("nietzsche.txt", "r") as t:
	        self.text = [l.strip("\n") for l in t]
	        self.text = " ".join(self.text)
	        self.text = self.text.split(" ")
	        self.word_count = len(self.text)
	        print self.word_count

    def __iter__(self):
        while 1:
            yield self.mark, self.text[self.mark]
            self.mark += 1

    def go_to(word):
        self.mark = word


""" helper functions """
def key(event):
	if event.char == "\x1b":
	    event.widget.quit()
	
	if event.char == "+":
	    book.mark = book.mark + book.word_count / 10
	if event.char == "-":
	    book.mark = book.mark - book.word_count / 10
	
	if event.char == " ":
	    global pause
	    pause = not pause
	
	if event.char == "1":
	    book.wpm = 100
	if event.char == "2":
	    book.wpm = 200
	if event.char == "3":
	    book.wpm = 300
	if event.char == "4":
	    book.wpm = 400
	if event.char == "5":
	    book.wpm = 500
	if event.char == "6":
	    book.wpm = 600
	if event.char == "7":
	    book.wpm = 700
	if event.char == "8":
	    book.wpm = 800
	if event.char == "9":
	    book.wpm = 900
	#print repr(event.char)
	#print event.char


def update():
	global pause
	if pause:
	    pass
	else:
	    i, temp = book_iter.next()
	    v.set(temp)
	    u.set(str(i * 100 / book.word_count))
	
	#if temp.endswith("."):
	    #t.after(update_after * 2, update)
	#else:
	    #t.after(update_after, update)
	
	update_after = 60 * 1000 // book.wpm
	t.after(update_after, update)



""" main entry """
if __name__ == "__main__":

	book = Book()
	book_iter = iter(book)
	root = Tk()
	
	# the appearance of the frame can be modified choosing a relief type and
	# applying appropriate bandwidth.
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))
	root.focus_set()
	
	#root.bind("<Escape>", lambda e: e.widget.quit())
	root.bind("<Key>", key)
	
	#f = Frame(root,borderwidth=2,relief=SUNKEN, width=100, height=h/2 - 100)
	f = Frame(root, width=w, height=h / 2.0 - 100)
	f.pack()
	
	#.pack(side=LEFT,padx=5,pady=5)
	v = StringVar()
	u = StringVar()
	
	#t = Label(root,textvariable=v, font=("Helvetica", 50), justify=CENTER)
	t = Label(root, textvariable=v, font=("Myriad Pro", 50), justify=CENTER)
	
	percent = Label(root, textvariable=u, font=("Myriad Pro", 12), justify=CENTER)
	
	#t.pack(expand=1)
	t.pack()
	percent.pack()
	
	update()
	
	root.title("SPEEDO.py")
	root.mainloop()