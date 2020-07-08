import os
import json
from plugin import plugin, alias
from colorama import Fore

PLUGIN_PATH = os.path.abspath(os.path.dirname(__file__))
CHORDS_FILE = os.path.join(PLUGIN_PATH, "../data/chords.json")

# List for guitar neck
# 6 strings, 12 flats
#
# See https://www.guitar-chord.org/images/fretboard.png
EMPTY_NECK = [
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False]
]



@alias('chords')
@plugin('chord')
class ChordsPlugin():
    """
    Prints the schema of a guitar chord.
    The plugin is now designed only for a 6-string guitar 
    and its standard tuning
    """

    def __call__(self, jarvis, s):
        jarvis.say(str(EMPTY_NECK))

        self.get_chord("C")

    def get_chord(self, chord_name):
        with open(CHORDS_FILE) as f:
            chords = json.load(f)

        chord_data = chords[chord_name]

        print(chord_data)