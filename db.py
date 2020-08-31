import sqlite3


def store(info: list):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    #c.execute("CREATE TABLE books(name, stock, price);")
    insert: str = "INSERT INTO books(name, stock, price) VALUES(?, ?, ?);"
    c.executemany(insert, info)
    connection.commit()
    connection.close()
