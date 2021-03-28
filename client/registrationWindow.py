from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registrationForm(object):
    def setupUi(self, registrationForm):
        """

        :param registrationForm:
        :type registrationForm:
        """
        registrationForm.setObjectName("registrationForm")
        registrationForm.resize(313, 211)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        registrationForm.setFont(font)
        registrationForm.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.usernameLineEdit = QtWidgets.QLineEdit(registrationForm)
        self.usernameLineEdit.setGeometry(QtCore.QRect(10, 90, 291, 31))
        self.usernameLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                            "font: 12pt \"Lucida Calligraphy\";")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(registrationForm)
        self.passwordLineEdit.setGeometry(QtCore.QRect(10, 130, 291, 31))
        self.passwordLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                            "font: 12pt \"Lucida Calligraphy\";")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.nameLineEdit = QtWidgets.QLineEdit(registrationForm)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.nameLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                        "font: 12pt \"Lucida Calligraphy\";")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(registrationForm)
        self.emailLineEdit.setGeometry(QtCore.QRect(10, 50, 291, 31))
        self.emailLineEdit.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                         "font: 12pt \"Lucida Calligraphy\";")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.registrationButton = QtWidgets.QPushButton(registrationForm)
        self.registrationButton.setGeometry(QtCore.QRect(10, 170, 291, 31))
        self.registrationButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                              "border-radius: 10px;\n"
                                              "background-color: rgb(17, 167, 157);\n"
                                              "")
        self.registrationButton.setObjectName("registrationButton")

        self.retranslateUi(registrationForm)
        QtCore.QMetaObject.connectSlotsByName(registrationForm)

    def retranslateUi(self, registrationForm):
        """

        :param registrationForm:
        :type registrationForm:
        """
        _translate = QtCore.QCoreApplication.translate
        registrationForm.setWindowTitle(_translate("registrationForm", "Регистрация"))
        self.usernameLineEdit.setPlaceholderText(_translate("registrationForm", "Логин"))
        self.passwordLineEdit.setPlaceholderText(_translate("registrationForm", "Пароль"))
        self.nameLineEdit.setPlaceholderText(_translate("registrationForm", "Имя"))
        self.emailLineEdit.setPlaceholderText(_translate("registrationForm", "Электронная почта"))
        self.registrationButton.setText(_translate("registrationForm", "Зарегистрироваться"))
