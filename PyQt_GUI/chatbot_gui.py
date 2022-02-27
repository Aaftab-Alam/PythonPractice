import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	i=0
	j=0
	
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Chatbot")
		self.setupUI()
	

	def setupUI(self):
		global chatlayout
		outerlayout=qtw.QVBoxLayout()
		header=qtw.QGridLayout()
		footer=qtw.QGridLayout()
		chatlayout=qtw.QGridLayout()
		
		##------Header--------##
		self.chat_icon=qtw.QLabel("Icon",self)
		#self.chat_icon.setStyleSheet=("margin:0px;padding:30px; background:{color};color:white;")
		self.chat_icon.setStyleSheet("border:2px solid black;padding:0px;")
		header.addWidget(self.chat_icon,0,0)
		self.chat_name=qtw.QLabel("Chatbot",self)
		self.chat_name.setStyleSheet("border:2px solid black")
		header.addWidget(self.chat_name,0,1)
		header.setColumnStretch(2,1)
		
		## -----TextBar------##
		self.textbar=qtw.QLineEdit(placeholderText="Type...")
		footer.addWidget(self.textbar)
		self.textbar.setStyleSheet("border:2px solid lightblue;border-radius:10px;padding:10px;margin:20px;height:140px;font-size:80px;")
		self.send_button=qtw.QPushButton("Send",clicked=lambda:self.sent())
		footer.addWidget(self.send_button,0,1)
	
		outerlayout.addLayout(header)
		outerlayout.addLayout(chatlayout)
		outerlayout.addStretch()
		outerlayout.addLayout(footer)
		self.setLayout(outerlayout)
	
	def sent(self):
			global chatlayout,i,j
			text=self.textbar.text()
			if text=="":
				pass
			else:
				self.chat=qtw.QLabel(text)
				chatlayout.addWidget(self.chat,MainWindow.i,MainWindow.j)
				MainWindow.i+=1
				self.textbar.setText("")
				self.textbar.setPlaceholderText("Type...")
				#MainWindow.j+=1
	
	

app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()