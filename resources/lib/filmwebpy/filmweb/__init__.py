# coding=utf-8
from resources.lib.filmwebpy.filmweb._exceptions import FilmwebParserError
from resources.lib.filmwebpy.filmweb.parser import FilmwebHTTP


def Filmweb(access='http'):
    if access == 'http':
        return FilmwebHTTP()
    else:
        raise FilmwebParserError('Unknown data system: %s' % access)
