from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import random
from gtts import gTTS
import os
from playsound import playsound
import speech_recognition as sr

class Ui_V_Assistant():
    def setupUi(self, V_Assistant):
        V_Assistant.setObjectName("V_Assistant")
        V_Assistant.resize(812, 607)
        V_Assistant.setStyleSheet("background-image: url(:/bg/BG.jpg);")
        self.centralwidget = QtWidgets.QWidget(V_Assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.headingg = QtWidgets.QTextEdit(self.centralwidget)
        self.headingg.setGeometry(QtCore.QRect(230, 20, 391, 51))
        self.headingg.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.headingg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headingg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.headingg.setLineWidth(0)
        self.headingg.setReadOnly(True)
        self.headingg.setObjectName("headingg")
        self.lang_select = QtWidgets.QComboBox(self.centralwidget)
        self.lang_select.setGeometry(QtCore.QRect(580, 280, 181, 31))
        self.lang_select.setEditable(False)
        self.lang_select.setObjectName("lang_select")
        self.lang_select.addItem("")
        self.lang_select.addItem("")
        self.lang_select.addItem("")
        self.lang_select.addItem("")
        self.lang_select.addItem("")
        self.lang_select.addItem("")
        self.mic_button = QtWidgets.QPushButton(self.centralwidget)
        self.mic_button.clicked.connect(self.call)
        self.mic_button.setGeometry(QtCore.QRect(340, 210, 171, 191))
        self.mic_button.setStyleSheet("background-image: url(:/micc/mic.jpg);")
        self.mic_button.setText("")
        self.mic_button.setObjectName("mic_button")
        self.help = QtWidgets.QTextEdit(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(590, 490, 211, 51))
        self.help.setReadOnly(False)
        self.help.setObjectName("help")
        self.link1 = QtWidgets.QPushButton(self.centralwidget)
        self.link1.clicked.connect(self.open_webbrowser1)
        self.link1.setText("Link 1")
        self.link1.setGeometry(670, 560 , 60, 40)
        self.link2 = QtWidgets.QPushButton(self.centralwidget)
        self.link2.setText("Link 2")
        self.link2.clicked.connect(self.open_webbrowser2)
        self.link2.setGeometry(740, 560, 60, 40)

        V_Assistant.setCentralWidget(self.centralwidget)

        self.retranslateUi(V_Assistant)
        self.lang_select.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(V_Assistant)

    def open_webbrowser1(self):
        webbrowser.open('https://www.cropscience.bayer.in/Sustainable-Crop-Solutions/National-Helpline-for-Farmers.aspx')
    def open_webbrowser2(self):
        webbrowser.open('https://farmer.gov.in/')
    def retranslateUi(self, V_Assistant):
        _translate = QtCore.QCoreApplication.translate
        V_Assistant.setWindowTitle(_translate("V_Assistant", "Farmer Voice Assistant"))
        self.headingg.setHtml(_translate("V_Assistant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">FARMER VOICE ASSISTANT</span></p></body></html>"))
        self.lang_select.setCurrentText(_translate("V_Assistant", "Select Language"))
        self.lang_select.setItemText(0, _translate("V_Assistant", "Select Language"))
        self.lang_select.setItemText(1, _translate("V_Assistant", "Hindi"))
        self.lang_select.setItemText(2, _translate("V_Assistant", "Telugu"))
        self.lang_select.setItemText(3, _translate("V_Assistant", "Tamil"))
        self.lang_select.setItemText(4, _translate("V_Assistant", "Bengali"))
        self.lang_select.setItemText(5, _translate("V_Assistant", "English"))
        self.help.setHtml(_translate("V_Assistant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Helpline Number- 18002006321</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Website Help-</span></p></body></html>"))


    def talkToMe(self, audio):

        print(audio)
        self.r1 = random.randint(1, 10000000)
        self.r2 = random.randint(1, 10000000)

        self.randfile = str(self.r2) + "randomtext" + str(self.r1) + ".mp3"

        self.tts = gTTS(text=audio, lang='en', slow=False)
        self.tts.save(self.randfile)
        playsound(self.randfile)

        print(self.randfile)
        os.remove(self.randfile)


    def myCommand(self):

        self.r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Ready...')
            self.r.pause_threshold = 1
            self.r.adjust_for_ambient_noise(source, duration=1)
            audio = self.r.listen(source)

        try:
            self.command = self.r.recognize_google(audio).lower()
            print('You said: ' + self.command + '\n')

        except sr.UnknownValueError:
            print('Your last command couldn\'t be heard')
            self.command = self.myCommand()

        return self.command


    def assistant(self, command):

        if 'what are you doing' in command:
            self.talkToMe('Waiting for your command')
        else:
            self.talkToMe('Sorry could not understand you')


        self.talkToMe(audio='How may i help you')

    def call(self):
        while True:
            self.assistant(self.myCommand())



import mic1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_Assistant = QtWidgets.QMainWindow()
    ui = Ui_V_Assistant()
    ui.setupUi(V_Assistant)
    V_Assistant.show()
    sys.exit(app.exec_())
