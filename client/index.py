import pickle
import socket
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QInputDialog

import aboutMeWindow
import createPostWindow
import messageWindow
import sendMessageWindow
import loginWindow
import mainWindow
import registrationWindow


def send_request(request):
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.sendall(pickle.dumps(request))
    data = sock.recv(64000)
    sock.close()
    return pickle.loads(data)


class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):

    def __init__(self, user_data):
        self.user_data = user_data
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.send_message_window = None
        self.show_message_window = None
        self.create_post_window = None
        self.about_me_window = None
        self.exitButton.clicked.connect(self.close)
        self.createPostButton.clicked.connect(self.create_post)
        self.username = user_data.get('username')
        self.user_name = user_data.get('name')
        self.user_email = user_data.get('email')
        self.messages = []
        self.sendMessageButton.clicked.connect(self.show_send_message_window)
        self.refresh_messages_list()
        self.refresh_labels()
        self.refresh_news_feed()
        self.refresh_my_news_feed()
        self.refresh_friends_list()
        self.addFriend.clicked.connect(self.add_friend)
        self.deleteFriend.clicked.connect(self.delete_friend)
        self.messagesList.doubleClicked.connect(self.show_message)
        self.aboutMeButton.clicked.connect(self.open_about_me_window)

    def add_friend(self):
        text, ok = QInputDialog.getText(self, 'Добавить друга', 'Введите имя друга:')
        if ok:
            send_request(["add friend", {"username": self.username, "friend": text}])
            self.refresh_friends_list()

    def delete_friend(self):
        if self.friendsList.currentItem() is not None:
            print(self.friendsList.currentItem())
            send_request(
                ["delete friend", {"username": self.username, "friend": self.friendsList.currentItem().text()}])
            self.refresh_friends_list()

    def refresh_friends_list(self):
        response = send_request(["get user friends", {"username": self.username}])
        self.friendsList.clear()
        for i in response[1].get("friends"):
            self.friendsList.addItem(i)

    def refresh_my_news_feed(self):
        response = send_request(["get posts", {"username": self.username}])
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        if response[0]:
            for i in response[1]:
                elem = QtWidgets.QTextBrowser()
                elem.setText(i.get("text"))
                elem.setHtml(i.get("html"))
                self.verticalLayout_2.addWidget(elem)

    def refresh_news_feed(self):
        response = send_request(["get all posts"])
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        if response[0]:
            for i in response[1]:
                label = QtWidgets.QLabel()
                label.setText(f"Автор поста:{i.get('author')}")
                elem = QtWidgets.QTextBrowser()
                elem.setText(i.get("text"))
                elem.setHtml(i.get("html"))
                self.verticalLayout.addWidget(label)
                self.verticalLayout.addWidget(elem)

    def open_about_me_window(self):
        self.about_me_window = AboutMeWindow(self.user_data)
        self.about_me_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.about_me_window.show()

    def create_post(self):
        self.show_message_window = CreatePostWindow(self.username, self)
        self.show_message_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show_message_window.show()

    def show_message(self):
        message = self.messages.pop(self.messagesList.currentRow())
        self.show_message_window = MessageWindow(message.get("text"), message.get("sender_name"))
        self.show_message_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show_message_window.show()
        request = ["delete message", {"username": self.username, "text": message.get("text")}]
        send_request(request)
        self.refresh_messages_list()
        self.refresh_labels()

    def refresh_labels(self):
        self.helloLabel.setText(f"Здравствуйте, {self.user_name}")
        self.infoLabel.setText(f"У вас {len(self.messages)} непрочитанных сообщений")

    def refresh_messages_list(self):
        self.messages = send_request(
            ["get user messages", {"username": self.username}])[1].get("messages")
        self.messagesList.clear()
        for i in self.messages:
            self.messagesList.addItem(i.get("text").split("\n")[0])

    def show_send_message_window(self):
        self.send_message_window = SendMessageWindow(self.username, self)
        self.send_message_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.send_message_window.show()


class AboutMeWindow(QtWidgets.QWidget, aboutMeWindow.Ui_aboutMeForm):

    def __init__(self, user_data):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.user_data = user_data

        layout = QVBoxLayout(self)
        self.aboutMeArea.setLayout(layout)

        name_label = QtWidgets.QLabel()
        username_label = QtWidgets.QLabel()
        email_label = QtWidgets.QLabel()

        name_label.setText(f"Имя:{user_data.get('name')}")
        username_label.setText(f"Логин:{user_data.get('username')}")
        email_label.setText(f"Почта:{user_data.get('email')}")
        layout.addWidget(name_label)
        layout.addWidget(username_label)
        layout.addWidget(email_label)


class CreatePostWindow(QtWidgets.QWidget, createPostWindow.Ui_createPostForm):

    def __init__(self, username, main_window):
        """

        :param username:
        :type username:
        :param main_window:
        :type main_window:
        """
        self.main_window = main_window
        super().__init__()
        self.username = username
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.sendPostButton.clicked.connect(self.send_post)

    def send_post(self):
        if len(self.postTextBrowser.toPlainText()) <= 50:
            self.postTextBrowser.setPlainText("Пост слишком короткий!!")
        else:
            request = ["create post",
                       {"html": self.postTextBrowser.toHtml(), "text": self.postTextBrowser.toPlainText(),
                        "username": self.username}]
            send_request(request)
            self.main_window.refresh_news_feed()
            self.main_window.refresh_my_news_feed()
            self.close()


class RegistrationWindow(QtWidgets.QWidget, registrationWindow.Ui_registrationForm):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.registrationButton.clicked.connect(self.registration)
        self.main_window = None

    def registration(self):
        if self.nameLineEdit.text() != "" and self.emailLineEdit.text() != "" and self.usernameLineEdit.text() != "" \
                and self.passwordLineEdit.text() != "":
            request = ["add user", {"name": self.nameLineEdit.text(), "email": self.emailLineEdit.text(),
                                    "username": self.usernameLineEdit.text(), "password": self.passwordLineEdit.text()}]
            send_request(request)
            self.close()


class MessageWindow(QtWidgets.QWidget, messageWindow.Ui_MessageForm):

    def __init__(self, text, sender_name):
        """

        :param text:
        :type text:
        :param sender_name:
        :type sender_name:
        """
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.sender_name = sender_name
        self.senderNameLabel.setText(f"Получено от: {self.sender_name}")
        self.messageTextBrowser.setPlainText(text)


class SendMessageWindow(QtWidgets.QWidget, sendMessageWindow.Ui_sendMessageForm):

    def __init__(self, sender_name, main_window):
        """

        :param sender_name:
        :type sender_name:
        :param main_window:
        :type main_window:
        """
        self.main_window = main_window
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.sender_name = sender_name
        self.sendMessageButton.clicked.connect(self.send_message)

    def send_message(self):
        request = ["send message",
                   {"recipient_name": self.nameLineEdit.text(), "text": self.messagePlainTextEdit.toPlainText(),
                    "sender_name": self.sender_name}]
        response = send_request(request)
        if response[0]:
            self.messagePlainTextEdit.setPlainText("Сообщение успешно отправлено")
            self.main_window.refresh_messages_list()
            self.main_window.refresh_labels()
        else:
            self.messagePlainTextEdit.setPlainText("Пользователь с таким именем не найден")


class LoginWindow(QtWidgets.QWidget, loginWindow.Ui_loginForm):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.registrationButton.clicked.connect(self.registration)
        self.loginButton.clicked.connect(self.login)
        self.registration_window = None
        self.main_window = None

    def login(self):

        if self.usernameLineEdit.text() != "" and self.passwordLineEdit.text() != "":
            response = send_request(
                ["get user", {"username": self.usernameLineEdit.text(), "password": self.passwordLineEdit.text()}])
            if response[0]:
                self.main_window = MainWindow(response[1])
                self.main_window.show()
                self.close()
            else:
                pass

    def registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.registration_window.show()


def my_except_hook(in_type, value, type_back):
    """

    :param in_type:
    :type in_type:
    :param value:
    :type value:
    :param type_back:
    :type type_back:
    """
    QtWidgets.QMessageBox.critical(
        window, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(in_type, value, type_back)


sys.excepthook = my_except_hook
app = QtWidgets.QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec_())
