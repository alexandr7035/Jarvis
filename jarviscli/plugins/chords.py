import os
from plugin import plugin, alias
from colorama import Fore

FILE_PATH = os.path.abspath(os.path.dirname(__file__))

@alias('chords')
@plugin('chord')
class ChordsPlugin():
    """
    Prints the schema of a guitar chord.
    The plugin is now designed only for a 6-string guitar 
    and its standard tuning
    """

    def __call__(self, jarvis, s):
        jarvis.say("TEST TEST TEST")
