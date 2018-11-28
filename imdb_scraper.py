import imdb
# Create the IMDB object that will be used to access the IMDb's database.
imbd_object = imdb.IMDb() # by default access the web.

# Search for a movie (get a list of Movie objects).
results = imbd_object.search_movie('The Matrix')
#print(len(results))
# As this returns a list of all movies containing the word "The Matrix", we pick the first element
movie = results[0]

imbd_object.update(movie)

print "All the information we can get about this movie from IMDB-"
print movie.keys()

import tmdb_scraper

print "The genres for The Matrix pulled from IMDB are -",movie['genres']
print "The genres for The Matrix pulled from TMDB are -",get_movie_genres_tmdb("The Matrix")