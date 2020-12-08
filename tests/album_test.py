import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("Axis: Bold as Love", "rock", "Jimi Hendrix")

    def test_album_has_title(self):
        self.assertEqual("Axis: Bold as Love", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Jimi Hendrix", self.album.artist)