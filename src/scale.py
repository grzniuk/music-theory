import jsonpickle
import src.pitch as pitch
from collections import namedtuple
import typing

class ScaleNotes(typing.NamedTuple):
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
        return self[degree-1]

    def slice(self, slicer):
        notes = list(self)
        return tuple(notes[slicer])
        #return tuple([self.degree(i%7) for i in (start, start+2, start+4)])

class Scale:

    # 1..8 -> notes[0..7] so to dereference decrement degree_number
    def degree_number(self, degree_number):
        return self._notes[degree_number - 1]

    def name(self):
        return self._name

    def is_major(self):
        return self._major

    def is_minor(self):
        return not self._major

    def maj_min(self):
        if self.is_major():
            return 'maj'
        else:
            return 'min'

    def notes(self):
        return self._notes

    def pitch(self):
        return self._pitch

    def tonic(self):
        return self._notes.tonic
    def supertonic(self):
        return self._notes.supertonic
    def mediant(self):
        return self._notes.mediant
    def subdominant(self):
        return self._notes.subdominant
    def dominant(self):
        return self._notes.dominant
    def submediant(self):
        return self._notes.submediant
    def leading(self):
        return self._notes.leading

    def __init__(self, name, notes, pitch=None, major=False):
        self._name = name
        self._notes = notes
        self._pitch = pitch
        self._major = major

    def note_names(self):
        return tuple([note.name() for note in self.notes()])

    def __str__(self):
        return f"{self.name()} ({self.pitch().name()}, {self.maj_min()}): {self.notes()}"

    def __repr__(self):
        return jsonpickle.encode(self)

scales = {

    'Cmaj': Scale(
        "Cmaj",
        ScaleNotes(pitch.c, pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b),
        pitch.c, True
    ),

    'Cmin': Scale(
        "Cmin",
        ScaleNotes(pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat),
        pitch.c, False
    ),

    'C#maj': Scale(
        # C#maj scale uses E in place of E# and B in place of B# (on piano)
        'C#maj',
        ScaleNotes(pitch.c_sharp, pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp, pitch.b_sharp),
        pitch.c_sharp, True
    ),

    'C#min': Scale(
        "C#min",
        ScaleNotes(pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b),
        pitch.c_sharp, False
    ),

    'Dbmaj': Scale(
        "Dbmaj",
        ScaleNotes(pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c),
        pitch.d_flat, True
    ),

    'Dbmin':
        # min scale includes Fb which is absent from piano so we'll skip it
        None,

    'Dmaj': Scale(
        "Dmaj",
        ScaleNotes(pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c_sharp),
        pitch.d, True
    ),

    'Dmin': Scale(
        "Dmin",
        ScaleNotes(pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c),
        pitch.d, False
    ),

    'D#maj':
        # D#maj is a theoretical key so i'll skip it
        None,

    'D#min': Scale(
        # D#min scale uses E in place of E# (on piano)
        'D#min',
        ScaleNotes(pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp),
        pitch.d_sharp, False
    ),

    'Ebmaj': Scale(
        'Ebmaj',
        ScaleNotes(pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d),
        pitch.e_flat, True
    ),

    'Ebmin': Scale(
        # Ebmin scale uses B in place of Cb (on piano)
        'Ebmin',
        ScaleNotes(pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat),
        pitch.e_flat, False
    ),

    'Emaj': Scale(
        "Emaj",
        ScaleNotes(pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d_sharp),
        pitch.e, True
    ),

    'Emin': Scale(
        "Emin",
        ScaleNotes(pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d),
        pitch.e, False
    ),

    'Fmaj': Scale(
        "Fmaj",
        ScaleNotes(pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e),
        pitch.f, True
    ),

    'Fmin': Scale(
        "Fmin",
        ScaleNotes(pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat),
        pitch.f, False
    ),

    'F#maj':
        # F#maj scale includes E# which is absent from piano so we'll skip it
        None,

    'F#min': Scale(
        "F#min",
        ScaleNotes(pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e),
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
        ScaleNotes(pitch.g, pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f_sharp),
        pitch.g, True
    ),

    'Gmin': Scale(
        "Gmin",
        ScaleNotes(pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f),
        pitch.g, False
    ),

    'G#maj':
        # G#maj scale includes E# which is absent from piano so we'll skip it
        None,

    'G#min': Scale(
        "G#min",
        ScaleNotes(pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp),
        pitch.g_sharp, False
    ),

    'Abmaj': Scale(
        "Abmaj",
        ScaleNotes(pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g),
        pitch.a_flat, True
    ),

    'Abmin': Scale(
        # Abmin scale uses B in place of Cb and E in place of Fb (on piano)
        'Abmin',
        ScaleNotes(pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat, pitch.e_flat, pitch.f_flat, pitch.g_flat),
        pitch.a_flat, False
    ),

    'Amaj': Scale(
        "Amaj",
        ScaleNotes(pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g_sharp),
        pitch.a, True
    ),

    'Amin': Scale(
        "Amin",
        ScaleNotes(pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f, pitch.g),
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
        ScaleNotes(pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a),
        pitch.b_flat, True
    ),

    'Bbmin': Scale(
        "Bbmin",
        ScaleNotes(pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat),
        pitch.b_flat, False
    ),

    'Bmaj': Scale(
        "Bmaj",
        ScaleNotes(pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp),
        pitch.b, True
    ),

    'Bmin': Scale(
        "Bmin",
        ScaleNotes(pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a),
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
