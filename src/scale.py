import jsonpickle
import pitch
from collections import namedtuple
import typing
import roman_notation

class ScalePitches(typing.NamedTuple):
    tonic: pitch.Pitch
    supertonic: pitch.Pitch
    mediant: pitch.Pitch
    subdominant: pitch.Pitch
    dominant: pitch.Pitch
    submediant: pitch.Pitch
    leading: pitch.Pitch

    def __str__(self):
        pitch_strs = [p.name() for p in list(self)]
        return f"{', '.join(pitch_strs)}"

    def __repr__(self):
        return jsonpickle.encode(self)

    def degree(self, degree):
        if not isinstance(degree, int):
            degree = roman_notation.from_roman(degree)
            # is the degree between 1 & 7?
            if degree in range(1, 7):
                return self[degree-1]
        raise IndexError('degree must be an integer or roman numeral in range 1-7')

    @property
    def I(self):
        return self[0]

    @property
    def II(self):
        return self[1]

    @property
    def III(self):
        return self[2]

    @property
    def IV(self):
        return self[3]

    @property
    def V(self):
        return self[4]

    @property
    def VI(self):
        return self[5]

    @property
    def VII(self):
        return self[6]

    def slice(self, slicer):
        pitches = list(self)
        return tuple(pitches[slicer])
        #return tuple([self.degree(i%7) for i in (start, start+2, start+4)])

class Scale:

    def __init__(self, name, pitches, pitch=None, major=False):
        self._name = name
        self._pitches = pitches
        self._major = major

    # 1..7 -> pitches[0..6] so to dereference decrement degree_number
    def degree(self, degree_number):
        if degree_number not in range(1, 7):
            raise ValueError('degree_number: {degree_number} must be in range 1..7.')
        return self.pitches[degree_number - 1]

    @property
    def name(self):
        return self._name

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return not self._major

    def maj_min(self):
        if self.major:
            return 'maj'
        else:
            return 'min'

    @property
    def pitches(self):
        return self._pitches

    @property
    def tonic(self):
        return self._pitches.tonic

    @property
    def I(self):
        return self._pitches.tonic

    @property
    def supertonic(self):
        return self._pitches.supertonic

    @property
    def II(self):
        return self._pitches.supertonic

    @property
    def mediant(self):
        return self._pitches.mediant

    @property
    def III(self):
        return self._pitches.mediant

    @property
    def subdominant(self):
        return self._pitches.subdominant

    @property
    def IV(self):
        return self._pitches.subdominant

    @property
    def dominant(self):
        return self._pitches.dominant

    @property
    def V(self):
        return self._pitches.dominant

    @property
    def submediant(self):
        return self._pitches.submediant

    @property
    def VI(self):
        return self._pitches.submediant

    @property
    def leading(self):
        return self._pitches.leading

    @property
    def VII(self):
        return self._pitches.leading

    def pitch_names(self):
        return tuple([pitch.name for pitch in self.pitches])

    def __str__(self):
        return f"{self.name} ({self.tonic.name}, {self.maj_min()}): {self.pitches}"

    def __repr__(self):
        return jsonpickle.encode(self)

scales = {

    'Cmaj': Scale(
        "Cmaj",
        ScalePitches(pitch.c, pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b),
        pitch.c, True
    ),

    'Cmin': Scale(
        "Cmin",
        ScalePitches(pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat),
        pitch.c, False
    ),

    'C#maj': Scale(
        # C#maj scale uses E in place of E# and B in place of B# (on piano)
        'C#maj',
        ScalePitches(pitch.c_sharp, pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp, pitch.b_sharp),
        pitch.c_sharp, True
    ),

    'C#min': Scale(
        "C#min",
        ScalePitches(pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b),
        pitch.c_sharp, False
    ),

    'Dbmaj': Scale(
        "Dbmaj",
        ScalePitches(pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c),
        pitch.d_flat, True
    ),

    'Dbmin':
        # min scale includes Fb which is absent from piano so we'll skip it
        None,

    'Dmaj': Scale(
        "Dmaj",
        ScalePitches(pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c_sharp),
        pitch.d, True
    ),

    'Dmin': Scale(
        "Dmin",
        ScalePitches(pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c),
        pitch.d, False
    ),

    'D#maj':
        # D#maj is a theoretical key so i'll skip it
        None,

    'D#min': Scale(
        # D#min scale uses E in place of E# (on piano)
        'D#min',
        ScalePitches(pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp),
        pitch.d_sharp, False
    ),

    'Ebmaj': Scale(
        'Ebmaj',
        ScalePitches(pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d),
        pitch.e_flat, True
    ),

    'Ebmin': Scale(
        # Ebmin scale uses B in place of Cb (on piano)
        'Ebmin',
        ScalePitches(pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat),
        pitch.e_flat, False
    ),

    'Emaj': Scale(
        "Emaj",
        ScalePitches(pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d_sharp),
        pitch.e, True
    ),

    'Emin': Scale(
        "Emin",
        ScalePitches(pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d),
        pitch.e, False
    ),

    'Fmaj': Scale(
        "Fmaj",
        ScalePitches(pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e),
        pitch.f, True
    ),

    'Fmin': Scale(
        "Fmin",
        ScalePitches(pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat),
        pitch.f, False
    ),

    'F#maj':
        # F#maj scale includes E# which is absent from piano so we'll skip it
        None,

    'F#min': Scale(
        "F#min",
        ScalePitches(pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e),
        pitch.f_sharp, False
    ),

    'Gbmaj':
        # Gbmaj scale includes Cb which is absent from piano so we'll skip it
        None,

    'Gbmin':
        # Gbmin is theoretical so we'll skip it
        None,

    'Gmaj': Scale(
        "Gmaj",
        ScalePitches(pitch.g, pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f_sharp),
        pitch.g, True
    ),

    'Gmin': Scale(
        "Gmin",
        ScalePitches(pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f),
        pitch.g, False
    ),

    'G#maj':
        # G#maj scale includes E# which is absent from piano so we'll skip it
        None,

    'G#min': Scale(
        "G#min",
        ScalePitches(pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp),
        pitch.g_sharp, False
    ),

    'Abmaj': Scale(
        "Abmaj",
        ScalePitches(pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g),
        pitch.a_flat, True
    ),

    'Abmin': Scale(
        # Abmin scale uses B in place of Cb and E in place of Fb (on piano)
        'Abmin',
        ScalePitches(pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat, pitch.e_flat, pitch.f_flat, pitch.g_flat),
        pitch.a_flat, False
    ),

    'Amaj': Scale(
        "Amaj",
        ScalePitches(pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g_sharp),
        pitch.a, True
    ),

    'Amin': Scale(
        "Amin",
        ScalePitches(pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f, pitch.g),
        pitch.a, False
    ),

    'A#maj':
        # A#maj is theoretical so we'll skip it
        None,

    'A#min':
        # A#min scale includes B# which is absent from piano so we'll skip it
        None,

    'Bbmaj': Scale(
        "Bbmaj",
        ScalePitches(pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a),
        pitch.b_flat, True
    ),

    'Bbmin': Scale(
        "Bbmin",
        ScalePitches(pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat),
        pitch.b_flat, False
    ),

    'Bmaj': Scale(
        "Bmaj",
        ScalePitches(pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp),
        pitch.b, True
    ),

    'Bmin': Scale(
        "Bmin",
        ScalePitches(pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a),
        pitch.b, False
    )
}

# major = { key: scales[key].maj for key in scales.keys() }
# minor = { key: scales[key].min for key in scales.keys() }

# Ancient Greek modes

dorian = Scale(
    "dorian",
    (pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b, pitch.c),
    pitch.d, False
)

phrygian = Scale(
    "phrygian",
    (pitch.e, pitch.f, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d),
    pitch.e, False
)

lydian = Scale(
    "lydian",
    (pitch.f, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d, pitch.e),
    pitch.f, True
)

ionian = Scale(
    "ionian",
    (pitch.c, pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b),
    pitch.c, True
)
