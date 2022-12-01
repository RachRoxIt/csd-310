"""import statements"""
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "port": "3006",
    "user": "root",
    "password": "Yodapop311!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}
"""This is a try/catch block for handling any potential MySql database errors"""
try:
    db = mysql.connector.connect(**config)  # connect to the movies database

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"]
                                                                                      , config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()


def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the data set and out put the results to the terminal window.
    # inner join query
    cursor.execute("SELECT film.film_name as Name, film.film_director as Director, "
                   "genre.genre_name as Genre, studio.studio_name as 'Studio Name' "
                   "from film "
                   "INNER JOIN genre ON film.genre_id=genre.genre_id "
                   "INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()
    print("\n  -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1],
                                                                                         film[2], film[3]))


def new_movie(cursor):
    add_movie = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, " \
                "studio_id, genre_id) " \
                "VALUES ('Jurassic World', 2015, 124, 'Collin Trevorrow', (SELECT studio_id FROM studio " \
                "WHERE studio_name = 'Universal Pictures'), (SELECT genre_id FROM genre WHERE " \
                "genre_name = 'Drama'))"
    cursor.execute(add_movie)
    db.commit()


def update_genre(cursor):
    new_genre = "UPDATE film SET film_id = 2, genre_id = 1 WHERE genre_id = 2"
    cursor.execute(new_genre)
    db.commit()


def delete_movie(cursor):
    deletes_movie = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(deletes_movie)
    db.commit()


cursor = db.cursor()


show_films(cursor, "-- DISPLAYING FILMS --")

new_movie(cursor)
show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")

update_genre(cursor)
show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror -- --")

delete_movie(cursor)
show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE --")

db.close()
