import unittest

from models.artist import Artist

class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Jimi Hendrix")
        

    def test_artist_has_name(self):
        self.assertEqual("Jimi Hendrix", self.artist.name)