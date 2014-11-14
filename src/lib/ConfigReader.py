import os

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

class ConfigReader(object):
    def __init__ (self, path, file, section):
        self.config = ConfigParser()
        self.config.read(os.path.join(path, file))
        self.section = section

    def get_string(self, name):
        return self.config.get(self.section, name)

    def get_int(self, name):
        return int(self.config.get(self.section, name))