import jsonpickle
import src.pitch as pitch
import src.note as note
import src.scale as scale

class Chord():

    def __init__(self, name, notes, major=True, diminished=False, uses_proxy=False):
        self._name = name
        self._notes = notes
        self._major = major
        self._diminished = diminished
        self._uses_proxy = uses_proxy

    def name(self):
        return self._name

    def notes(self):
        return self._notes

    def is_major(self):
        return self._major

    def is_diminished(self):
        return self._diminished

    def uses_proxy(self):
        return self._uses_proxy

    def type(self):
        if self.is_major():
            return 'maj'
        elif self.is_diminished():
            return 'dim'
        elif self.is_minor():
            return 'min'
        else:
            raise ValueError(f'{self.name()} is not a valid chord type - please check values.')

    def is_minor(self):
        return not self.is_major() and not self.is_diminished()

    def includes_alias(self):
        return self._includes_alias

    def __str__(self):
        note_names = [x.name() for x in self.notes()]
        return f"{self.name()}: {'-'.join(note_names)}"

    def __repr__(self):
        return jsonpickle(self)

    @classmethod
    def classify_by_scale_degree(cls, degree, maj_min):
        if maj_min == 'maj':
            if (degree in (1, 4, 5)):
                return 'maj'
            elif (degree in (2, 3, 6)):
                return 'min'
            elif (degree == 7):
                return 'dim'
            else:
                raise IndexError(f'{degree} is out of bounds. degree should be a value in range 1..7')
        elif maj_min == 'min':
            if (degree in (3, 6, 7)):
                return 'maj'
            elif (degree in (1, 4, 5)):
                return 'min'
            elif (degree == 2):
                return 'dim'
            else:
                raise IndexError(f'{degree} is out of bounds. degree should be a value in range 1..7')
        else:
            raise IndexError(f'{maj_min} is an invalis scale type - must be either maj or min.')

    @classmethod
    def boolean_tuple_type(cls, type_str):
        if type_str == 'maj':
            return (True, False)
        elif type_str == 'dim':
            return (False, True)
        elif type_str == 'min':
            return (False, False)
        else:
            raise ValueError(f'{type_str} is an invalid chord type. Valid types are maj, min or dim')

    @classmethod
    def triad(cls, scale, degree=1):
        if scale:
            # find if the chord is maj/min/dim
            type_str = Chord.classify_by_scale_degree(degree, scale.maj_min())
            # set boolean flags
            (is_major, is_diminished) = Chord.boolean_tuple_type(type_str)
            # select the degree note from scale, then the next two thirds
            # where a third is two further degrees into the scale
            degree -= 1
            slicer = slice(degree, degree+5, 2)
            notes = list(scale.notes() + scale.notes())[slicer]
            # name is the first note's pitch
            name = notes[0].name() + type_str
            # some piano chords use a different key as a proxy
            # substitute the proxy in _after_ determining the name
            uses_proxy = False
            piano_keys = []
            for i, note in enumerate(notes):
                # if note in pitch.non_key_pitches:
                if note not in pitch.key_pitches:
                    if pitch.proxy[note.name()]:
                        piano_keys.append(pitch.proxy[note.name()])
                        uses_proxy = True
                    else:
                        raise IndexError(f'No proxy found for {note.name()}.')
                else:
                    piano_keys.append(note)
            return Chord(
                name, piano_keys, is_major, is_diminished, uses_proxy
            )
        else:
            return None

chords = {}
for p in pitch.key_pitches:
    pname = p.name() # C, C#, Db, etc.
    for maj_min in ('maj', 'min'):
        key = ''.join((pname, maj_min))
        s = scale.scales[key]
        if s:
            for j, note in enumerate(s.notes()):
                c = Chord.triad(s, j+1)
                name = c.name()
                if name in chords.keys():
                    if (chords[name].notes() != c.notes()) and not c.uses_proxy():
                        raise ValueError(f'Conflicting values for {name} chord: {chords[name]} and {c}')
                chords[name] = c
