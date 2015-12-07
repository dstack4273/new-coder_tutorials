from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc

class TalkBackBot(irc.IRCClient):

    def connectionMade(self):
        """ called when a connection is made to a channel """
        self.nickname = self.factory.nickname
        self.realname = self.factory.realname
        irc.IRCClient.connectionMade(self)
        log.msg("connectionMade")

    def connectionLost(self, reason):
        """ Called when the connection is lost """
        irc.IRCClient.connectionLost(self, reason)
        log.msg("connectionLost {!r}".format(reason))

    # callbacks for events

    def signedOn(self):
        """ Called when the bot has successfully signed on to the server """
        log.msg("Signed On")
        if self.nickname != self.factory.nickname:
            log.msg('Your nickname was already occupied, actual nickname is '
                    '"{}".'.format(self.nickname))
        self.join(self.factory.channel)

    def joined(self, channel):
        """ Called when the bot joins the channel """
        log.msg("[{nick} has joined {channel}]"
                .format(nick = self.nickname, channel = self.factory.channel,))

    def privmsg(self, user, channel, msg):
        """ Called when the bot recieves a message """
        sendTo = None
        prefix = ''
        senderNick = user.split('!', 1)[0]
        if channel == self.nickname:
            # /MSG back
            sendTo = senderNick
        elif msg.startswith(self.nickname):
            # Reply back on the channel
            sendTo = channel
            prefix = senderNick + ': '
        else:
            msg = msg.lower()
            for trigger in self.factory.triggers:
                if msg in trigger:
                    sendTo = channel
                    prefix = senderNick + ': '
                    break

        if sendTo:
            quote = self.factory.quotes.pick()
            self.msg(sendTo, prefix + quote)
            log.msg(
                "sent message to {reciever}, triggered by {sender}:\n\t{quote}"
                .format(reciever=sendTo, sender=senderNick, quote=quote)
            )

class TalkBackBotFactory(protocol.ClientFactory):
    protocol = TalkBackBot

    def __init__(self, channel, nickname, realname, quotes, triggers):
        """ Initilzing the bot factory with our defined settings """
        self.channel = channel
        self.nickname = nickname
        self.realname = realname
        self.quotes = quotes
        self.triggers = triggers
