from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc

class TalkBackBotFactort(protocol.ClientFactory):

    def __init__(self, settings):
        """ Initilzing the bot factory with our defined settings """

class TalkBackBot(irc.IRCClient):

    def connectionMade(self):
        """ called when a connection is made (to a channel?) """

    def connectionLost(self, reason):
        """ Called when the connection is lost """

    # callbacks for events

    def signedOn(self):
        """ Called when the bot has successfully signed on to the server """

    def joined(self, channel):
        """ Called when the bot joins the channel """

    def privmsg(self, user, channel, msg):
        """ Called when the bot recieves a message """
