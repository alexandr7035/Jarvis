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
    and its standard tuning.
    """

    def __call__(self, jarvis, s):
        # Chord name must passed as "s" string
        # Check if not empty
        if s.strip() != "":
            # Check if chord is described in the json
            try:
                self.get_chord(s.upper())
            except KeyError:
                jarvis.say("No such chord found.")
        else:
            jarvis.say("Please, specify the chord.")
    

        

    def get_chord(self, chord_name):
        with open(CHORDS_FILE) as f:
            chords = json.load(f)

        chord_data = chords[chord_name]
        chord_schema_list = EMPTY_NECK

        # Update chord schema
        for string in range(0,6):
            for index, fret in enumerate(chord_schema_list[string]):
                # Frets in the JSON are numerated from 1 while list' elements - from 0 
                # So add 1 to indexes here
                #
                # FIXME: maybe should number from 0 to 5 in json to avoid this?
                if (index + 1) in chord_data["string_" + str(string + 1)]:
                    chord_schema_list[string][index] = True


        print(chord_schema_list) 
                