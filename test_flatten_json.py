import unittest
import flatten_json 

from flatten_json import flatten

class TestFlattenJson(unittest.TestCase):
    def test_flatten(self):
        # Testing a flat json object
        self.assertDictEqual({"a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "test",
                "f": {
                    "g": "deeper",
                    "h": {
                        "node": 24,
                        "visible": True
                        },
                    "i": False
                    "j": {
                        "elem": 34
                        "anga": False,
                        "last": True
                        }
                    }
                }
            },
            {'a': 1,
            'b': True,
            'c.d': 3,
            'c.e': 'test',
            'c.f.g': 'deeper',
            'c.f.h': 24,
            'c.f.i': False
            })

