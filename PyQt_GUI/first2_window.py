from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import sys

def window():
	app=QApplication(sys.argv)
	win=QWidget()
	#win.setLayout(QtWidgets.QVBoxLayout())
	win.setWindowTitle("Aadil")
	win.setGeometry(100,100,500,500)
	label=QtWidgets.QLabel(win)
#	label=QtWidgets.QLabel("Aadil")
	label.setText("Myvdvdv first Lhdhdhdabel")
#	label.move(100,100)
	
	win.show()
	sys.exit(app.exec_())
	
window()