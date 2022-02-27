import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hellow")
		self.setLayout(qtw.QVBoxLayout())
		
		my_label=qtw.QLabel("Hello Aadil")
		my_label.setFont(qtg.QFont("Lucida"))
		self.layout().addWidget(my_label)
		
		my_entry=qtw.QLineEdit()
		my_entry.setObjectName("name_field")
		my_entry.setText("")
		self.layout().addWidget(my_entry)
		
		my_button=qtw.QPushButton("Press",clicked=lambda :press_it())
		self.layout().addWidget(my_button)
		
		self.show()
		
		def press_it():
			my_label.setText(f"Hello {my_entry.text()}")
			my_entry.setText("")
			
app=qtw.QApplication([])
mw=MainWindow()

app.exec_()