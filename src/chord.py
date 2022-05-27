import src.note as note
import src.scale as scale

class Chord():

    def __init__(self, name, notes):
        self._name = name
        self._notes = notes

    def name(self):
        return self._name

    def notes(self):
        return self._notes

    def __str__(self):
        note_names = [x.name() for x in self.notes()]
        return f"{self.name()}: {'-'.join(note_names)}"

    def __repr__(self):
        return json.dumps(dict(self))

def triad(scale):
    if scale:
        return Chord(scale.name(), scale.notes()[0:5:2])
    else:
        return None

major = { pitch: triad(scale.major[pitch]) for pitch in scale.major.keys() }
minor = { pitch: triad(scale.minor[pitch]) for pitch in scale.minor.keys() }
