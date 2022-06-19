import jsonpickle
import pitch
import scale
import random
import roman_notation

class Chord():

    def __init__(self, name, pitches, major=True, diminished=False, uses_proxy=False):
        self._name = name
        self._pitches = pitches
        self._major = major
        self._diminished = diminished
        self._uses_proxy = uses_proxy

    @property
    def name(self):
        return self._name

    @property
    def pitches(self):
        return self._pitches

    @property
    def major(self):
        return self._major

    @property
    def diminished(self):
        return self._diminished

    @property
    def uses_proxy(self):
        return self._uses_proxy

    @property
    def type(self):
        if self.major:
            return 'maj'
        elif self.diminished:
            return 'dim'
        elif self.minor:
            return 'min'
        else:
            raise ValueError(f'{self.name()} is not a valid chord type - please check values.')

    @property
    def minor(self):
        return not self.major and not self.diminished

    @property
    def includes_alias(self):
        return self._includes_alias

    def __str__(self):
        pitch_names = [x.name for x in self.pitches]
        return f"{self.name}: {'-'.join(pitch_names)}"

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
    def triad(cls, s, degree=1):
        if s:
            # find if the chord is maj/min/dim
            type_str = Chord.classify_by_scale_degree(degree, s.maj_min())

            # set boolean flags
            (is_major, is_diminished) = Chord.boolean_tuple_type(type_str)

            # select the degree pitch from scale, then the next two thirds
            # where a third is two further degrees into the scale
            degree -= 1
            slicer = slice(degree, degree+5, 2)
            pitches = list(s.pitches + s.pitches)[slicer]
            name = pitches[0].name + type_str

            # some piano chords use a different key as a proxy
            # substitute the proxy in _after_ determining the name
            uses_proxy = False
            piano_keys = []
            for i, p in enumerate(pitches):

                # is the pitch found on a piano keyboard?
                if p not in pitch.key_pitches:
                    if pitch.proxy[p.name]:
                        piano_keys.append(pitch.proxy[p.name])
                        uses_proxy = True
                    else:
                        raise IndexError(f'No proxy found for {pitch.name()}.')

                else:
                    piano_keys.append(p)

            return Chord(
                name, piano_keys, is_major, is_diminished, uses_proxy
            )

        else:
            return None

triads = {}

for p1 in pitch.key_pitches:

    # loop for major and minor scales
    for maj_min in ('maj', 'min'):

        # key name e.g. Cmaj, Cmin, C#maj, etc.
        key_name = p1.name + maj_min
        s = scale.scales[key_name]

        if s:
            for j, p2 in enumerate(s.pitches):
                c = Chord.triad(s, j+1)
                name = c.name
                if name in triads.keys():
                    if (triads[name].pitches != c.pitches) and not c.uses_proxy:
                        raise ValueError(f'Conflicting values for {name} chord: {triads[name]} and {c}')
                triads[name] = c

class Progression(tuple):

    def __new__(self, degree_tuple):
        # sanity checks
        for degree in degree_tuple:
            if not isinstance(degree, int):
                degree = roman_notation.from_roman(degree)
                if degree not in range(1, 7):
                    raise ValueError('list values must be integers or roman numerals in range 1-7.')
        return tuple.__new__(Progression, degree_tuple)

progressions = {
    'common': (
        Progression(('I', 'IV', 'V')),
        Progression(('I', 'VI', 'IV', 'V')),
        Progression(('II', 'V', 'I'))
    )
}

def random_common_progression():
    rnd_index = random.randint(0, len(progressions['common']) - 1)
    return progressions['common'][rnd_index]
