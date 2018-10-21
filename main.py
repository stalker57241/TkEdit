from tkinter import *

from modules import edit, helpm
class TKedit(object):
	def __init__(self, *args):
		self.root = Tk()
		self.text = Text(self.root)
		self.menubar = Menu(self.root)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.helpmenu = Menu(self.menubar)
		self.build()
	def build(self):
		self.root.title("TextEdit")
		self.text.pack(expand = True)
		self.filemenu.add_command(label = "New", command=edit.new(self.text))
		self.filemenu.add_command(label = "Open", command=edit.open(self.text))
		self.filemenu.add_command(label = "Save",command=edit.save(self.text))
		self.filemenu.add_command(label = "Save as...", command=edit.saveas(self.text))
		self.filemenu.add_separator()
		self.filemenu.add_command(label = "exit", command=self.root.quit)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		self.helpmenu.add_command(label="About", command=helpm.about)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)
		self.root.config(menu=self.menubar)
		self.root.mainloop()

if __name__ == "__main__":
	TKedit()