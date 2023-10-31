#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

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
    obalance tinytext,
    date tinytext);
'''
cursor.execute(query)
cursor.execute('PRAGMA table_info(pets);')

result = cursor.fetchall()
print(result)
for i in result:
    print(i)

data = [
    [1789,'Bella','Dog','Maltese','Joe Mantenga', '778457120', '700','2022-01-28'],
    [985,'Lucy','Dog','Bichon','Hanna Montana', '7784857629', '950','2020-11-13'],
    [2157,'Chloe','Cat','persian','Amanda Huggenkis', '7784475012', '630','2023-03-21'],
    [2845,'Max','Dog','poodle','Michael Jackson', '7789851068', '810','2023-10-28'],
    [1318,'Coco','Bird','parrot','Peter Nesmith', '7785736489', '370','2021-05-03']
    ]

for i in data:
    query = f"insert into pets (id,pname,pspecies,pbreed,oname,ophone,obalance,date) values ({i[0]},'{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}');"
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from pets"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)



"""create table if not exists pets (
    id integer primary key autoincrement,
    pname tinytext,
    pspecies tinytext,
    pbreed tinytext,
    oname tinytext,
    ophone int,
    obalance integer,
    date Char(10));"""