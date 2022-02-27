import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Hellow")
		self.txt=""
		self.setupUI()
	
	def setupUI(self):
		outerlayout=qtw.QVBoxLayout()
		entry_layout=qtw.QHBoxLayout()
		button_layout=qtw.QGridLayout()
		#button_layout.setSpacing(8)
		self.entry=qtw.QLineEdit(placeholderText="0",readOnly=True)
		self.entry.setStyleSheet("border:2px solid lightblue;border-radius:10px;padding:10px;margin:20px;height:140px;font-size:80px;")
		self.entry.setAlignment(qc.Qt.AlignRight)
		entry_layout.addWidget(self.entry)
		
		for i in range(3):
			for j in range(3):
			  text=str(9-(3*i+j))
			  self.add_button(text)
			  button_layout.addWidget(self.button,1+i,j)
		
		alist=["+","-","*","/","="]	
		for i in range(len(alist)):
			self.add_button(alist[i],"#2E8B57") if alist[i]=="=" else self.add_button(alist[i],"#5D3FD3")
			button_layout.addWidget(self.button,i,3)
		
		self.add_button(".","#5D3FD3")
		button_layout.addWidget(self.button,4,2)
		self.add_button("0")
		button_layout.addWidget(self.button,4,0,1,2)
		self.add_button("C","#5D3FD3")
		button_layout.addWidget(self.button,0,0,1,2)
		self.add_button("Del","#5D3FD3")
		button_layout.addWidget(self.button,0,2)
			
		outerlayout.addLayout(entry_layout)
		outerlayout.addLayout(button_layout)
		self.setLayout(outerlayout)
		
	def add_button(self,text,color="#DA70D6"):
		self.button=qtw.QPushButton(text,clicked=lambda:self.func(),styleSheet=f"margin:0px;padding:30px; background:{color};color:white;")
			
	def func(self):
		val=self.sender().text()
		if val=="C":
			self.entry.setText("")
			self.entry.setPlaceholderText("0")
			self.txt=""
		elif val=="Del":
			self.txt=self.txt[0:len(self.txt)-1]	
			self.entry.setText(self.txt)
		elif val=="=":
			try:
				result=str(eval(self.txt))
				self.entry.setText(result)
			except:
				self.entry.setPlaceholderText("Invalid Syntax")
		else:
			self.txt=self.entry.text() + val
			self.entry.setText(self.txt)
			
app=qtw.QApplication([])
win=MainWindow()
win.show()

app.exec_()