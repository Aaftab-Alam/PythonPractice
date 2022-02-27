import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hellow")
		self.setLayout(qtw.QGridLayout())
		self.setupUI()
	
	def setupUI(self):
		for i in range(3):
			for j in range(3):
				self.my_button=qtw.QPushButton(self)
				self.my_button.setText(str(9-(3*i+j)))
				self.my_button.setStyleSheet("padding:90px;")
				self.my_button.pressed.connect(lambda:self.func())
				self.layout().addWidget(self.my_button,i,j)
	def func(self):
		print(self.sender().text())
		


app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()