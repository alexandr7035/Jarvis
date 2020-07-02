import os
from plugin import plugin, alias
from colorama import Fore

PLUGIN_PATH = os.path.abspath(os.path.dirname(__file__))
CHORD_BASIC_SCHEMA_FILE = os.path.join(PLUGIN_PATH, "../data/chord_basic_schema.txt")

@alias('chords')
@plugin('chord')
class ChordsPlugin():
    """
    Prints the schema of a guitar chord.
    The plugin is now designed only for a 6-string guitar 
    and its standard tuning
    """

    def __call__(self, jarvis, s):
        with open(CHORD_BASIC_SCHEMA_FILE, "r") as f:
            jarvis.say(f.read())
