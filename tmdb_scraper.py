import os
# set here the path where you want the scraped folders to be saved!
poster_folder='posters_final/'
if poster_folder.split('/')[0] in os.listdir('./'):
    print('Folder already exists')
else:
    os.mkdir('./'+poster_folder)

# For the purpose of this example, i will be working with the 1999 Sci-Fi movie - "The Matrix"!
import tmdbsimple as tmdb
api_key = 'fef700e782c3f8e5633313fc10ecfe12' #Enter your own API key here to run the code below. 


tmdb.API_KEY = api_key #This sets the API key setting for the tmdb object
search = tmdb.Search() #this instantiates a tmdb "search" object which allows your to search for the movie
import os.path
# These functions take in a string movie name i.e. like "The Matrix" or "Interstellar"
# What they return is pretty much clear in the name - Poster, ID , Info or genre of the Movie!
def grab_poster_tmdb(movie):
    response = search.movie(query=movie)
    id=response['results'][0]['id']
    movie = tmdb.Movies(id)
    posterp=movie.info()['poster_path']
    title=movie.info()['original_title']
    if os.path.isfile(poster_folder+title+'.jpg '):
        return
    url='image.tmdb.org/t/p/original'+posterp
    title='_'.join(title.split(' '))
    strcmd='wget -O '+poster_folder+title+'.jpg '+url
    os.system(strcmd)

def get_movie_id_tmdb(movie):
    response = search.movie(query=movie)
    movie_id=response['results'][0]['id']
    return movie_id

def get_movie_info_tmdb(movie):
    response = search.movie(query=movie)
    id=response['results'][0]['id']
    movie = tmdb.Movies(id)
    info=movie.info()
    return info

def get_movie_genres_tmdb(movie):
    response = search.movie(query=movie)
    id=response['results'][0]['id']
    movie = tmdb.Movies(id)
    genres=movie.info()['genres']
    return genres

"""print get_movie_genres_tmdb("The Matrix")

info=get_movie_info_tmdb("The Matrix")
print "All the Movie information from TMDB gets stored in a dictionary with the following keys for easy access -"
# print info.keys()

info=get_movie_info_tmdb("The Matrix")
print info['tagline']

import imdb
# Create the IMDB object that will be used to access the IMDb's database.
imbd_object = imdb.IMDb() # by default access the web.

# Search for a movie (get a list of Movie objects).
results = imbd_object.search_movie('The Matrix')
#print(len(results))
# As this returns a list of all movies containing the word "The Matrix", we pick the first element
movie = results[0]

print results

imbd_object.update(movie)

print "All the information we can get about this movie from IMDB-"
# print movie.keys()

print "The genres for The Matrix pulled from IMDB are -",movie['genres']
print "The genres for The Matrix pulled from TMDB are -",get_movie_genres_tmdb("The Matrix")

"""

all_movies=tmdb.Movies()

top_movies=all_movies.popular()

print(len(top_movies['results']))








#try:
#    search.movie(query=movie) #An API request
#except:
#    try:
#        time.sleep(10) #sleep for a bit, to give API requests a rest.
#        search.movie(query=<i>movie_name</i>) #Make second API request
#    except:
#        print "Failed second attempt too, check if there's any error in request"
#time.sleep(1)