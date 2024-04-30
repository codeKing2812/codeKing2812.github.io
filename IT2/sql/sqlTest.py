import sqlite3



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


create_connection('/Users/linus/Desktop/Skole/Programmering/codeKing2812.github.io/IT2/sql/chinook.db')
