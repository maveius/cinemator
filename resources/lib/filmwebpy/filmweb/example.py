from resources.lib.filmwebpy.filmweb import Filmweb
from resources.lib.filmwebpy.filmweb.func import get_list_genres

fw = Filmweb('http')

list = get_list_genres()

for i in range(len(list)):
    if list[i]['genre_name'] == 'komedia rom.':
        print list[i]
        #['genre_name']

found_movies = fw.search_filtered_movie(title=None, page=1, genre_id=30, search_type='film')

for i in range(len(found_movies)):
    print found_movies[i]['title'], found_movies[i].get('poster')
