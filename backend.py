import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        if title == "":
            mtitle = title
        else:
            mtitle = '%' + title + '%'
        if author == "":
            mauthor = author
        else:
            mauthor =  '%' + author + '%'
        if year == "":
            myear = year
        else:
            myear =  '%' + year + '%'
        if title == "":
            mtitle = title
        else:
            mtitle = '%' + title + '%'
        if isbn == "":
            misbn = isbn
        else:
            misbn =  '%' + isbn + '%'
        self.cur.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ? OR year LIKE ? OR isbn LIKE ?", (mtitle, mauthor, myear, misbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()