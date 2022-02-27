import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hellow")
		self.setLayout(qtw.QVBoxLayout())
		self.setupUI()
	
	def setupUI(self):
		my_label=qtw.QLabel(self)
		my_label.setText("Hello How are you?")
		self.layout().addWidget(my_label)
		
		my_text=qtw.QTextEdit(self,lineWrapMode=qtw.QTextEdit.FixedColumnWidth,lineWrapColumnOrWidth=30,placeholderText="Type Something...",)
		self.layout().addWidget(my_text)
		
		my_button=qtw.QPushButton(self)
		my_button.setText("Click me")
		my_button.pressed.connect(lambda : press_it())
		self.layout().addWidget(my_button)
		
		def press_it():
			my_label.setText(f"You typed '{my_text.toPlainText()}'")
			my_text.setPlainText("")
			my_text.setPlaceholderText("You clicked the button")
		


app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()