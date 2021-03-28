from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendMessageForm(object):
    def setupUi(self, sendMessageForm):
        """

        :param sendMessageForm:
        :type sendMessageForm:
        """
        sendMessageForm.setObjectName("sendMessageForm")
        sendMessageForm.resize(400, 362)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        sendMessageForm.setFont(font)
        sendMessageForm.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.messagePlainTextEdit = QtWidgets.QPlainTextEdit(sendMessageForm)
        self.messagePlainTextEdit.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.messagePlainTextEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                                "font: 12pt \"Lucida Calligraphy\";")
        self.messagePlainTextEdit.setObjectName("messagePlainTextEdit")
        self.nameLineEdit = QtWidgets.QLineEdit(sendMessageForm)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 280, 381, 31))
        self.nameLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                        "font: 12pt \"Lucida Calligraphy\";")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.sendMessageButton = QtWidgets.QPushButton(sendMessageForm)
        self.sendMessageButton.setGeometry(QtCore.QRect(10, 320, 381, 31))
        self.sendMessageButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                             "border-radius: 10px;\n"
                                             "background-color: rgb(17, 167, 157);\n"
                                             "")
        self.sendMessageButton.setObjectName("sendMessageButton")

        self.retranslateUi(sendMessageForm)
        QtCore.QMetaObject.connectSlotsByName(sendMessageForm)

    def retranslateUi(self, sendMessageForm):
        """

        :param sendMessageForm:
        :type sendMessageForm:
        """
        _translate = QtCore.QCoreApplication.translate
        sendMessageForm.setWindowTitle(_translate("sendMessageForm", "Сообщение"))
        self.nameLineEdit.setPlaceholderText(_translate("sendMessageForm", "Имя"))
        self.sendMessageButton.setText(_translate("sendMessageForm", "Отправить сообщение"))
