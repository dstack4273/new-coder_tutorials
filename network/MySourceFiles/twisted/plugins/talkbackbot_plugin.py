from ConfigParser import ConfigParser

from twisted.application.service import IServiceMaker, Service
from twisted.internet.endpoints import clientFromString
from twisted.plugin import IPlugin
from twisted.python import usage, log
from zope.interface import implementer

from talkback.bot import TalkBackBotFactory
from talkback.quote_picker import QuotePicker

class Options(usage.Options):

class TalkBackBotService(Service):

    def __init__(self, endpoint, channel, nickname, realname, quotesFilename, triggers):

    def startService(self):
        """ Constructs a client and connects to the server """

    def stopService(self):
        """ Disconnect """

class BotServiceMaker(object):
    tapname = "twsrs"
    description = ""
    options = Options

    def makeService (self, options):
        
