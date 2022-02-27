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
		my_label.setText("Spinboxes!!!")
		self.layout().addWidget(my_label)
		
		my_spin=qtw.QSpinBox(self,value=20,maximum=100,minimum=0,singleStep=10)
		my_spin.setFont(qtg.QFont("Lucida",22))
		self.layout().addWidget(my_spin)
		
		
		my_button=qtw.QPushButton(self)
		my_button.setText("Press")
		my_button.pressed.connect(lambda: button_func())
		self.layout().addWidget(my_button)
		
		def button_func():
			my_label.setText(f"You choose {my_spin.value()}")


app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()