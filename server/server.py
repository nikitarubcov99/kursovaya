import pickle
import socket

from sqlalchemy.orm import sessionmaker

import model
from model import *

Session = sessionmaker(bind=model.engine)
session = Session()

def start():
    import socket
    model.init()
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', 9090))
    serv_sock.listen(10)

    while True:
        client_sock, address = serv_sock.accept()
        print('Connected by', address)

        while True:
            data = client_sock.recv(64000)
            if not data:
                break
            request = pickle.loads(data)
            client_sock.sendall(check_request(request))

        client_sock.close()


def check_request(request):
    """

    :param request:
    :type request:
    :return:
    :rtype:
    """
    if request[0] == "add user":
        user = session.query(User).filter(User.name == request[1].get('name')).first()
        if user:
            return pickle.dumps([False, "Пользователь с логином {request[1].get('username')} уже существует"])
        else:
            user = model.User(request[1].get("name"), request[1].get("email"), request[1].get("username"),
                              request[1].get("password"))
            session.add(user)
            session.commit()
            return pickle.dumps([True, "Пользователь с логином {request[1].get('username')} создан"])
    elif request[0] == "get user":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user and user.password == request[1].get('password'):
            return pickle.dumps(
                [True, {"username": str(user.username), "name": str(user.name), "email": str(user.email)}])
        return pickle.dumps([False])
    elif request[0] == "get user messages":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user:
            messages = []
            for i in user.messages:
                messages.append({"text": i.text, "sender_name": i.sender_name})
            return pickle.dumps(
                [True, {"messages": messages}])
        return pickle.dumps([False])
    elif request[0] == "get user friends":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user:
            friends = [i for i in user.friends.split("NEXT") if i != ""]
            return pickle.dumps(
                [True, {"friends": friends}])
        return pickle.dumps([False])
    elif request[0] == "add friend":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        all_users = session.query(User).all()
        if user:
            for need_user in all_users:
                if need_user.name == request[1].get('friend'):
                    user.friends += f"{request[1].get('friend')}NEXT"
                    session.add(user)
                    session.commit()
                    return pickle.dumps(
                        [True])
        return pickle.dumps([False])
    elif request[0] == "delete friend":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user:
            user.friends = user.friends.replace(f"{request[1].get('friend')}", "")
            session.add(user)
            session.commit()
            return pickle.dumps(
                [True])
        return pickle.dumps([False])
    elif request[0] == "delete message":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user:
            messages = user.messages
            for message in messages:
                if message.text == request[1].get('text'):
                    session.delete(message)
                    session.commit()
                    return pickle.dumps(
                        [True, "Сообщение удалено"])
        return pickle.dumps([False])
    elif request[0] == "send message":
        user = session.query(User).filter(User.name == request[1].get('recipient_name')).first()
        if user:
            message = Message(request[1].get('text'), request[1].get('sender_name'))
            message.parent = user
            session.add(message)
            session.commit()
            return pickle.dumps(
                [True, "Сообщение отправлено"])
        return pickle.dumps([False])
    elif request[0] == "create post":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user:
            post = Post(request[1].get('html'), request[1].get('text'), user.name)
            post.parent = user
            session.add(post)
            session.commit()
            return pickle.dumps(
                [True, "Пост опубликован"])
        return pickle.dumps([False])
    elif request[0] == "get posts":
        user = session.query(User).filter(User.username == request[1].get('username')).first()
        if user:
            posts = []
            for i in user.posts:
                posts.append({"text": i.text, "html": i.html})
            return pickle.dumps([True, posts])
        return pickle.dumps([False])
    elif request[0] == "get all posts":
        users = session.query(User).all()
        posts = []
        for user in users:
            for i in user.posts:
                posts.append({"text": i.text, "html": i.html, "author": i.creator_name})
        return pickle.dumps([True, posts])


if __name__ == '__main__':
    start()
