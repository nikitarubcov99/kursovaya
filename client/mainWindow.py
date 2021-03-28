from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QListWidget, QWidget, QVBoxLayout, QScrollArea, QHBoxLayout, QLabel, QTabWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """

        :param MainWindow:
        :type MainWindow:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 434)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 511, 421))
        self.tabWidget.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                     "border-radius: 10px;\n"
                                     "color: rgb(17, 167, 157);\n"
                                     "")
        self.profileTab = QWidget()
        self.profileTab.setObjectName(u"profileTab")
        self.helloLabel = QLabel(self.profileTab)
        self.helloLabel.setObjectName(u"helloLabel")
        self.helloLabel.setGeometry(QRect(10, 10, 491, 31))
        self.infoLabel = QLabel(self.profileTab)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(10, 50, 491, 31))
        self.messagesList = QListWidget(self.profileTab)
        self.messagesList.setObjectName(u"messagesList")
        self.messagesList.setGeometry(QRect(10, 90, 491, 281))
        self.messagesList.setStyleSheet(u"background: rgba(10,100,120,100);")
        self.tabWidget.addTab(self.profileTab, "")
        self.feedNewsTab = QWidget()
        self.feedNewsTab.setObjectName(u"feedNewsTab")
        self.horizontalLayout = QHBoxLayout(self.feedNewsTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.feedsArea = QScrollArea(self.feedNewsTab)
        self.feedsArea.setObjectName(u"feedsArea")
        self.feedsArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 481, 353))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.feedsArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.feedsArea)

        self.tabWidget.addTab(self.feedNewsTab, "")
        self.myNewsFeedTab = QWidget()
        self.myNewsFeedTab.setObjectName(u"myNewsFeedTab")
        self.myFeedsArea = QScrollArea(self.myNewsFeedTab)
        self.myFeedsArea.setObjectName(u"myFeedsArea")
        self.myFeedsArea.setGeometry(QRect(10, 10, 487, 365))
        self.myFeedsArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 485, 363))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.myFeedsArea.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.myNewsFeedTab, "")
        self.friendsTab = QWidget()
        self.friendsTab.setObjectName(u"friendsTab")
        self.friendsList = QListWidget(self.friendsTab)
        self.friendsList.setObjectName(u"friendsList")
        self.friendsList.setGeometry(QRect(10, 10, 491, 321))
        font1 = QFont()
        font1.setFamily(u"Lucida Calligraphy")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.friendsList.setFont(font1)
        self.friendsList.setStyleSheet(u"")
        self.tabWidget.addTab(self.friendsTab, "")
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(530, 300, 211, 31))
        self.exitButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                      "border-radius: 10px;\n"
                                      "background-color: rgb(17, 167, 157);\n"
                                      "")
        self.sendMessageButton = QPushButton(self.centralwidget)
        self.sendMessageButton.setObjectName(u"sendMessageButton")
        self.sendMessageButton.setGeometry(QRect(530, 140, 211, 31))
        self.sendMessageButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                             "border-radius: 10px;\n"
                                             "background-color: rgb(17, 167, 157);\n"
                                             "")
        self.createPostButton = QPushButton(self.centralwidget)
        self.createPostButton.setObjectName(u"createPostButton")
        self.createPostButton.setGeometry(QRect(530, 180, 211, 31))
        self.createPostButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                            "border-radius: 10px;\n"
                                            "background-color: rgb(17, 167, 157);\n"
                                            "")
        self.deleteFriend = QPushButton(self.centralwidget)
        self.deleteFriend.setObjectName(u"deleteFriend")
        self.deleteFriend.setGeometry(QRect(530, 260, 211, 31))
        self.deleteFriend.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                        "border-radius: 10px;\n"
                                        "background-color: rgb(17, 167, 157);\n"
                                        "")
        self.addFriend = QPushButton(self.centralwidget)
        self.addFriend.setObjectName(u"addFriend")
        self.addFriend.setGeometry(QRect(530, 220, 211, 31))
        self.addFriend.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                     "border-radius: 10px;\n"
                                     "background-color: rgb(17, 167, 157);\n"
                                     "")
        self.aboutMeButton = QPushButton(self.centralwidget)
        self.aboutMeButton.setObjectName(u"aboutMeButton")
        self.aboutMeButton.setGeometry(QRect(530, 100, 211, 31))
        self.aboutMeButton.setStyleSheet(u"font: 12pt \"Lucida Calligraphy\";\n"
                                         "border-radius: 10px;\n"
                                         "background-color: rgb(17, 167, 157);\n"
                                         "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """

        :param MainWindow:
        :type MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helloLabel.setText(_translate("MainWindow", "Здравствуйте , Олег"))
        self.infoLabel.setText(_translate("MainWindow", "У вас 6 непрочитанных сообщений"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profileTab), _translate("MainWindow", "Профиль"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.feedNewsTab), _translate("MainWindow", "Лента"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.myNewsFeedTab), _translate("MainWindow", "Моя лента"))
        self.addFriend.setText(_translate("MainWindow", "Добавить друга"))
        self.deleteFriend.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.friendsTab), _translate("MainWindow", "Друзья"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.sendMessageButton.setText(_translate("MainWindow", "Отправить сообщение"))
        self.createPostButton.setText(_translate("MainWindow", "Создать пост"))
        self.aboutMeButton.setText(_translate("MainWindow", "Обо мне"))
