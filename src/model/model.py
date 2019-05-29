import mysql.connector as mariadb

mariadb_connection=mariadb.connect(
   host="localhost",
   user="root",
   database="test"
)

cursor = mariadb_connection.cursor(buffered=True)

#INSERT INTO `test`.`books` (`author`, `section`, `title`, `date`) VALUES ('Jk rowling', 'fantasy', 'Harry Potter', '1997-04-22');


def saver(title, author, date, section, status, summary):
    sql = "INSERT INTO books (title, author, date, section, status, summary) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (title, author, date, section, status, summary)
    try:
        cursor.execute(sql, val)
    except mariadb.Error as error:
        print("Error: {}".format(error))
    print(sql)
    mariadb_connection.commit()
    return True


