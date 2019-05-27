
import mysql.connector as mariadb

mariadb_connection=mariadb.connect(
   host="localhost",
   user="root",
   database="test"
)

cursor = mariadb_connection.cursor()

#INSERT INTO `test`.`books` (`author`, `section`, `title`, `date`) VALUES ('Jk rowling', 'fantasy', 'Harry Potter', '1997-04-22');
print(cursor.execute("SELECT * FROM books"))


def saver(title, author, date, section):
    sql = "INSERT INTO books (title, author, date, section) VALUES (%s, %s, %s, %s)"
    val = (title, author, date, section)
    cursor.execute(sql, val)
    print(sql)
    mariadb.commit()


    return True

