from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
global FILENAME

def new(text):
	global FILENAME
	text.delete('1.0', END)
	FILENAME = "Untiled"
def open(text):
	files = askopenfile(mode="r")
	textf = files.read()
	text.insert('1.0', textf)
	files.close()
def save(text):
	pass
def saveas(text):
	pass
