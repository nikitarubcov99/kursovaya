from sqlalchemy import Column, Integer, String, create_engine, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data.sqlite')

Base = declarative_base()


def init():
    Base.metadata.create_all(engine)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    html = Column(Text)
    creator_name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, html, text, creator_name):
        """
        :param html:
        :type html:
        :param text:
        :type text:
        :param creator_name:
        :type creator_name:
        """
        self.html = html
        self.text = text
        self.creator_name = creator_name

    def __repr__(self):
        return f"<Post('{self.text}')>"


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    sender_name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, text, sender_name):
        """
        :param text:
        :type text:
        :param sender_name:
        :type sender_name:
        """
        self.text = text
        self.sender_name = sender_name

    def __repr__(self):
        """
        :return:
        :rtype:
        """
        return f"<Message('{self.text}')>"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    messages = relationship("Message", backref='parent')
    posts = relationship("Post", backref='parent')
    friends = Column(Text)

    def __init__(self, name, email, username, password):
        """

        :param name:
        :type name:
        :param email:
        :type email:
        :param username:
        :type username:
        :param password:
        :type password:
        """
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.friends = ""

    def __repr__(self):
        """

        :return:
        :rtype:
        """
        return "<User('%s','%s', '%s')>" % (self.name, self.username, self.password)
