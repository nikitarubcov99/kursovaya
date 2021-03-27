from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createPostForm(object):
    def setupUi(self, createPostForm):
        createPostForm.setObjectName("createPostForm")
        createPostForm.resize(460, 393)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        createPostForm.setFont(font)
        createPostForm.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.postTextBrowser = QtWidgets.QTextBrowser(createPostForm)
        self.postTextBrowser.setGeometry(QtCore.QRect(10, 10, 441, 331))
        self.postTextBrowser.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                           "font: 12pt \"Lucida Calligraphy\";")
        self.postTextBrowser.setReadOnly(False)
        self.postTextBrowser.setObjectName("postTextBrowser")
        self.sendPostButton = QtWidgets.QPushButton(createPostForm)
        self.sendPostButton.setGeometry(QtCore.QRect(10, 350, 441, 31))
        self.sendPostButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                          "border-radius: 10px;\n"
                                          "background-color: rgb(17, 167, 157);\n"
                                          "")
        self.sendPostButton.setObjectName("sendPostButton")

        self.retranslateUi(createPostForm)
        QtCore.QMetaObject.connectSlotsByName(createPostForm)

    def retranslateUi(self, createPostForm):
        _translate = QtCore.QCoreApplication.translate
        createPostForm.setWindowTitle(_translate("createPostForm", "Создание поста"))
        self.postTextBrowser.setPlaceholderText(_translate("createPostForm", "ПОДДЕРЖИВАЮТСЯ HTML ТЕГИ ДЛЯ ФОРМАТИРОВАНИЯ ТЕКСТА"))
        self.sendPostButton.setText(_translate("createPostForm", "Опубликовать"))
