from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutMeForm(object):
    def setupUi(self, aboutMeForm):
        """

        :param aboutMeForm:
        :type aboutMeForm:
        """
        aboutMeForm.setObjectName("aboutMeForm")
        aboutMeForm.resize(272, 479)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        aboutMeForm.setFont(font)
        aboutMeForm.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.aboutMeArea = QtWidgets.QScrollArea(aboutMeForm)
        self.aboutMeArea.setGeometry(QtCore.QRect(10, 40, 251, 431))
        self.aboutMeArea.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                       "font: 12pt \"Lucida Calligraphy\";")
        self.aboutMeArea.setWidgetResizable(True)
        self.aboutMeArea.setObjectName("aboutMeArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 249, 429))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.aboutMeArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtWidgets.QLabel(aboutMeForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label.setStyleSheet(u"color: rgb(17, 167, 157);\n"
                                 "font: 12pt \"Lucida Calligraphy\";")

        self.label.setObjectName("label")

        self.retranslateUi(aboutMeForm)
        QtCore.QMetaObject.connectSlotsByName(aboutMeForm)

    def retranslateUi(self, aboutMeForm):
        """

        :param aboutMeForm:
        :type aboutMeForm:
        """
        _translate = QtCore.QCoreApplication.translate
        aboutMeForm.setWindowTitle(_translate("aboutMeForm", "Обо мне"))
        self.label.setText(_translate("aboutMeForm", "Данные:"))
