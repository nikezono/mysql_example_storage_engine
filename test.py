import mysql.connector

if __name__ == '__main__':
    db = mysql.connector.connect(
        host="localhost", user="root", password="root")
    cursor = db.cursor()

    cursor.execute('SET sql_log_bin = 0;')
    cursor.execute('DROP DATABASE IF EXISTS st_test')
    cursor.execute('CREATE DATABASE st_test')
    cursor.execute('CREATE TABLE st_test.items (\
        title VARCHAR(50) NOT NULL,\
        content TEXT\
    ) ENGINE = ci_example')
    db.commit()

    cursor.execute(
        'INSERT INTO st_test.items (\
            title, content\
        ) VALUES ("alice", "alice meets bob")'
    )
    db.commit()
