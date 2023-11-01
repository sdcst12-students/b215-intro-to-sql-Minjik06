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
    id integer,
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
    [10,'Bella','Dog','Maltese','Joe Mantenga', '778457120','joe@sdss.ca', '700','2020-01-28'],
    [20,'Lucy','Dog','Bichon','Hanna Montana', '7784857629', 'miley@cyrus.com','950','2021-11-13'],
    [30,'Chloe','Cat','persian','Amanda Huggenkis', '7784475012', 'cool1@gmail.com','630','2022-03-21'],
    [40,'Max','Dog','poodle','Michael Jackson', '7789851068', 'singer@thriller.com','810','2023-05-03'],
    [45,'Coco','Bird','parrot','Peter Nesmith', '7785736489', 'bassist@monkees.org','370','2023-10-28']
    ]

for i in data:
    query = f"insert into pets (id,pname,pspecies,pbreed,oname,ophone,email,obalance,date) values ({i[0]},'{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}');"
    print(query)
    cursor.execute(query)

connection.commit()

query = "select * from pets"
cursor.execute(query)

result = cursor.fetchall()
print(result)
for i in result:
    print(i)

print()

b=int(input("retrieve a record\n1.id?\n2.phone number?\n3.email?\n:"))
print()
if b==1:
    a=int(input("Enter ID : "))
    cursor.execute('select * from pets where id=:id',{"id":a})
    result = cursor.fetchall()
    if result:
        for i in result:
            print(i)
    else:
        print("records are not found")
elif b==2:
    a=str(input("Enter phone number? : "))
    cursor.execute('select * from pets where ophone=:ophone',{"ophone":a})
    result = cursor.fetchall()
    print(result)
    for i in result:
        print(i)
elif b==3:
    a=str(input("Enter email? : "))
    cursor.execute('select * from pets where email=:email',{"email":a})
    result = cursor.fetchall()
    print(result)
    for i in result:
        print(i)


