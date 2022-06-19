import pitch as p
#import note as n
import scale as s
import chord as c
import key as k

from json import dump, JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

pitch = {
    'c': p.c,
    'c_sharp': p.c_sharp,
    'd_flat': p.d_flat,
    'd': p.d,
    'd_sharp': p.d_sharp,
    'e_flat': p.e_flat,
    'e': p.e,
    'f': p.f,
    'f_sharp': p.f_sharp,
    'g_flat': p.g_flat,
    'g': p.g,
    'g_sharp': p.g_sharp,
    'a_flat': p.a_flat,
    'a': p.a,
    'a_sharp': p.a_sharp,
    'b_flat': p.b_flat,
    'b': p.b
}

filename = 'json/pitch.json'
with open(filename, 'w', encoding='utf8') as json_file:
    dump(pitch, json_file, indent=4, cls=MyEncoder)

scales = s.scales
filename = 'json/scale.json'
with open(filename, 'w', encoding='utf8') as json_file:
    dump(scales, json_file, indent=4, cls=MyEncoder)

chords = {}
chords['triads'] = c.triads
filename = 'json/chords.json'
with open(filename, 'w', encoding='utf8') as json_file:
    dump(chords, json_file, indent=4, cls=MyEncoder)

keys = {}
keys['triads'] = k.triads
filename = 'json/keys.json'
with open(filename, 'w', encoding='utf8') as json_file:
    dump(keys, json_file, indent=4, cls=MyEncoder)
