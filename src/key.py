import jsonpickle
import chord
import pitch
import scale

class Key:

    def __init__(self, name, chords):
        for c in (chords):
            if not isinstance(c, chord.Chord):
                raise TypeError(f"{c} is not a valid chord object.")
        self._name = name
        self._chords = chords

    def __str__(self):
        return f"{self.name}: {', '.join(self.chord_names())}"

    def __repr__(self):
        return jsonpickle.encode(self)

    @property
    def name(self):
        return self._name

    @property
    def chords(self):
        return self._chords

    def chord_names(self):
        return tuple([c.name() for c in self.chords])

    # 1..7 -> chords[0..6] so to dereference decrement degree_number
    def degree(self, degree_number):
        if degree_number not in range(1, 7):
            raise ValueError('degree_number: {degree_number} must be in range 1..7.')
        return self.chords[degree_number - 1]

    @property
    def tonic(self):
        return self._chords[0]

    @property
    def I(self):
        return self._chords[0]

    @property
    def supertonic(self):
        return self._chords[1]

    @property
    def II(self):
        return self._chords[1]

    @property
    def mediant(self):
        return self._chords[2]

    @property
    def III(self):
        return self._chords[2]

    @property
    def subdominant(self):
        return self._chords[3]

    @property
    def IV(self):
        return self._chords[3]

    @property
    def dominant(self):
        return self._chords[4]

    @property
    def V(self):
        return self._chords[4]

    @property
    def submediant(self):
        return self._chords[5]

    @property
    def VI(self):
        return self._chords[5]

    @property
    def leading(self):
        return self._chords[6]

    @property
    def VII(self):
        return self._chords[6]

triads = {}

for p in pitch.key_pitches:
    # pitch name e.g. C, C#, Db, etc.
    pname = p.name

    # loop for major and minor scales
    for maj_min in ('maj', 'min'):

        # key name e.g. Cmaj, Cmin, C#maj, etc.
        key_name = ''.join((pname, maj_min))
        s = scale.scales[key_name]

        chord_list = []

        if s:
            for j, pitch in enumerate(s.pitches):
                c = chord.Chord.triad(s, j+1)
                name = c.name
                chord_list.append(c)

            triads[key_name] = Key(key_name, tuple(chord_list))
