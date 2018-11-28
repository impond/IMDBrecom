import os
import tmdbsimple as tmdb

api_key = 'fef700e782c3f8e5633313fc10ecfe12' #Enter your own API key here to run the code below. 
tmdb.API_KEY = api_key

all_movies=tmdb.Movies()

top_movies=all_movies.popular()

print(len(top_movies['results']))

top20_movs=top_movies['results']

first_movie=top20_movs[0]
print "Here is all the information you can get on this movie - "
print first_movie
print "\n\nThe title of the first movie is - ", first_movie['title']

for i in range(len(top20_movs)):
	mov=top20_movs[i]
	title=mov['title']
	print title
	if i==4:
		break

for i in range(len(top20_movs)):
    mov=top20_movs[i]
    genres=mov['genre_ids']
    print genres
    if i==4:
        break

# Create a tmdb genre object!
genres=tmdb.Genres()
# the list() method of the Genres() class returns a listing of all genres in the form of a dictionary.
print tmdb.Genres()

list_of_genres=genres(list)