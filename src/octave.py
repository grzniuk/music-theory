class Octave:

    # just a string representing the note name - change to object later
    notes = (
        'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'Ab'
    )

    @classmethod
    def notes(cls):
        return notes

    @classmethod
    def white_notes(cls):
        return notes[0, 2:3, 5, 7:8, 10]

    @classmethod
    def black_notes(cls):
        return notes[1, 4, 6, 9, 11]
