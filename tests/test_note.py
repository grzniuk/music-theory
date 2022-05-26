import pytest
import sys

sys.path.append('.')
import src.pitch as pitch
import src.note as note

class TestNote():

    def test_new_pitch(self):
        obj = pitch.Pitch('test', 0)
        assert obj.name() == 'test'

    def test_pitch_constants(self):
        assert pitch.c.name() == 'C'
        assert pitch.c != pitch.c_sharp
        assert pitch.c_sharp == pitch.d_flat

    def test_new_note(self):
        obj = note.Note('test', pitch.f, 8, 49)
        assert obj.name() == 'test'
        assert obj.pitch() == pitch.f
        assert obj.pitch() != pitch.g
        assert obj.octave() == 8
        assert obj.octave() != 'handkerchief'
        assert obj.octave() != 7
        assert obj.frequency() == 49
        assert obj.frequency() != 0
