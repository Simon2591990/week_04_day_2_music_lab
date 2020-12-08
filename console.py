import pdb
from models.artist import Artist 
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist("Jimi Hendrix")
artist_2 = Artist("Pink FLoyd")
album_1 = Album("Axis: Bold as Love", "rock", artist_1)

#delete all
album_repository.delete_all()
artist_repository.delete_all()

artist_repository.save(artist_1)
artist_repository.save(artist_2)

artist_repository.select_all()
# artist_repository.select(1)
# artist_repository.delete(4)
album_repository.save(album_1)


pdb.set_trace()