import pdb
from models.artist import Artist 

import repositories.artist_repository as artist_repository

artist_1 = Artist("Jimi Hendrix")
artist_2 = Artist("Pink FLoyd")

#delete all
artist_repository.delete_all()

artist_repository.save(artist_1)
artist_repository.save(artist_2)

# artist_repository.select_all()
# artist_repository.select(1)
# artist_repository.delete(4)
