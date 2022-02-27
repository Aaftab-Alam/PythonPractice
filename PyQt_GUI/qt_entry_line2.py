import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc

class MainWindow(qtw.QWidget):
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hellow")
		self.setLayout(qtw.QVBoxLayout())
		self.setupUI()
	
	def setupUI(self):
		self.entry=qtw.QLineEdit(self,placeholderText="Hi")
		self.entry.setAlignment(qc.Qt.AlignRight)
		self.layout().addWidget(self.entry)


app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()