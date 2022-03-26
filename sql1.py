import sqlite3
connect = sqlite3.connect('school.db') 
cur = connect.cursor()
query1 = "CREATE TABLE IF NOT EXISTS classes (id INT, class INT, num_of_stud INT, teacher CHAR, age INT)"
query2 = "CREATE TABLE IF NOT EXISTS students (id INT, familia CHAR, imya CHAR, otchestvo CHAR, class INT)"
#query3 = "CREATE TABLE IF NOT EXISTS  (Id INT, class INT, num_of_stud INT, teacher INT,)"
cur. execute(query1)
cur.execute("INSERT INTO book VALUES(1, 9, 21, 'Smirnov', 43)")
cur.execute("INSERT INTO book VALUES(2, 9, 22, 'Petrova', 29)")
cur.execute("INSERT INTO book VALUES(3, 10, 19, 'Popov', 37)")
cur.execute("INSERT INTO book VALUES(4, 8, 24, 'Tarasova', 31)")
cur.execute("INSERT INTO book VALUES(5, 1, 27, 'Zuev', 44)")

cur. execute(query2)
cur.execute("INSERT INTO book VALUES(18, 'Kotov', 'Andrew', 'Alexandrovich', 9)")
cur.execute("INSERT INTO book VALUES(29, 'Sobolev', 'Petya', 'Viktorovich', 9)")
cur.execute("INSERT INTO book VALUES(98, 'Frolov', 'Anotoliy', 'Vyachaslavovich', 10)")
cur.execute("INSERT INTO book VALUES(33, 'Volkova', 'Liza', 'Vasilevna', 8)")
cur.execute("INSERT INTO book VALUES(66, 'Ushinskiy', 'Denis', 'Vladimirovich', 1)")


#cur. execute(query)
#cur.execute("INSERT INTO book VALUES('PUSHKIN', 1789)")
#cur.execute('UPDATE book SET year =1895')
#book1 = ("Esenin", 1890)
#cur.execute("INSERT INTO book VALUES(?, ?)", book1)
#cur.execute(UPDATE book SET year = 1895 WHERE author = "Esenin")
#cur.execute("SELECT * FROM book")
#rows = cur.fetchall()
#print(rows)
#for row in rows:
#    print(row)
#connect.commit()
#connect.close()
