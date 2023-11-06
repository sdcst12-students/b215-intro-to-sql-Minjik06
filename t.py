import sqlite3

file='dbase1.db'
connection = sqlite3.connect(file)
print(connection)

cursor=connection.cursor()
query='''
create table if not exists pets (
    id integer primary key autoincrement,
    pname tinytext,
    pspecies tinytext,
    pbreed tinytext,
    oname tinytext,
    ophone tinytext,
    email tinytext,
    obalance tinytext,
    date tinytext);
'''


cursor.execute(query)
cursor.execute('PRAGMA table_info(pets);')

result = cursor.fetchall()
print(result)
for i in result:
    print(i)

cursor.execute('delete from pets') 
data = [
    ['Bella','Dog','Maltese','Joe Mantenga', '778457120','joe@sdss.ca', '700','2020-01-28'],
    ['Lucy','Dog','Bichon','Hanna Montana', '7784857629', 'miley@cyrus.com','950','2021-11-13'],
    ['Chloe','Cat','persian','Amanda Huggenkis', '7784475012', 'cool1@gmail.com','630','2022-03-21'],
    ['Max','Dog','poodle','Michael Jackson', '7789851068', 'singer@thriller.com','810','2023-05-03'],
    ['Coco','Bird','parrot','Peter Nesmith', '7785736489', 'bassist@monkees.org','370','2023-10-28']
    ]

for i in data:
    query = f"insert into pets (pname,pspecies,pbreed,oname,ophone,email,obalance,date) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}');"
    print(query)
    cursor.execute(query)

connection.commit()

query = "select * from pets"
cursor.execute(query)

result = cursor.fetchall()
print(result)
for i in result:
    print(i)