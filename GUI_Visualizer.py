from MainWindow import Ui_GUI_IQFARMA

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QImage,QPixmap

import sys


# Libreria para info Logging
import logging

""" //////////////////////////////////////////
    //            MAIN CLASS GUI            //
    //////////////////////////////////////////
"""

class GUI(QtWidgets.QMainWindow):
    """ _init_ (descripcion de variables)
    
    """
    def __init__(self):    
        QtWidgets.QMainWindow.__init__(self)
        ## Creamos nuestra GUI
        self.ui = Ui_GUI_IQFARMA()
        self.ui.setupUi(self)
        ## Creamos Flags
        self.flagCara1=False
        ## Cretamos Qtimers para evitar atasco en el constructor de la GUI
        self.FuncionTimer1()
        GUI
        
    def FuncionTimer1(self):
        print("hola",self.flagCara1)
        
    
class UuarioDialogBox():
    1


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