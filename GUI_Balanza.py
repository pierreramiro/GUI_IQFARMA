from MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QImage,QPixmap

import sys 
import pandas as pd ## Libreria para leer archivo csv
import logging ## Libreria para info Logging
from datetime import datetime ## Linreria para obtener fecha
from threading import Thread
import time
import snap7

""" GLOBAL VARIABLE """
FLAG_PLC_AVALABLE=False


#CARACTERÍSTICAS HARDWARE Y SOFTWARE DEL PLC
IP = '192.168.0.1'
RACK = 0
SLOT = 1

DB_NUMBER = 2
START_ADDRESS = 0
SIZE = 259

value = 1


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
        """ creamos variables FLAG """
        self._FLAG_initProcess = False
        """ creamos variables generales """
        self.idCaja=0
        self.Peso=25.0
        self.Param1=None
        self.Param2=None
        self.Param3=None
        self.Param4=None
        self.Param5=None
        self.Decision=None
        self.oldText=None        
        self.ui.plainTextEdit_peso.setPlainText("{:.4f}".format(self.Peso))
        """ Iniciaizamos un Check """
        self.ui.radioButton_param1.setChecked(True)
        """ Asignamos conexion entre botones de numeros"""
        self.ui.pushButton_digito0.pressed.connect(self.dig0_pressed)
        self.ui.pushButton_digito1.pressed.connect(self.dig1_pressed)
        self.ui.pushButton_digito2.pressed.connect(self.dig2_pressed)
        self.ui.pushButton_digito3.pressed.connect(self.dig3_pressed)
        self.ui.pushButton_digito4.pressed.connect(self.dig4_pressed)
        self.ui.pushButton_digito5.pressed.connect(self.dig5_pressed)
        self.ui.pushButton_digito6.pressed.connect(self.dig6_pressed)
        self.ui.pushButton_digito7.pressed.connect(self.dig7_pressed)
        self.ui.pushButton_digito8.pressed.connect(self.dig8_pressed)
        self.ui.pushButton_digito9.pressed.connect(self.dig9_pressed)
        """ Asignamos conexion entre botones de DER e IZQ"""
        self.ui.pushButton_der.pressed.connect(self.der_pressed)
        self.ui.pushButton_izq.pressed.connect(self.izq_pressed)
        
        """  Asignamos accion a DEL y OK"""
        self.ui.pushButton_digitoDEL.pressed.connect(self.digDEL_pressed)
        self.ui.pushButton_digitoOK.pressed.connect(self.digOK_pressed)
        """ CREAMOS HILO QUE SONDEA BANDERA PARA INICIAR PROCESO DE PYTHON """
        self.thread_init=Thread(target=self.sondeaVarPLC)
        self.thread_init.start()
        """ Creamos un timer que actualiza la linea del terminal """
        self.timer_updateTerminalLabel=QTimer()
        self.timer_updateTerminalLabel.timeout.connect(self.updateTerminalLabel)
        self.timer_updateTerminalLabel.start(100)
        """ Realizamos la conexión con el PLC """
        if FLAG_PLC_AVALABLE:
            #CONEXIÓN
            self.plc = snap7.client.Client()
            self.plc.connect(IP, RACK, SLOT)
            #LECTURA DEL BLOQUE DE DATOS DEL PLC
            self.sdb = self.plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

    def writeBool(self,db_number, start_offset, bit_offset, value): 
        reading = self.plc.db_read(db_number, start_offset, 1)    
        snap7.util.set_bool(reading, 0, bit_offset, value)   
        self.plc.db_write(db_number, start_offset, reading)       

    def updateTerminalLabel(self):
        if not self._FLAG_initProcess:
            return
        self.ui.plainTextEdit_peso.setPlainText("{:.4f}".format(self.Peso))
        self.Param1="{}".format(self.ui.plainTextEdit_param1.toPlainText())
        self.Param2="{}".format(self.ui.plainTextEdit_param2.toPlainText())
        self.Param3="{}".format(self.ui.plainTextEdit_param3.toPlainText())
        self.Param4="{}".format(self.ui.plainTextEdit_param4.toPlainText())
        self.Param5="{}".format(self.ui.plainTextEdit_param5.toPlainText())
        nuevoText="{}\n[INFO] idCaja: {}\tPeso: {:.4f}\tParam1: {}\tParam2: {}\tParam3: {}\tParam4: {}\tParam5: {}\tDecision:{}".format(self.oldText,self.idCaja,self.Peso,self.Param1,self.Param2,self.Param3,self.Param4,self.Param5,self.Decision)
        self.ui.plainTextEdit_terminal.setPlainText(nuevoText)
        
    def sondeaVarPLC(self):
        if FLAG_PLC_AVALABLE:
            """"""""""""""""""""""""""""""""""""""""""""""""""""""
            """"""""""""""""""""""""""""""""""""""""""""""""""""""
            while True:
                print("wait for peso in PLC")
                time.sleep(1)
            #LECTURA DEL PESO
            self.Peso = self.db[514:515].decode('UTF-8').strip('\x00')
            """"""""""""""""""""""""""""""""""""""""""""""""""""""
            """"""""""""""""""""""""""""""""""""""""""""""""""""""
        else:
            time.sleep(2)
            self.Peso+=0.1
            self.idCaja+=1
        self._FLAG_initProcess=True
        self.oldText=self.ui.plainTextEdit_terminal.toPlainText()
        
    def der_pressed(self):
        if not (self._FLAG_initProcess):
            return
        self.Decision="Derecha"
        
    def izq_pressed(self):
        if not (self._FLAG_initProcess):
            return
        self.Decision="Izquierda"
        
    def digDEL_pressed(self):
        if not (self._FLAG_initProcess):
            return
        
        if self.ui.radioButton_param1.isChecked():
            id=1
        elif self.ui.radioButton_param2.isChecked():
            id=2
        elif self.ui.radioButton_param3.isChecked():
            id=3
        elif self.ui.radioButton_param4.isChecked():
            id=4
        elif self.ui.radioButton_param5.isChecked():
            id=5
        pythonCommand="self.ui.plainTextEdit_param{}.setPlainText(\"\")".format(id)
        eval(pythonCommand)
            
    def digOK_pressed(self):
        if not (self._FLAG_initProcess):
            return
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""
        """"""""""""""""""""""""""""""""""""""""""""""""""""""
        """ Soltamos al PLC para continuar con el bucle """
        if FLAG_PLC_AVALABLE:
            self.writeBool(DB_NUMBER, 258, 0, value)
        """"""""""""""""""""""""""""""""""""""""""""""""""""""
        """"""""""""""""""""""""""""""""""""""""""""""""""""""
        
        ## Reiniciamos los valores
        self.Param1=None
        self.Param2=None
        self.Param3=None
        self.Param4=None
        self.Param5=None
        self.Decision=None
        ## Limpiamos los plainText
        self.ui.plainTextEdit_param1.setPlainText("")
        self.ui.plainTextEdit_param2.setPlainText("")
        self.ui.plainTextEdit_param3.setPlainText("")
        self.ui.plainTextEdit_param4.setPlainText("")
        self.ui.plainTextEdit_param5.setPlainText("")
        self.ui.plainTextEdit_peso.setPlainText("")        
        ## Reiniciamos las variables _FLAG
        self._FLAG_initProcess=False
        ## iniciamos el Hilos nuevamente
        self.thread_init=Thread(target=self.sondeaVarPLC)
        self.thread_init.start()
        
    def dig0_pressed(self):
        self.writeDigito(0)
    def dig1_pressed(self):
        self.writeDigito(1)
    def dig2_pressed(self):
        self.writeDigito(2)
    def dig3_pressed(self):
        self.writeDigito(3)
    def dig4_pressed(self):
        self.writeDigito(4)
    def dig5_pressed(self):
        self.writeDigito(5)
    def dig6_pressed(self):
        self.writeDigito(6)
    def dig7_pressed(self):
        self.writeDigito(7)
    def dig8_pressed(self):
        self.writeDigito(8)
    def dig9_pressed(self):
        self.writeDigito(9)
    
        
    def writeDigito(self,dig):
        if not (self._FLAG_initProcess):
            return
        
        if self.ui.radioButton_param1.isChecked():
            id=1
        elif self.ui.radioButton_param2.isChecked():
            id=2
        elif self.ui.radioButton_param3.isChecked():
            id=3
        elif self.ui.radioButton_param4.isChecked():
            id=4
        elif self.ui.radioButton_param5.isChecked():
            id=5
        pythonCommand="self.ui.plainTextEdit_param{}.setPlainText(self.ui.plainTextEdit_param{}.toPlainText()+\"{}\")".format(id,id,dig)
        eval(pythonCommand)
       

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
    
