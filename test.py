import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QAction
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.uic import *

app = QApplication(sys.argv)
cocktail = loadUi('create.ui')

def mixCocktail(str):
      cocktail.show()
      cocktail.showFullScreen()
      cocktail.lbl_header.setText(str)
      return self 


widget = loadUi('drinkmixer.ui')

widget.btn_ckt1.clicked.connect(mixCocktail("string"))

widget.show()
sys.exit(app.exec_())