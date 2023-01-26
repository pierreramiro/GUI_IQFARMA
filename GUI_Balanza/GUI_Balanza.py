from MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QImage,QPixmap

import sys 
import pandas as pd ## Libreria para leer archivo csv
import logging ## Libreria para info Logging
from datetime import datetime ## Linreria para obtener fecha

   
""" 
//////////////////////////////////////////
//            MAIN CLASS GUI            //
//////////////////////////////////////////
"""
class GUI(QtWidgets.QMainWindow):
    def __init__(self):    
        QtWidgets.QMainWindow.__init__(self)
        ## Creamos nuestra GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
       
""" //////////////////////////////////////////
    //                Main                  //
    //////////////////////////////////////////
"""
def setUpGUI():
    ## Creamos formato Lgging
    FORMAT = '%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d): %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    ## Creamos la app
    app = QtWidgets.QApplication(sys.argv)  
    #Creamos el visualizador
    GUI_window=GUI()
    GUI_window.show()                        
    sys.exit(app.exec_())
    
