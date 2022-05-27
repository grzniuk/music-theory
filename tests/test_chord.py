import pytest
import sys

sys.path.append('.')
import src.scale as scale
import src.chord as chord

class TestChord():

    def test_new_chord(self):
        obj = scale.Scale('test', scale.scales['B'].maj)
        assert obj.name() == 'test'

    def test_chord_constants(self):
        assert len(chord.major) > 0
        cmaj = chord.major['C']
        print(cmaj)
        cmin = chord.minor['C']
        print(cmin)
