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
        
        self.Button_emergencia = QtWidgets.QPushButton(self.centralwidget)
        self.Button_emergencia.setGeometry(QtCore.QRect(90, 760, 61, 71))
        self.Button_emergencia.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.Button_emergencia.setText("")
        self.Button_emergencia.setObjectName("Button_emergencia")
        
        self.Button_parada = QtWidgets.QPushButton(self.centralwidget)
        self.Button_parada.setGeometry(QtCore.QRect(280, 760, 61, 71))
        self.Button_parada.setObjectName("Button_parada")
        
        self.Button_inicio = QtWidgets.QPushButton(self.centralwidget)
        self.Button_inicio.setGeometry(QtCore.QRect(400, 760, 61, 71))
        self.Button_inicio.setObjectName("Button_inicio")
        
        self.Button_confirmacion = QtWidgets.QPushButton(self.centralwidget)
        self.Button_confirmacion.setGeometry(QtCore.QRect(520, 760, 61, 71))
        self.Button_confirmacion.setObjectName("Button_confirmacion")
        
        self.Button_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.Button_usuario.setGeometry(QtCore.QRect(240, 30, 31, 21))
        self.Button_usuario.setText("")
        self.Button_usuario.setObjectName("Button_usuario")
        
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setGeometry(QtCore.QRect(280, 30, 67, 17))
        self.label_usuario.setObjectName("label_usuario")
        self.label_fecha = QtWidgets.QLabel(self.centralwidget)
        self.label_fecha.setGeometry(QtCore.QRect(560, 30, 67, 17))
        self.label_fecha.setObjectName("label_fecha")
        self.label_CicloRobot = QtWidgets.QLabel(self.centralwidget)
        self.label_CicloRobot.setGeometry(QtCore.QRect(220, 171, 117, 17))
        self.label_CicloRobot.setObjectName("label_CicloRobot")
        ##
        self.led_iniciaCicloRobot = QtWidgets.QPushButton(self.centralwidget)
        self.led_iniciaCicloRobot.setGeometry(QtCore.QRect(181, 166, 29, 25))
        self.led_iniciaCicloRobot.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_iniciaCicloRobot.setText("")
        self.led_iniciaCicloRobot.setObjectName("led_iniciaCicloRobot")
        ##
        self.label_PresenciaCaja = QtWidgets.QLabel(self.centralwidget)
        self.label_PresenciaCaja.setGeometry(QtCore.QRect(220, 218, 98, 17))
        self.label_PresenciaCaja.setObjectName("label_PresenciaCaja")
        ##
        self.led_PresenciaCaja = QtWidgets.QPushButton(self.centralwidget)
        self.led_PresenciaCaja.setGeometry(QtCore.QRect(181, 212, 29, 25))
        self.led_PresenciaCaja.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_PresenciaCaja.setText("")
        self.led_PresenciaCaja.setObjectName("led_PresenciaCaja")
        ##
        self.led_Cara2 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Cara2.setGeometry(QtCore.QRect(181, 304, 29, 25))
        self.led_Cara2.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Cara2.setText("")
        self.led_Cara2.setObjectName("led_Cara2")
        ##
        self.label_PasaCara1 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara1.setGeometry(QtCore.QRect(220, 264, 100, 17))
        self.label_PasaCara1.setObjectName("label_PasaCara1")
        ##
        self.led_Cara1 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Cara1.setGeometry(QtCore.QRect(181, 258, 29, 25))
        self.led_Cara1.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Cara1.setText("")
        self.led_Cara1.setObjectName("led_Cara1")
        ##
        self.led_Cara3 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Cara3.setGeometry(QtCore.QRect(181, 350, 29, 25))
        self.led_Cara3.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Cara3.setText("")
        self.led_Cara3.setObjectName("led_Cara3")
        ##
        self.led_Cara4 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Cara4.setGeometry(QtCore.QRect(181, 396, 29, 25))
        self.led_Cara4.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Cara4.setText("")
        self.led_Cara4.setObjectName("led_Cara4")
        ##
        self.label_ParIzq = QtWidgets.QLabel(self.centralwidget)
        self.label_ParIzq.setGeometry(QtCore.QRect(20, 120, 111, 17))
        self.label_ParIzq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ParIzq.setObjectName("label_ParIzq")
        ##
        self.label_ParDer = QtWidgets.QLabel(self.centralwidget)
        self.label_ParDer.setGeometry(QtCore.QRect(260, 120, 121, 17))
        self.label_ParDer.setObjectName("label_ParDer")
        ##
        self.label_PasaCara2 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara2.setGeometry(QtCore.QRect(220, 311, 94, 17))
        self.label_PasaCara2.setObjectName("label_PasaCara2")
        ##
        self.label_PasaCara3 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara3.setGeometry(QtCore.QRect(220, 357, 100, 17))
        self.label_PasaCara3.setObjectName("label_PasaCara3")
        ##
        self.label_PasaCara4 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara4.setGeometry(QtCore.QRect(220, 404, 92, 17))
        self.label_PasaCara4.setObjectName("label_PasaCara4")
        ##
        self.label_PasaPeso = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaPeso.setGeometry(QtCore.QRect(220, 450, 68, 17))
        self.label_PasaPeso.setObjectName("label_PasaPeso")
        ##
        self.led_Peso = QtWidgets.QPushButton(self.centralwidget)
        self.led_Peso.setGeometry(QtCore.QRect(181, 442, 29, 25))
        self.led_Peso.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Peso.setText("")
        self.led_Peso.setObjectName("led_Peso")
        ##
        self.led_Imprime = QtWidgets.QPushButton(self.centralwidget)
        self.led_Imprime.setGeometry(QtCore.QRect(181, 488, 29, 25))
        self.led_Imprime.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Imprime.setText("")
        self.led_Imprime.setObjectName("led_Imprime")
        ##
        self.label_Imprime = QtWidgets.QLabel(self.centralwidget)
        self.label_Imprime.setGeometry(QtCore.QRect(220, 497, 118, 17))
        self.label_Imprime.setObjectName("label_Imprime")
        ##
        self.label_PasaCara4_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara4_2.setGeometry(QtCore.QRect(220, 543, 92, 17))
        self.label_PasaCara4_2.setObjectName("label_PasaCara4_2")
        ## Led Cara5
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara5 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara5.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara5.setGeometry(QtCore.QRect(181, 534, 29, 25))
        self.led_Cara5.setObjectName("led_Cara5")
        ## Led Cara6
        image = QtGui.QImage(HEADER_PATH+'resources/green-led-off.png')
        image=image.scaled(29, 25,QtCore.Qt.KeepAspectRatio)
        self.led_Cara6 = QtWidgets.QLabel(self.centralwidget)
        self.led_Cara6.setPixmap(QtGui.QPixmap.fromImage(image))
        self.led_Cara6.setGeometry(QtCore.QRect(181, 580, 29, 25))
        self.led_Cara6.setObjectName("led_Cara6")
        ##
        self.label_PasaCara4_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_PasaCara4_3.setGeometry(QtCore.QRect(220, 590, 92, 17))
        self.label_PasaCara4_3.setObjectName("label_PasaCara4_3")
        ##
        self.label_fecha_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_fecha_2.setGeometry(QtCore.QRect(480, 590, 131, 17))
        self.label_fecha_2.setObjectName("label_fecha_2")
        ##
        self.label_Alarma1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Alarma1.setGeometry(QtCore.QRect(520, 160, 131, 17))
        self.label_Alarma1.setObjectName("label_Alarma1")
        ##
        self.led_Alarma1 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Alarma1.setGeometry(QtCore.QRect(480, 150, 31, 31))
        self.led_Alarma1.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Alarma1.setText("")
        self.led_Alarma1.setObjectName("led_Alarma1")
        ##
        self.label_Alarma2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Alarma2.setGeometry(QtCore.QRect(520, 210, 131, 17))
        self.label_Alarma2.setObjectName("label_Alarma2")
        ##
        self.led_Alarma2 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Alarma2.setGeometry(QtCore.QRect(480, 200, 31, 31))
        self.led_Alarma2.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Alarma2.setText("")
        self.led_Alarma2.setObjectName("led_Alarma2")
        ##
        self.label_Alarma3 = QtWidgets.QLabel(self.centralwidget)
        self.label_Alarma3.setGeometry(QtCore.QRect(520, 260, 131, 17))
        self.label_Alarma3.setObjectName("label_Alarma3")
        ##
        self.led_Alarma3 = QtWidgets.QPushButton(self.centralwidget)
        self.led_Alarma3.setGeometry(QtCore.QRect(480, 250, 31, 31))
        self.led_Alarma3.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_Alarma3.setText("")
        self.led_Alarma3.setObjectName("led_Alarma3")
        ##
        self.led_ParIzq = QtWidgets.QPushButton(self.centralwidget)
        self.led_ParIzq.setGeometry(QtCore.QRect(140, 120, 29, 25))
        self.led_ParIzq.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_ParIzq.setText("")
        self.led_ParIzq.setObjectName("led_ParIzq")
        ##
        self.led_ParDer = QtWidgets.QPushButton(self.centralwidget)
        self.led_ParDer.setGeometry(QtCore.QRect(220, 120, 29, 25))
        self.led_ParDer.setStyleSheet("background-color: rgb(239, 0, 0);")
        self.led_ParDer.setText("")
        self.led_ParDer.setObjectName("led_ParDer")
        ##
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(600, 580, 61, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        GUI_IQFARMA.setCentralWidget(self.centralwidget)
        ##
        self.menubar = QtWidgets.QMenuBar(GUI_IQFARMA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 22))
        self.menubar.setObjectName("menubar")
        GUI_IQFARMA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI_IQFARMA)
        self.statusbar.setObjectName("statusbar")
        GUI_IQFARMA.setStatusBar(self.statusbar)

        self.retranslateUi(GUI_IQFARMA)
        QtCore.QMetaObject.connectSlotsByName(GUI_IQFARMA)

    def retranslateUi(self, GUI_IQFARMA):
        _translate = QtCore.QCoreApplication.translate
        GUI_IQFARMA.setWindowTitle(_translate("GUI_IQFARMA", "GUI_IQFARMA"))
        self.Button_parada.setText(_translate("GUI_IQFARMA", "O"))
        self.Button_inicio.setText(_translate("GUI_IQFARMA", "I"))
        self.Button_confirmacion.setText(_translate("GUI_IQFARMA", "C"))
        self.label_usuario.setText(_translate("GUI_IQFARMA", "user: "))
        self.label_fecha.setText(_translate("GUI_IQFARMA", "Fecha"))
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
        self.label_PasaCara4_2.setText(_translate("GUI_IQFARMA", "Pasa 5ta Cara"))
        self.label_PasaCara4_3.setText(_translate("GUI_IQFARMA", "Pasa 6ta Cara"))
        self.label_fecha_2.setText(_translate("GUI_IQFARMA", "Contador Cajas:"))
        self.label_Alarma1.setText(_translate("GUI_IQFARMA", "Alarma 1"))
        self.label_Alarma2.setText(_translate("GUI_IQFARMA", "Alarma 2"))
        self.label_Alarma3.setText(_translate("GUI_IQFARMA", "Alarma 3"))
