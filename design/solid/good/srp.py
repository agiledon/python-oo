#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Email(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Content(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_string(self):
        pass


class MyContent(Content):
    def __init__(self, content):
        self.content = content

    def get_string(self):
        return "<MyML>{}</MyML>".format(self.content)


class DefaultEmail(Email):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.get_string()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


def main():
    email = DefaultEmail('IM')
    email.set_sender('qmal')
    email.set_receiver('james')
    content = MyContent('Hello, there!')
    email.set_content(content)
    print(email)


if __name__ == '__main__':
    main()
