import pdb
from models.artist import Artist 
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist('Jimi Hendrix')
artist_2 = Artist('Pink FLoyd')
album_1 = Album("Axis: Bold as Love", "rock", artist_1)
album_2 = Album("Electric Ladyland", "rock", artist_1)
album_3 = Album("Jimi Hendrix Experience", "rock", artist_1)

#delete all
# album_repository.delete_all()
# artist_repository.delete_all()

# artist_repository.save(artist_1)
# artist_repository.save(artist_2)
# # artist_repository.select_all()
# # artist_repository.select(1)
# # artist_repository.delete(4)

# # artist_2.name = 'Fink Ployd'

# # artist_repository.update(artist_2)

# # album_1.genre = 'hippy music'

# album_repository.save(album_1)
# album_repository.save(album_2)
# album_repository.save(album_3)

# artist_repository.albums(artist_1)

# # album_repository.delete(10)



# pdb.set_trace()
