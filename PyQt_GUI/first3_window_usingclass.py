from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(100,100,1000,1000)
		self.setWindowTitle("Bac")
		self.initUI()
		
	def initUI(self):
		self.label=QtWidgets.QLabel(self)
		self.label.setText("Hello Motherfucker")
		self.label.move(100,100)
		self.update(self.label)
		
		self.b1=QtWidgets.QPushButton(self,clicked=self.func)
		self.b1.setText("Click me motherfucker")
		#self.b1.clicked.connect(func)
		self.b1.move(100,200)
		self.update(self.b1)
		
	def func(self):
		self.label.setText("You clicked a button you motherfucker")
		self.update(self.label)
		
	def update(self,widget):
		self.widget=widget
		self.widget.adjustSize()
		
def window():
		app=QApplication(sys.argv)
		win=MyWindow()
		win.show()
		sys.exit(app.exec_())
		
window()
		