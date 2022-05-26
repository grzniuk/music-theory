import src.note as note
import src.scale as scale

class Chord():

    def __init__(self, name, notes):
        self._name = name
        self._notes = notes

    def notes(self):
        return self._notes

major = {}
for maj in scale.major:
    if maj:
        # get alternate values from the scale between 0 and 5
        major[maj.name()] = Chord(maj.name(), maj.notes()[0:5:2])

minor = {}
for min in scale.minor:
    if min:
        # get alternate values from the scale between 0 and 5
        minor[min.name()] = Chord(min.name(), min.notes()[0:5:2])
