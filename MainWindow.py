# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
## libreria para obtener el path
import pathlib
HEADER_PATH=str(pathlib.Path(__file__).parent.resolve())+"/"#+"../../"

class Ui_GUI_IQFARMA(object):
    def setupUi(self, GUI_IQFARMA):
        GUI_IQFARMA.setObjectName("GUI_IQFARMA")
        GUI_IQFARMA.resize(789, 878)
        self.centralwidget = QtWidgets.QWidget(GUI_IQFARMA)
        self.centralwidget.setObjectName("centralwidget")
        ## Boton emergencia
        self.Button_emergencia = QtWidgets.QPushButton(self.centralwidget)
        self.Button_emergencia.setGeometry(QtCore.QRect(90, 760, 61, 71))
        self.Button_emergencia.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.Button_emergencia.setText("")
        self.Button_emergencia.setObjectName("Button_emergencia")
        ## Boton parada
        self.Button_parada = QtWidgets.QPushButton(self.centralwidget)
        self.Button_parada.setGeometry(QtCore.QRect(280, 760, 61, 71))
        self.Button_parada.setObjectName("Button_parada")
        ## Boton Inicio
        self.Button_inicio = QtWidgets.QPushButton(self.centralwidget)
        self.Button_inicio.setGeometry(QtCore.QRect(400, 760, 61, 71))
        self.Button_inicio.setObjectName("Button_inicio")
        ## Boton confirmación
        self.Button_confirmacion = QtWidgets.QPushButton(self.centralwidget)
        self.Button_confirmacion.setGeometry(QtCore.QRect(520, 760, 61, 71))
        self.Button_confirmacion.setObjectName("Button_confirmacion")
        ## Estado del sistema
        self.label_estado = QtWidgets.QLabel(self.centralwidget)
        self.label_estado.setGeometry(QtCore.QRect(40, 30, 207, 17))
        self.label_estado.setObjectName("label_estado")
        ## Fecha 
        self.label_fecha = QtWidgets.QLabel(self.centralwidget)
        self.label_fecha.setGeometry(QtCore.QRect(480, 30, 207, 17))
        self.label_fecha.setObjectName("label_fecha")
        """USUARIO widgets"""
        ## Boton usuario
        self.Button_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.Button_usuario.setGeometry(QtCore.QRect(220, 30, 31, 21))
        self.Button_usuario.setText("")
        self.Button_usuario.setObjectName("Button_usuario")
        self.Button_usuario.setIcon(QtGui.QIcon(HEADER_PATH+'resources/userIcon.png'))
        ## Label usuario
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setGeometry(QtCore.QRect(260, 30, 167, 17))
        self.label_usuario.setObjectName("label_usuario")
        """Parihuela_Izquierda Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_ParIzq = QtWidgets.QLabel(self.centralwidget)
        self.led_ParIzq.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_ParIzq.setGeometry(QtCore.QRect(140, 120, 29, 25))
        self.led_ParIzq.setObjectName("led_ParIzq")
        ## Label
        self.label_ParIzq = QtWidgets.QLabel(self.centralwidget)
        self.label_ParIzq.setGeometry(QtCore.QRect(20, 120, 111, 17))
        self.label_ParIzq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ParIzq.setObjectName("label_ParIzq")
        """Parihuela_Izquierda Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_ParDer = QtWidgets.QLabel(self.centralwidget)
        self.led_ParDer.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_ParDer.setGeometry(QtCore.QRect(220, 120, 29, 25))
        self.led_ParDer.setObjectName("led_ParDer")
        ## Label
        self.label_ParDer = QtWidgets.QLabel(self.centralwidget)
        self.label_ParDer.setGeometry(QtCore.QRect(260, 120, 121, 17))
        self.label_ParDer.setObjectName("label_ParDer")
        """Inicia_Ciclo_Robot Widgets"""
        ## Led 
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_iniciaCicloRobot = QtWidgets.QLabel(self.centralwidget)
        self.led_iniciaCicloRobot.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_iniciaCicloRobot.setGeometry(QtCore.QRect(181, 166, 29, 25))
        self.led_iniciaCicloRobot.setObjectName("led_iniciaCicloRobot")
        ## Label
        self.label_CicloRobot = QtWidgets.QLabel(self.centralwidget)
        self.label_CicloRobot.setGeometry(QtCore.QRect(220, 171, 117, 17))
        self.label_CicloRobot.setObjectName("label_CicloRobot")
        """Presencia_Caja Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_PresenciaCaja = QtWidgets.QLabel(self.centralwidget)
        self.led_PresenciaCaja.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_PresenciaCaja.setGeometry(QtCore.QRect(181, 212, 29, 25))
        self.led_PresenciaCaja.setObjectName("led_PresenciaCaja")
        ## Label
        self.label_PresenciaCaja = QtWidgets.QLabel(self.centralwidget)
        self.label_PresenciaCaja.setGeometry(QtCore.QRect(220, 218, 98, 17))
        self.label_PresenciaCaja.setObjectName("label_PresenciaCaja")
        """Cara1 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara1 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara1.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara1.setGeometry(QtCore.QRect(181, 258, 29, 25))
        self.led_Cara1.setObjectName("led_Cara1")
        ## Label
        self.label_PasaCara1 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara1.setGeometry(QtCore.QRect(220, 264, 100, 17))
        self.label_PasaCara1.setObjectName("label_PasaCara1")
        """Cara2 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara2 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara2.setGeometry(QtCore.QRect(181, 304, 29, 25))
        self.led_Cara2.setObjectName("led_Cara2")
        ## Label
        self.label_PasaCara2 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara2.setGeometry(QtCore.QRect(220, 311, 94, 17))
        self.label_PasaCara2.setObjectName("label_PasaCara2")
        """Cara3 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara3 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara3.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara3.setGeometry(QtCore.QRect(181, 350, 29, 25))
        self.led_Cara3.setObjectName("led_Cara3")
         ## Label
        self.label_PasaCara3 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara3.setGeometry(QtCore.QRect(220, 357, 100, 17))
        self.label_PasaCara3.setObjectName("label_PasaCara3")
        """Cara4 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara4 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara4.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara4.setGeometry(QtCore.QRect(181, 396, 29, 25))
        self.led_Cara4.setObjectName("led_Cara4")
        ## Label
        self.label_PasaCara4 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara4.setGeometry(QtCore.QRect(220, 404, 92, 17))
        self.label_PasaCara4.setObjectName("label_PasaCara4")
        """Cara5 Widgets"""
        ## Label
        self.label_PasaCara5 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara5.setGeometry(QtCore.QRect(220, 543, 92, 17))
        self.label_PasaCara5.setObjectName("label_PasaCara5")
        ## Led 
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara5 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara5.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara5.setGeometry(QtCore.QRect(181, 534, 29, 25))
        self.led_Cara5.setObjectName("led_Cara5")
        """Cara6 Widgets"""
        ## Led 
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara6 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara6.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara6.setGeometry(QtCore.QRect(181, 580, 29, 25))
        self.led_Cara6.setObjectName("led_Cara6")
        ## Label
        self.label_PasaCara6 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara6.setGeometry(QtCore.QRect(220, 590, 92, 17))
        self.label_PasaCara6.setObjectName("label_PasaCara6")
        """Peso Widgets"""
        ## Label
        self.label_PasaPeso = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaPeso.setGeometry(QtCore.QRect(220, 450, 68, 17))
        self.label_PasaPeso.setObjectName("label_PasaPeso")
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Peso = QtWidgets.QLabel(self.centralwidget)
        self.led_Peso.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Peso.setGeometry(QtCore.QRect(181, 442, 29, 25))
        self.led_Peso.setObjectName("led_Peso")
        """Imprime Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Imprime = QtWidgets.QLabel(self.centralwidget)
        self.led_Imprime.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Imprime.setGeometry(QtCore.QRect(181, 488, 29, 25))
        self.led_Imprime.setObjectName("led_Imprime")
        ## Label
        self.label_Imprime = QtWidgets.QLabel(self.centralwidget)
        self.label_Imprime.setGeometry(QtCore.QRect(220, 497, 118, 17))
        self.label_Imprime.setObjectName("label_Imprime")
        """Contador_Cajas Widgets"""
        ## Label
        self.label_contador = QtWidgets.QLabel(self.centralwidget)
        self.label_contador.setGeometry(QtCore.QRect(480, 590, 131, 17))
        self.label_contador.setObjectName("label_contador")
        """Alarma1 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/amber-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Alarma1 = QtWidgets.QLabel(self.centralwidget)
        self.led_Alarma1.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Alarma1.setGeometry(QtCore.QRect(480, 150, 31, 31))
        self.led_Alarma1.setObjectName("led_Alarma1")
        ## Label
        self.label_Alarma1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Alarma1.setGeometry(QtCore.QRect(520, 160, 131, 17))
        self.label_Alarma1.setObjectName("label_Alarma1")
        """Alarma2 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/amber-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Alarma2 = QtWidgets.QLabel(self.centralwidget)
        self.led_Alarma2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Alarma2.setGeometry(QtCore.QRect(480, 200, 31, 31))
        self.led_Alarma2.setObjectName("led_Alarma2")
        ## Label
        self.label_Alarma2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Alarma2.setGeometry(QtCore.QRect(520, 210, 131, 17))
        self.label_Alarma2.setObjectName("label_Alarma2")
        """Alarma3 Widgets"""
        ## Led
        image = QtGui.QImage(HEADER_PATH+'resources/amber-led-on.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Alarma3 = QtWidgets.QLabel(self.centralwidget)
        self.led_Alarma3.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Alarma3.setGeometry(QtCore.QRect(480, 250, 31, 31))
        self.led_Alarma3.setObjectName("led_Alarma3")
        ## Label
        self.label_Alarma3 = QtWidgets.QLabel(self.centralwidget)
        self.label_Alarma3.setGeometry(QtCore.QRect(520, 260, 131, 17))
        self.label_Alarma3.setObjectName("label_Alarma3")
        ## Contador
        self.plainTextEdit_contador = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_contador.setGeometry(QtCore.QRect(600, 580, 61, 31))
        self.plainTextEdit_contador.setObjectName("plainTextEdit")
        self.plainTextEdit_contador.setReadOnly(True)
        self.plainTextEdit_contador.setPlainText("0")
        ## Configuramos
        GUI_IQFARMA.setCentralWidget(self.centralwidget)
        # ## Configuramos la barra de menu
        # self.menubar = QtWidgets.QMenuBar(GUI_IQFARMA)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 22))
        # self.menubar.setObjectName("menubar")
        
        # GUI_IQFARMA.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(GUI_IQFARMA)
        # self.statusbar.setObjectName("statusbar")
        # GUI_IQFARMA.setStatusBar(self.statusbar)
        
        ## Añadimos el Texto
        self.retranslateUi(GUI_IQFARMA)
        QtCore.QMetaObject.connectSlotsByName(GUI_IQFARMA)

    def retranslateUi(self, GUI_IQFARMA):
        _translate = QtCore.QCoreApplication.translate
        GUI_IQFARMA.setWindowTitle(_translate("GUI_IQFARMA", "GUI_IQFARMA"))
        self.Button_parada.setText(_translate("GUI_IQFARMA", "O"))
        self.Button_inicio.setText(_translate("GUI_IQFARMA", "I"))
        self.Button_confirmacion.setText(_translate("GUI_IQFARMA", "C"))
        self.label_usuario.setText(_translate("GUI_IQFARMA", ""))
        self.label_estado.setText(_translate("GUI_IQFARMA", "Estado: Detenido"))
        self.label_fecha.setText(_translate("GUI_IQFARMA", "Fecha: "))
        self.label_CicloRobot.setText(_translate("GUI_IQFARMA", "Inicia Ciclo Robot"))
        self.label_PresenciaCaja.setText(_translate("GUI_IQFARMA", "Presencia Caja"))
        self.label_PasaCara1.setText(_translate("GUI_IQFARMA", "Pasa 1era Cara"))
        self.label_ParIzq.setText(_translate("GUI_IQFARMA", "Parihuela Izq"))
        self.label_ParDer.setText(_translate("GUI_IQFARMA", "Parihuela Der"))
        self.label_PasaCara2.setText(_translate("GUI_IQFARMA", "Pasa 2da Cara"))
        self.label_PasaCara3.setText(_translate("GUI_IQFARMA", "Pasa 3era Cara"))
        self.label_PasaCara4.setText(_translate("GUI_IQFARMA", "Pasa 4ta Cara"))
        self.label_PasaPeso.setText(_translate("GUI_IQFARMA", "Pasa Peso"))
        self.label_Imprime.setText(_translate("GUI_IQFARMA", "Imprime Etiqueta"))
        self.label_PasaCara5.setText(_translate("GUI_IQFARMA", "Pasa 5ta Cara"))
        self.label_PasaCara6.setText(_translate("GUI_IQFARMA", "Pasa 6ta Cara"))
        self.label_contador.setText(_translate("GUI_IQFARMA", "Contador Cajas:"))
        self.label_Alarma1.setText(_translate("GUI_IQFARMA", "Alarma 1"))
        self.label_Alarma2.setText(_translate("GUI_IQFARMA", "Alarma 2"))
        self.label_Alarma3.setText(_translate("GUI_IQFARMA", "Alarma 3"))
