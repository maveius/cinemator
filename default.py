# coding=utf-8
import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
from resources.lib.filmwebpy.filmweb import Filmweb
from resources.lib.filmwebpy.filmweb.func import get_list_genres

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

fw = Filmweb('http')

base_url = sys.argv[0]
args = urlparse.parse_qs(sys.argv[2][1:])


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


def parse_movies(page_id, genres_id):
    movies = fw.search_filtered_movie(title=None, page=page_id, genre_id=genres_id, search_type='film')
    movies_all_items = 0
    for idx in range(len(movies)):
        movie = movies[idx];
        movies_all_items = movie.pages
        item = xbmcgui.ListItem(movie['title'])
        item.setArt({'poster': movie.get('poster')})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url='', listitem=item)

    return movies_all_items


mode = args.get('mode', None)

if mode is None:
    genres = get_list_genres()

    for i in range(len(genres)):
        id = genres[i]['genre_id'].encode('utf-8')
        url = build_url({'mode': 'folder', 'foldername': id, 'page': 1})
        li = xbmcgui.ListItem(genres[i]['genre_name'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'folder', 'foldername': 'wszystkie'})
    li = xbmcgui.ListItem('wszystkie...')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
    genre_id = args['foldername'][0]
    page = int(args['page'][0])

    genres_page_url = build_url({'mode': None})
    list_item = xbmcgui.ListItem('...')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=genres_page_url, listitem=list_item, isFolder=True)

    if page > 1:
        url = build_url({'mode': 'folder', 'foldername': genre_id, 'page': (page - 1)})
        list_item = xbmcgui.ListItem('... Poprzednie')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item, isFolder=True)

    total = int(parse_movies(page, genre_id))

    if page < total:
        url = build_url({'mode': 'folder', 'foldername': genre_id, 'page': (page + 1)})
        list_item = xbmcgui.ListItem('Następne ...')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)
