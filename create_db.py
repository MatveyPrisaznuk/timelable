import sqlite3 as sql


con = sql.connect('db_web.db')


cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS school")

sql ='''CREATE TABLE "school" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"DATA"	TEXT,
	"SUBJECT"	TEXT
)'''
cur.execute(sql)


con.commit()


con.close()