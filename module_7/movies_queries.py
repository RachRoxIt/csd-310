#Rachel Cewe
#11/29/22
#Module 7.2 Table Queries
#https://github.com/RachRoxIt/csd-310/blob/main/module_7/movies_queries.py


import mysql.connector
from mysql.connector import errorcode

config = {
    "port": "3006",
    "user": "root",
    "password": "Yodapop311!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
    config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)


import mysql.connector
from mysql.connector import errorcode

config = {
    "port": "3006",
    "user": "root",
    "password": "Yodapop311!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
    config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

print(" -- DISPLAYING Studio RECORDS -- ")
cursor = db.cursor()
StudioQuery = "SELECT studio_id, studio_name FROM studio"
cursor.execute(StudioQuery)
studios = cursor.fetchall()
for studio in studios:
	print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


print(" -- DISPLAYING Genre RECORDS -- ")
cursor = db.cursor()
GenreQuery = "SELECT genre_id, genre_name FROM genre"
cursor.execute(GenreQuery)
genres = cursor.fetchall()
for genre in genres:
	print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))


print(" -- DISPLAYING Short Film RECORDS -- ")
cursor = db.cursor()
SFilmQuery = "SELECT film_name, film_runtime FROM film"
cursor.execute(SFilmQuery)
films = cursor.fetchall()
for film in films:
	print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))


print(" -- DISPLAYING Director RECORDS -- ")
cursor = db.cursor()
DirectorQuery = "SELECT genre_id, genre_name FROM genre"
cursor.execute(DirectorQuery)
directors = cursor.fetchall()
for director in directors:
	print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))


db.close()


    
