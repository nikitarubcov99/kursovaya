from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageForm(object):
    def setupUi(self, MessageForm):
        MessageForm.setObjectName("MessageForm")
        MessageForm.resize(400, 319)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        MessageForm.setFont(font)
        MessageForm.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.messageTextBrowser = QtWidgets.QTextBrowser(MessageForm)
        self.messageTextBrowser.setGeometry(QtCore.QRect(10, 10, 381, 271))
        self.messageTextBrowser.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                              "font: 12pt \"Lucida Calligraphy\";")
        self.messageTextBrowser.setObjectName("messageTextBrowser")
        self.senderNameLabel = QtWidgets.QLabel(MessageForm)
        self.senderNameLabel.setGeometry(QtCore.QRect(10, 290, 371, 20))
        self.senderNameLabel.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                           "font: 12pt \"Lucida Calligraphy\";")
        self.senderNameLabel.setObjectName("senderNameLabel")

        self.retranslateUi(MessageForm)
        QtCore.QMetaObject.connectSlotsByName(MessageForm)

    def retranslateUi(self, MessageForm):
        _translate = QtCore.QCoreApplication.translate
        MessageForm.setWindowTitle(_translate("MessageForm", "Сообщение"))
        self.senderNameLabel.setText(_translate("MessageForm", "TextLabel"))
