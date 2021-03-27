from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginForm(object):
    def setupUi(self, loginForm):
        loginForm.setObjectName("loginForm")
        loginForm.resize(313, 148)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        loginForm.setFont(font)
        loginForm.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.usernameLineEdit = QtWidgets.QLineEdit(loginForm)
        self.usernameLineEdit.setGeometry(QtCore.QRect(10, 20, 291, 31))
        self.usernameLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                            "font: 12pt \"Lucida Calligraphy\";")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(loginForm)
        self.passwordLineEdit.setGeometry(QtCore.QRect(10, 60, 291, 31))
        self.passwordLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                            "font: 12pt \"Lucida Calligraphy\";")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.loginButton = QtWidgets.QPushButton(loginForm)
        self.loginButton.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.loginButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(17, 167, 157);\n"
                                       "")
        self.loginButton.setObjectName("loginButton")
        self.registrationButton = QtWidgets.QPushButton(loginForm)
        self.registrationButton.setGeometry(QtCore.QRect(150, 100, 151, 31))
        self.registrationButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(17, 167, 157);\n"
                                              "")
        self.registrationButton.setObjectName("registrationButton")

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        _translate = QtCore.QCoreApplication.translate
        loginForm.setWindowTitle(_translate("loginForm", "Авторизация"))
        self.usernameLineEdit.setPlaceholderText(_translate("loginForm", "Логин"))
        self.passwordLineEdit.setPlaceholderText(_translate("loginForm", "Пароль"))
        self.loginButton.setText(_translate("loginForm", "Войти"))
        self.registrationButton.setText(_translate("loginForm", "Регистрация"))
