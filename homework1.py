
import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	cars = [
	('Ford','Fiesta',2),
	('Honda','One',67),
	('Ford','Mondeo',106),
	('Honda','Two',444),
	('Ford','Transit',678)
	]
	c.executemany("INSERT INTO inventory VALUES(?,?,?)",cars)