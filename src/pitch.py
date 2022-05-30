import jsonpickle

class Pitch():

    white_positions = (0, 2, 4, 5, 7, 9, 11)

    def __init__(self, name, position):
        self._name = name
        self._position = position

    def name(self):
        return self._name

    def position(self):
        return self._position

    def __eq__(self, other):
        if isinstance(other, Pitch):
            return self._position == other._position
        return False

    def is_white(self):
        return self._position in white_positions

    def is_black(self):
        return self._position not in white_positions

    def __str__(self):
        return self.name()

    def __repr__(self):
        return jsonpickle.encode(self)

c = Pitch('C', 0)
c_sharp = Pitch('C#', 1)
d_flat = Pitch('Db', 1)
d = Pitch('D', 2)
d_sharp = Pitch('D#', 3)
e_flat = Pitch('Eb', 3)
e = Pitch('E', 4)
f = Pitch('F', 5)
f_sharp = Pitch('F#', 6)
g_flat = Pitch('Gb', 6)
g = Pitch('G', 7)
g_sharp = Pitch('G#', 8)
a_flat = Pitch('Ab', 8)
a = Pitch('A', 9)
a_sharp = Pitch('A#', 10)
b_flat = Pitch('Bb', 10)
b = Pitch('B', 11)

key_pitches = (
    c, c_sharp, d_flat, d, d_sharp, e_flat, e, f, f_sharp, g_flat, g, g_sharp,
    a_flat, a, a_sharp, b_flat, b
)

b_sharp = Pitch('B#', -1)
c_flat = Pitch('Cb', -1)
e_sharp = Pitch('E#', -1)
f_flat = Pitch('Fb', -1)

test = 1

non_key_pitches = (
    b_sharp, c_flat, e_sharp, f_flat
)

proxy = {
    'B#': b,
    'Cb': b,
    'E#': e,
    'Fb': e
}

# octave_sharp = (c, c_sharp, d, d_sharp, e, f, f_sharp, g, g_sharp, a, a_sharp, b)
# octave_flat = (c, d_flat, d, e_flat, e, f, g_flat, g, a_flat, a, b_flat, b)
