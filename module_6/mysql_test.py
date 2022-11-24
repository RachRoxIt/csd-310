import mysql.connector
from mysql.connector import errorcode


config = {
	"user": "root",
	"password": "Yodapop311!",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}	

try:
 	db = mysql.connector.connect(**config)
 
	print("Database user {root} connected to MYSQL on host {127.0.0.1} with database {movies}".format(config["user"], config["host"], config["database"]))

	input("Press any key to continue...")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The speficified database does not exist")

	else:
		print(err)
finally:
	db.close()








 
