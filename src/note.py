import src.pitch as pitch

class Note():

    def __init__(self, name, pitch, octave, frequency):
        self._name = name
        self._pitch = pitch
        self._octave = octave
        self._frequency = frequency

    def __eq__(self, other):
        if isInstance(other, Note):
            return self._frequency == other._frequency
        return false

    def name(self):
        return self._name

    def pitch(self):
        return self._pitch

    def octave(self):
        return self._octave

    def frequency(self):
        return self._frequency

# all the notes on a piano from lowest to highest
a = (
    Note('A0', pitch.a, 0, 27.5),
    Note('A1', pitch.a, 1, 55),
    Note('A2', pitch.a, 2, 110),
    Note('A3', pitch.a, 3, 220),
    Note('A4', pitch.a, 4, 440),
    Note('A5', pitch.a, 5, 880),
    Note('A6', pitch.a, 6, 1864.66),
    Note('A7', pitch.a, 7, 3520)
)

a_sharp = (
    Note('A#0', pitch.a_sharp, 0, 29.1353),
    Note('A#1', pitch.a_sharp, 1, 58.2705),
    Note('A#2', pitch.a_sharp, 2, 116.541),
    Note('A#3', pitch.a_sharp, 3, 233.082),
    Note('A#4', pitch.a_sharp, 4, 466.164),
    Note('A#5', pitch.a_sharp, 5, 932.328),
    Note('A#6', pitch.a_sharp, 6, 1864.66),
    Note('A#7', pitch.a_sharp, 7, 3729.31)
)

b_flat = (
    Note('Bb0', pitch.b_flat, 0, 29.1353),
    Note('Bb1', pitch.b_flat, 1, 58.2705),
    Note('Bb2', pitch.b_flat, 2, 116.541),
    Note('Bb3', pitch.b_flat, 3, 233.082),
    Note('Bb4', pitch.b_flat, 4, 466.164),
    Note('Bb5', pitch.b_flat, 5, 932.328),
    Note('Bb6', pitch.b_flat, 6, 1864.66),
    Note('Bb7', pitch.b_flat, 7, 3729.31)
)

b = (
    Note('B0', pitch.b, 0, 30.8677),
    Note('B1', pitch.b, 1, 61.7354),
    Note('B2', pitch.b, 2, 123.471),
    Note('B3', pitch.b, 3, 246.942),
    Note('B4', pitch.b, 4, 493.883),
    Note('B5', pitch.b, 5, 987.767),
    Note('B6', pitch.b, 6, 1975.53),
    Note('B7', pitch.b, 7, 3951.07)
)

c = (
    None,
    Note('C1', pitch.c, 1, 32.7032),
    Note('C2', pitch.c, 2, 65.4064),
    Note('C3', pitch.c, 3, 130.813),
    Note('C4', pitch.c, 4, 261.626),
    Note('C5', pitch.c, 5, 523.251),
    Note('C6', pitch.c, 6, 1046.5),
    Note('C7', pitch.c, 7, 2093),
    Note('C8', pitch.c, 8, 4186.01)
)

c_sharp = (
    None,
    Note('C#1', pitch.c_sharp, 1, 34.6479),
    Note('C#2', pitch.c_sharp, 2, 69.2957),
    Note('C#3', pitch.c_sharp, 3, 138.591),
    Note('C#4', pitch.c_sharp, 4, 277.183),
    Note('C#5', pitch.c_sharp, 5, 554.365),
    Note('C#6', pitch.c_sharp, 6, 1108.73),
    Note('C#7', pitch.c_sharp, 7, 2217.46)
)

d_flat = (
    None,
    Note('Db1', pitch.d_flat, 1, 34.6479),
    Note('Db2', pitch.d_flat, 2, 69.2957),
    Note('Db3', pitch.d_flat, 3, 138.591),
    Note('Db4', pitch.d_flat, 4, 277.183),
    Note('Db5', pitch.d_flat, 5, 554.365),
    Note('Db6', pitch.d_flat, 6, 1108.73),
    Note('Db7', pitch.d_flat, 7, 2217.46)
)

d = (
    None,
    Note('D1', pitch.d, 1, 36.7081),
    Note('D2', pitch.d, 2, 73.4162),
    Note('D3', pitch.d, 3, 146.832),
    Note('D4', pitch.d, 4, 293.665),
    Note('D5', pitch.d, 5, 587.33),
    Note('D6', pitch.d, 6, 1174.66),
    Note('D7', pitch.d, 7, 2349.32)
)

d_sharp = (
    None,
    Note('D#1', pitch.d_sharp, 1, 38.8909),
    Note('D#2', pitch.d_sharp, 2, 77.7817),
    Note('D#3', pitch.d_sharp, 3, 146.832),
    Note('D#4', pitch.d_sharp, 4, 311.127),
    Note('D#5', pitch.d_sharp, 5, 622.254),
    Note('D#6', pitch.d_sharp, 6, 1244.51),
    Note('D#7', pitch.d_sharp, 7, 2489.02)
)

e_flat = (
    None,
    Note('Eb1', pitch.e_flat, 1, 38.8909),
    Note('Eb2', pitch.e_flat, 2, 77.7817),
    Note('Eb3', pitch.e_flat, 3, 146.832),
    Note('Eb4', pitch.e_flat, 4, 311.127),
    Note('Eb5', pitch.e_flat, 5, 622.254),
    Note('Eb6', pitch.e_flat, 6, 1244.51),
    Note('Eb7', pitch.e_flat, 7, 2489.02)
)

e = (
    None,
    Note('E1', pitch.e, 1, 41.2035),
    Note('E2', pitch.e, 2, 82.4069),
    Note('E3', pitch.e, 3, 164.814),
    Note('E4', pitch.e, 4, 329.628),
    Note('E5', pitch.e, 5, 659.255),
    Note('E6', pitch.e, 6, 1318.51),
    Note('E7', pitch.e, 7, 2637.02)
)

f = (
    None,
    Note('F1', pitch.f, 1, 43.6536),
    Note('F2', pitch.f, 2, 87.3071),
    Note('F3', pitch.f, 3, 174.614),
    Note('F4', pitch.f, 4, 349.228),
    Note('F5', pitch.f, 5, 698.456),
    Note('F6', pitch.f, 6, 1396.91),
    Note('F7', pitch.f, 7, 2793.83)
)

f_sharp = (
    None,
    Note('F#1', pitch.f_sharp, 1, 46.2493),
    Note('F#2', pitch.f_sharp, 2, 92.4986),
    Note('F#3', pitch.f_sharp, 3, 184.997),
    Note('F#4', pitch.f_sharp, 4, 369.994),
    Note('F#5', pitch.f_sharp, 5, 739.989),
    Note('F#6', pitch.f_sharp, 6, 1479.98),
    Note('F#7', pitch.f_sharp, 7, 2959.96)
)

g_flat = (
    None,
    Note('Gb1', pitch.g_flat, 1, 46.2493),
    Note('Gb2', pitch.g_flat, 2, 92.4986),
    Note('Gb3', pitch.g_flat, 3, 184.997),
    Note('Gb4', pitch.g_flat, 4, 369.994),
    Note('Gb5', pitch.g_flat, 5, 739.989),
    Note('Gb6', pitch.g_flat, 6, 1479.98),
    Note('Gb7', pitch.g_flat, 7, 2959.96)
)

g = (
    None,
    Note('G1', pitch.g, 1, 48.9995),
    Note('G2', pitch.g, 2, 97.9989),
    Note('G3', pitch.g, 3, 195.998),
    Note('G4', pitch.g, 4, 391.995),
    Note('G5', pitch.g, 5, 783.991),
    Note('G6', pitch.g, 6, 1567.98),
    Note('G7', pitch.g, 7, 3322.44)
)

g_sharp = (
    None,
    Note('G#1', pitch.g_sharp, 1, 51.913),
    Note('G#2', pitch.g_sharp, 2, 103.826),
    Note('G#3', pitch.g_sharp, 3, 207.652),
    Note('G#4', pitch.g_sharp, 4, 415.305),
    Note('G#5', pitch.g_sharp, 5, 830.609),
    Note('G#6', pitch.g_sharp, 6, 1661.22),
    Note('G#7', pitch.g_sharp, 7, 3322.44)
)

a_flat = (
    None,
    Note('Ab1', pitch.a_flat, 1, 51.913),
    Note('Ab2', pitch.a_flat, 2, 103.826),
    Note('Ab3', pitch.a_flat, 3, 207.652),
    Note('Ab4', pitch.a_flat, 4, 415.305),
    Note('Ab5', pitch.a_flat, 5, 830.609),
    Note('Ab6', pitch.a_flat, 6, 1661.22),
    Note('Ab7', pitch.a_flat, 7, 3322.44)
)
