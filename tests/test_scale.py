import pytest
import sys

sys.path.append('.')
import src.scale as scale
import src.pitch as pitch

class TestScale():

    def test_new_scale(self):
        obj = scale.Scale('test', (pitch.a, pitch.b, pitch.c))
        assert obj.name() == 'test'

    def test_scale_constants(self):
        assert scale.scales['Cmin'].name() == 'Cmin'
        assert scale.scales['Cmin'].is_minor()
