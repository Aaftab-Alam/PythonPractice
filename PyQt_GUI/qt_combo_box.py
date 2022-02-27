import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hellow")
		self.setLayout(qtw.QVBoxLayout())
		self.setupUI()
	
	def setupUI(self):
		self.my_label=qtw.QLabel(self)
		self.my_label.setText("Pick any one of the following!")
		self.layout(). addWidget(self.my_label)
		
		self.my_label1=qtw.QLabel(self)
		self.my_label1.setText("")
		self.layout(). addWidget(self.my_label1)
		
		self.my_label2=qtw.QLabel(self)
		self.my_label2.setText("")
		self.layout(). addWidget(self.my_label2)
		
		self.my_combo=qtw.QComboBox(self)
		self.my_combo.addItem("Pizza","First")
		self.my_combo.addItem("Burger","Second")
		self.my_combo.addItem("Cold Drink","Third")
		#Adding List
		self.my_combo.addItems(["French Fries","Momos","Kulche"])
		self.layout(). addWidget(self.my_combo)
		
		#Adding item/items at certain index
		self.my_combo.insertItem(2,"Inserted item")
		#insertItem(index,list) for multiple items
		
		self.my_button=qtw.QPushButton(self)
		self.my_button.setText("Click me!")
		self.my_button.pressed.connect(lambda : self.my_func())
		self.my_button.setStyleSheet("display:inline-block;padding:0.3em 1.2em;margin:0 0.1em 0.1em 0;border:0.06em solid rgba(0,255,255,1);border-radius:2em;box-sizing: border-box;text-decoration:none;font-family:'Roboto',sans-serif;font-weight:300;color:#000098;text-shadow: 0 0.04em 0.04em rgba(0,0,0);text-align:center;transition: all 0.2s; border-radius:50px; background-color:rgba(0,215,215,1);")
		self.layout().addWidget(self.my_button)
		
	def my_func(self):
		self.my_label.setText(f"You picked {self.my_combo.currentText()}!")
		self.my_label1.setText(f"Data of item {self.my_combo.currentData()}")
		self.my_label2.setText(f"Index of item {self.my_combo.currentIndex()}")
		
app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()