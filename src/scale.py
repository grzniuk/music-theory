import src.pitch as pitch
from enum import Enum

class Scale:

    # the scale should be eight notes starting and finishing on the same note in adjacent octaves
    _notes = (7)

    # degree name indices
    tonic_index = 0
    supertonic_index = 1
    mediant_index = 2
    subdominant_index = 3
    dominant_index = 4
    submediant_index = 5
    leading_tone_index = 6

    # 1..8 -> notes[0..7] so to dereference decrement degree_number
    def degree_number(self, degree_number):
        return self._notes[degree_number - 1]

    def name(self):
        return self._name

    def is_major(self):
        return self._major

    def notes(self):
        return self._notes

    def tonic(self):
        return self._notes[0]
    def supertonic(self):
        return self._notes[1]
    def mediant(self):
        return self._notes[2]
    def subdominant(self):
        return self._notes[3]
    def dominant(self):
        return self._notes[4]
    def submediant(self):
        return self._notes[5]
    def leading_tone(self):
        return self._notes[6]

    def __init__(self, name, notes):
        self._name = name
        self._notes = notes

class Key(Enum):
    MAJ = 0
    MIN = 1

C = {
    Key.MAJ: Scale(
        "Cmaj",
        (pitch.c, pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b)
    ),
    Key.MIN: Scale(
        "Cmin",
        (pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat)
    )
}

C_sharp = {
    # I haven't implemented E# so comment this one out
    # Key.MAJ: Scale(
    #     "C#maj",
    #     (pitch.c_sharp, pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.a_sharp, pitch.b_sharp)
    # ),
    Key.MAJ: None,
    Key.MIN: Scale(
        "C#min",
        (pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.a, pitch.b)
    )
}

D_flat = {
    Key.MAJ: Scale(
        "Dbmaj",
        (pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c)
    ),
    # I haven't implemented Fb so comment this one out
    # Key.MIN: Scale(
    #     "Dbmin",
    #     (pitch.d_flat, pitch.e_flat, pitch.f_flat, pitch.g_flat, pitch.a_flat, pitch.a, pitch.c_flat)
    Key.MIN: None
}

D = {
    Key.MAJ: Scale(
        "Dmaj",
        (pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c_sharp)
    ),
    Key.MIN: Scale(
        "Dmin",
        (pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c)
    )
}

D_sharp = {
    # D#maj is a theoretical key
    Key.MAJ: None,
    # I haven't implemented E# so comment this one out
    # Key.MIN: Scale(
    #     "D#min",
    #     (pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp)
    # )
    Key.MIN: None
}

E_flat = {
    Key.MAJ: Scale(
        "Ebmaj",
        (pitch.e_flat, pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d)
    ),
    # I haven't implemented Cb so comment this one out
    # Key.MIN: Scale(
    #     "Ebmin",
    #     (pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat)
    # )
    Key.MIN: None
}

E = {
    Key.MAJ: Scale(
        "Emaj",
        (pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d_sharp),
    ),
    Key.MIN: Scale(
        "Emin",
        (pitch.e, pitch.f_sharp, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d)
    )
}

F = {
    Key.MAJ: Scale(
        "Fmaj",
        (pitch.f, pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e)
    ),
    Key.MIN: Scale(
        "Fmin",
        (pitch.f, pitch.g, pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat)
    )
}

F_sharp = {
    # I haven't implemented E# so comment this one out
    # Key.MAJ: Scale(
    #     "F#maj",
    #     (pitch.f_sharp, pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e_sharp)
    # ),
    Key.MAJ: None,
    Key.MIN: Scale(
        "F#min",
        (pitch.f_sharp, pitch.g_sharp, pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e)
    )
}

G_flat = {
    # I haven't implemented c_flat so comment this one out
    # Key.MAJ: Scale(
    #     "Gbmaj",
    #     (pitch.g_flat, pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat, pitch.e_flat, pitch.f)
    # ),
    Key.MAJ: None,
    # Gbmin is theoretical
    Key.MIN: None
}

G = {
    Key.MAJ: Scale(
        "Gmaj",
        (pitch.g, pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f_sharp)
    ),
    Key.MIN: Scale(
        "Gmin",
        (pitch.g, pitch.a, pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f)
    )
}

G_sharp = {
    # I haven't implemented E# so comment this one out
    # Key.MAJ: Scale(
    #     "G#maj",
    #     (pitch.g_sharp, pitch.a_sharp, pitch.b_sharp, pitch.c_sharp, pitch.d_sharp, pitch.e_sharp, pitch.f_sharp)
    # ),
    Key.MAJ: None,
    Key.MIN: Scale(
        "Abmin",
        (pitch.g_sharp, pitch.a_sharp, pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.g)
    )
}

A_flat = {
    Key.MAJ: Scale(
        "Abmaj",
        (pitch.a_flat, pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g)
    ),
    # I haven't implemented Fb so comment this one out
    # Key.MIN: Scale(
    #     "Abmin",
    #     (pitch.a_flat, pitch.b_flat, pitch.c_flat, pitch.d_flat, pitch.e_flat, pitch.f_flat, pitch.g_flat)
    # )
    Key.MIN: None
}

A = {
    Key.MAJ: Scale(
        "Amaj",
        (pitch.a, pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g_sharp)
    ),
    Key.MIN: Scale(
        "Amin",
        (pitch.a, pitch.b, pitch.c, pitch.d, pitch.e, pitch.f, pitch.g)
    )
}

A_sharp = {
    # A#maj is theoretical
    Key.MAJ: None,
    # B# isn't on a piano keyboard so I ignore it - comment out this scale
    # Key.MIN: Scale(
    #     "A#min",
    #     (pitch.a_sharp, pitch.b_sharp, pitch.c_sharp, pitch.d_sharp, pitch.e_sharp, pitch.f_sharp, pitch.g_sharp)
    # )
    Key.MIN: None
}

B_flat = {
    Key.MAJ: Scale(
        "Bbmaj",
        (pitch.b_flat, pitch.c, pitch.d, pitch.e_flat, pitch.f, pitch.g, pitch.a)
    ),
    Key.MIN: Scale(
        "Bbmin",
        (pitch.b_flat, pitch.c, pitch.d_flat, pitch.e_flat, pitch.f, pitch.g_flat, pitch.a_flat)
    )
}

B = {
    Key.MAJ: Scale(
        "Bmaj",
        (pitch.b, pitch.c_sharp, pitch.d_sharp, pitch.e, pitch.f_sharp, pitch.g_sharp, pitch.a_sharp)
    ),
    Key.MIN: Scale(
        "Bmin",
        (pitch.b, pitch.c_sharp, pitch.d, pitch.e, pitch.f_sharp, pitch.g, pitch.a)
    )
}

indices = (
    'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 
    'Ab', 'A', 'A#', 'Bb', 'B'
)
scales = (
    C, C_sharp, D_flat, D, D_sharp, E_flat, E, F, F_sharp, G_flat, G, G_sharp,
    A_flat, A, A_sharp, B_flat, B
)
major = [pitch[Key.MAJ] for pitch in scales]
minor = [pitch[Key.MIN] for pitch in scales]
all = major + minor

# Ancient Greek modes

dorian = Scale( "dorian", (pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b, pitch.c) )

phrygian = Scale( "phrygian", (pitch.e, pitch.f, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d) )

lydian = Scale( "lydian", (pitch.f, pitch.g, pitch.a, pitch.b, pitch.c, pitch.d, pitch.e) )

ionian = Scale( "ionian", (pitch.c, pitch.d, pitch.e, pitch.f, pitch.g, pitch.a, pitch.b) )
