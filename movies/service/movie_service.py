__author__ = 'Rashed'
import csv

from movies.models import Movie,Link, Rating


def insert_movies():
    header = ('title', 'geners')
    with open('./ml-latest-small/movies.csv', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            movie = dict(zip(header, row[1:]))
            Movie.objects.create(**movie)


def insert_links():
    header = ('movie_id','imdbid', 'tmdbid')
    with open('./ml-latest-small/links.csv', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                row = map(int, row)
                print(row)
                links = dict(zip(header, row))
                Link.objects.create(**links)
            except ValueError :
                print('Some error in {}')



def insert_rating():
    header = ('movie_id','rating')
    with open('./ml-latest-small/ratings.csv', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                row = [float(x) for x in row[1:3]]
                row = [int(row[0]), row[1]]
                # import pdb
                # pdb.set_trace()
                ratings = dict(zip(header, row))
                Rating.objects.create(**ratings)
            except ValueError :
                print('Some error in {}')



def insert_all():
    insert_movies()
    insert_links()
    insert_rating()