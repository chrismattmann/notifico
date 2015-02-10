# -*- coding: utf8 -*-
from utopia import signals


class NickInUsePlugin(object):
    def __init__(self, nick_func):
        """
        A plugin that automatically tries the next nick, if
        the current nick is already in use.

        :param nick_func: A function which returns
                          the new nick to select
        """
        self._fun = nick_func

    def bind(self, client):
        signals.m.on_443.connect(self.on_443, sender=client)

        return self

    def on_443(self, client, prefix, args):
        client.identity._nick = self._fun()
        client.send('NICK', client.identity.nick)
        client.send(
            'USER',
            client.identity.user,
            '8',
            '*',
            client.identity.real
        )


