import os
import logging

from mk2.plugins import Plugin
from mk2.events import Console, ServerStopped, ServerStopping, ServerOutput

def get_level(string):
    if string is "DEBUG":
        return logging.DEBUG
    if string is "INFO":
        return logging.INFO
    if string is "WARN":
        return logging.WARN
    if string is "ERROR":
        return logging.ERROR
    return string


class Log(Plugin):
    path      = Plugin.Property(default="logs/server.log")
    
    def setup(self):
        self.register(self.logger, Console)
        self.logger = logging.getLogger('MinecraftLogger')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.handlers.RotatingFileHandler(self.path, maxBytes=536870912, backupCount=5))

    def logger(self, event):
        event.level
        self.logger.log(get_level(event.level), event.data)
