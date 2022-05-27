import src.pitch as pitch
from collections import namedtuple

class Scale:

    # the scale should be eight notes starting and finishing on the same note in adjacent octaves
    _notes = namedtuple(
        'Notes',
        'tonic supertonic mediant subdominant dominant submediant leading'
    )

    # 1..8 -> notes[0..7] so to dereference decrement degree_number
    def degree_number(self, degree_number):
        return self._notes[degree_number - 1]

    def name(self):
        return self._name

    def is_major(self):
        return self._major

    def is_minor(self):
        return not self._major

    def major_minor(self):
        if self.is_major:
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
        note_str = ", ".join(self.note_names())
        return f"{self.name()} ({self.pitch().name()}, self.major_minor()): {note_str}"

    def __repr__(self):
        return json.dumps(dict(self))

PitchScales = namedtuple('PitchScales', 'maj min')

scales = {
    'C': PitchScales(
        Scale(
            "Cmaj",
            (pitch.c, pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b),
            pitch.c, True
        ),
        Scale(
            "Cmin",
            (pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat),
            pitch.c, False
        )
    ),

    'C#': PitchScales(
        # maj scale includes E# which is absent from piano so we'll skip it
        None,
        Scale(
            "C#min",
            (pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.a, pitch.b),
            pitch.c_sharp, True
        )
    ),

    'Db': PitchScales(
        Scale(
            "Dbmaj",
            (pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c),
            pitch.d_flat, True
        ),
        # min scale includes Fb which is absent from piano so we'll skip it
        None
    ),

    'D': PitchScales(
        Scale(
            "Dmaj",
            (pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c_sharp),
            pitch.d, True
        ),
        Scale(
            "Dmin",
            (pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c),
            pitch.d, False
        )
    ),

    'D#': PitchScales(
        # D#maj is a theoretical key so i'll skip it
        None,
        # maj scale includes E# which is absent from piano so we'll skip it
        None
    ),

    'Eb': PitchScales(
        Scale(
            "Ebmaj",
            (pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d),
            pitch.e_flat, True
        ),
        # min scale includes Cb which is absent from piano so we'll skip it
        None
    ),

    'E': PitchScales(
        Scale(
            "Emaj",
            (pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d_sharp),
            pitch.e, True
        ),
        Scale(
            "Emin",
            (pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d),
            pitch.e, False
        )
    ),

    'F': PitchScales(
        Scale(
            "Fmaj",
            (pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e),
            pitch.f, True
        ),
        Scale(
            "Fmin",
            (pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat),
            pitch.f, False
        )
    ),

    'F#': PitchScales(
        # maj scale includes E# which is absent from piano so we'll skip it
        None,
        Scale(
            "F#min",
            (pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e),
            pitch.f_sharp, False
        )
    ),

    'Gb': PitchScales(
        # maj scale includes Cb which is absent from piano so we'll skip it
        None,
        # Gbmin is theoretical so we'll skip it
        None
    ),

    'G': PitchScales(
        Scale(
            "Gmaj",
            (pitch.g, pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f_sharp),
            pitch.g, True
        ),
        Scale(
            "Gmin",
            (pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f),
            pitch.g, False
        )
    ),

    'G#': PitchScales(
        # maj scale includes E# which is absent from piano so we'll skip it
        None,
        Scale(
            "G#min",
            (pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.g),
            pitch.g_sharp, False
        )
    ),

    'Ab': PitchScales(
        Scale(
            "Abmaj",
            (pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g),
            pitch.a_flat, True
        ),
        # min scale includes Fb which is absent from piano so we'll skip it
        None
    ),

    'A': PitchScales(
        Scale(
            "Amaj",
            (pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g_sharp),
            pitch.a, True
        ),
        Scale(
            "Amin",
            (pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f, pitch.g),
            pitch.a, False
        )
    ),

    'A#': PitchScales(
        # A#maj is theoretical so we'll skip it
        None,
        # min scale includes B# which is absent from piano so we'll skip it
        None
    ),

    'Bb': PitchScales(
        Scale(
            "Bbmaj",
            (pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a),
            pitch.b_flat, True
        ),
        Scale(
            "Bbmin",
            (pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat),
            pitch.b_flat, False
        )
    ),

    'B': PitchScales(
        Scale(
            "Bmaj",
            (pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp),
            pitch.b, True
        ),
        Scale(
            "Bmin",
            (pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a),
            pitch.b, False
        )
    )
}

major = { key: scales[key].maj for key in scales.keys() }
minor = { key: scales[key].min for key in scales.keys() }

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
