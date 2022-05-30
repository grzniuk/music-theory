from operator import itemgetter

class Octave:

    # just a string representing the note name
    __slots__ = [
        'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'Ab'
    ]

    pitches = property()

    white_notes = property(itemgetter(0, 2, 3, 5, 7, 8, 10))

    black_notes = property(itemgetter(1, 4, 6, 9, 11))
