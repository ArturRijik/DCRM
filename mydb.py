import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'legacymarik0805',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE ali")

print("Masha Allah!")
