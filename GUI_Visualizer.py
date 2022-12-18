from MainWindow import Ui_GUI_IQFARMA,HEADER_PATH

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QImage,QPixmap

import sys 
import pandas as pd ## Libreria para leer archivo csv
import logging ## Libreria para info Logging
from datetime import datetime ## Linreria para obtener fecha

"""Variables globales"""
userData=[]
   
""" 
//////////////////////////////////////////
//            MAIN CLASS GUI            //
//////////////////////////////////////////
"""
class GUI(QtWidgets.QMainWindow):
    def __init__(self):    
        QtWidgets.QMainWindow.__init__(self)
        ## Creamos nuestra GUI
        self.ui = Ui_GUI_IQFARMA()
        self.ui.setupUi(self)    
        ## creamos variables
        self.list_leds_widgets=[self.ui.led_ParIzq,self.ui.led_ParDer,self.ui.led_iniciaCicloRobot,self.ui.led_PresenciaCaja,self.ui.led_Cara1,self.ui.led_Cara2,self.ui.led_Cara3,self.ui.led_Cara4,self.ui.led_Peso,self.ui.led_Imprime,self.ui.led_Cara5,self.ui.led_Cara6]
        self.idLedState=0
        self.counterCajas=115
        ## Creamos Flags
        self.flagActiveUser = False
        self.flagCara1=False
        self.flagOperando=False
        ## Conectamos botones con las funciones
        self.ui.Button_emergencia.pressed.connect(self.button_emergencia_pressed)
        self.ui.Button_inicio.pressed.connect(self.button_inicio_pressed)
        self.ui.Button_parada.pressed.connect(self.button_parada_pressed)
        self.ui.Button_confirmacion.pressed.connect(self.button_confirmacion_pressed)
        self.ui.Button_usuario.pressed.connect(self.button_usuario_pressed)
        ## Cretamos Qtimers para evitar atasco en el constructor de la GUI
        self.timerUpdateDate=QTimer()
        self.timerUpdateDate.timeout.connect(self.updateDate)
        self.timerUpdateDate.start(500)
        ## Cretamos Qtimers para evitar atasco en el constructor de la GUI
        self.timerTest=QTimer()
        self.timerTest.timeout.connect(self.test)
        
    """Timers Functions"""
    def updateDate(self):
        try:
            self.ui.label_fecha.setText(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
        except KeyboardInterrupt:
            self.close()
            
    def test(self):
        if self.idLedState==len(self.list_leds_widgets):
            ## Resetamos los leds
            self.counterCajas+=1
            self.idLedState=0
            image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
            image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)    
            for led in self.list_leds_widgets:
                led.setPixmap(QtGui.QPixmap.fromImage(image))
            self.ui.plainTextEdit_contador.setPlainText(str(self.counterCajas))
            return            
        led=self.list_leds_widgets[self.idLedState]
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-on.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)    
        led.setPixmap(QtGui.QPixmap.fromImage(image))
        self.idLedState+=1          
        
    
    """Buttons pressed Functions"""
    def button_emergencia_pressed(self):
        if not(self.flagActiveUser):
            return
        self.ui.label_estado.setText("Estado: Detenido")
        ## Put some code here
        self.timerTest.stop()
        
    def button_parada_pressed(self):
        if not(self.flagActiveUser):
            return
        self.ui.label_estado.setText("Estado: Detenido")
        ## Put some code here
        self.timerTest.stop()
        
    def button_inicio_pressed(self):
        if not(self.flagActiveUser):
            return
        self.ui.label_estado.setText("Estado: Operando")
        self.timerTest.start(250)
        ## Put some code here
        
    def button_confirmacion_pressed(self):
        if not(self.flagActiveUser):
            return
        ## Put some code here
        
    ## Funciones de Dialog
    def button_usuario_pressed(self):
        dlg = UsuarioDialogBox(self)
        dlg.show()
    
    
    """Update State Functions"""    
    def FuncionTimer1(self):
        1
        
""" 
//////////////////////////////////////////
//            Dialog USUARIO            //
//////////////////////////////////////////
"""
class UsuarioDialogBox(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(UsuarioDialogBox,self).__init__(parent)
        self.setWindowTitle("Ingrese Usuario")
        ## Creo el layout de nuestra ventana (vertical)
        layout=QtWidgets.QVBoxLayout()
        """Creamos los textEdit de Usuario y password"""
        layoutUserPass=QtWidgets.QFormLayout()
        ## Creo el label usuario
        self.text_user=QtWidgets.QLineEdit()
        layoutUserPass.addRow("Usuario: ",self.text_user)
        ## Creo el label password
        self.text_pass=QtWidgets.QLineEdit()
        layoutUserPass.addRow("Password: ",self.text_pass)
        """Creamos los botones Accept y close"""
        layoutButtons=QtWidgets.QVBoxLayout()
        ## Creo el boton OK y Cancel
        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layoutButtons.addWidget(buttonBox)
        """Juntamos los layouts"""
        layout.addLayout(layoutUserPass)
        layout.addLayout(layoutButtons)
        self.setLayout(layout)
    
    def accept(self):
        users=userData[:,0]
        passwords=userData[:,1]
        if self.text_user.text() in users and self.text_pass.text() in passwords:
            logging.info("Usuario registrado")
            parent=self.parent()
            parent.ui.label_usuario.setText(self.text_user.text())
            parent.flagActiveUser=True
        self.close()
""" //////////////////////////////////////////
    //                Main                  //
    //////////////////////////////////////////
"""
def setUpGUI():
    global userData
    userData=pd.read_csv("users.csv",dtype="string").to_numpy()
    ## Creamos formato Lgging
    FORMAT = '%(asctime)s - %(levelname)s - (%(filename)s:%(lineno)d): %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    ## Creamos la app
    app = QtWidgets.QApplication(sys.argv)  
    #Creamos el visualizador
    GUI_window=GUI()
    GUI_window.show()                        
    sys.exit(app.exec_())
    