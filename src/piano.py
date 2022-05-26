import octave

class Piano:

    # there are 7.25 octaves but we'll round up to simplify
    num_octaves = 8
    octaves = [num_octaves]
    octaves = (
        (Octave.notes()),
        (Octave.notes()),
        (Octave.notes()),
        (Octave.notes()),
        (Octave.notes()),
        (Octave.notes()),
        (Octave.notes()),
        (Octave.notes()[0:3]) # 'A', 'Bb', 'B', 'C'
    )
    num_keys = 88
