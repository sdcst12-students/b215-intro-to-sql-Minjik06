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

def data():
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
    connection.commit()

    print("_____Information stored__________________________________________________________________________________")
    query = "select * from pets"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)
    print("_________________________________________________________________________________________________________")
    print()

    connection.close()



def addInfo(a,b,c,d,e,f,g,h):
    connection=sqlite3.connect('dbase1.db')
    cursor=connection.cursor()

    cursor.execute("insert into pets (pname,pspecies,pbreed,oname,ophone,email,obalance,date) values (?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h))

    connection.commit()
    connection.close()

def Id(id):
    connection=sqlite3.connect('dbase1.db')
    cursor=connection.cursor()

    cursor.execute('select * from pets where id=?',(id,))
    result=cursor.fetchall()

    if result:
        for i in result:
            print(f"\ninformation : {result}")
            print(f"***** ID: {i[0]}, Name: {i[1]} *****\n")
    else:
        print("records are not found / please add information")
        a=str(input("Enter the pet's name: "))
        b=str(input("Enter the pet's species: "))
        c=str(input("Enter the pet's breed: "))
        d=str(input("Enter the owner's name: "))
        e=str(input("Enter the owner's phone number: "))
        f=str(input("Enter the owner's email: "))
        g=str(input("Enter the owner's balance: "))
        h=str(input("Enter the date of first visit: "))
        addInfo(a,b,c,d,e,f,g,h)
        print()
        print("__________________________________your information is successfully added__________________________________")
        Phone(e)
        print()
        data()

    connection.close()

def Email(email):
    connection=sqlite3.connect('dbase1.db')
    cursor=connection.cursor()

    cursor.execute('select * from pets where email=?',(email,))
    result=cursor.fetchall()

    if result:
        for i in result:
            print(f"\ninformation : {result}")
            print(f"***** ID: {i[0]}, Name: {i[1]} *****\n")
    else:
        print("records are not found / please add information")
        a=str(input("Enter the pet's name: "))
        b=str(input("Enter the pet's species: "))
        c=str(input("Enter the pet's breed: "))
        d=str(input("Enter the owner's name: "))
        e=str(input("Enter the owner's phone number: "))
        f=str(input("Enter the owner's email: "))
        g=str(input("Enter the owner's balance: "))
        h=str(input("Enter the date of first visit: "))
        addInfo(a,b,c,d,e,f,g,h)
        print()
        print("__________________________________your information is successfully added__________________________________")
        Email(f)
        print()
        data()
    connection.close()

def Phone(phone):
    connection=sqlite3.connect('dbase1.db')
    cursor=connection.cursor()

    cursor.execute('select * from pets where ophone=?',(phone,))
    result=cursor.fetchall()

    if result:
        for i in result:
            print(f"\ninformation : {result}")
            print(f"***** ID: {i[0]}, Name: {i[1]} *****\n")
    else:
        print("records are not found / please add information")
        a=str(input("Enter the pet's name: "))
        b=str(input("Enter the pet's species: "))
        c=str(input("Enter the pet's breed: "))
        d=str(input("Enter the owner's name: "))
        e=str(input("Enter the owner's phone number: "))
        f=str(input("Enter the owner's email: "))
        g=str(input("Enter the owner's balance: "))
        h=str(input("Enter the date of first visit: "))
        addInfo(a,b,c,d,e,f,g,h)
        print()
        print("__________________________________your information is successfully added__________________________________")
        Phone(e)
        print()
        data()
    connection.close()

def Newinfo():
    connection=sqlite3.connect('dbase1.db')
    print()
    a=str(input("Enter the pet's name: "))
    b=str(input("Enter the pet's species: "))
    c=str(input("Enter the pet's breed: "))
    d=str(input("Enter the owner's name: "))
    e=str(input("Enter the owner's phone number: "))
    f=str(input("Enter the owner's email: "))
    g=str(input("Enter the owner's balance: "))
    h=str(input("Enter the date of first visit: "))
    addInfo(a,b,c,d,e,f,g,h)
    print()
    print("__________________________________your information is successfully added__________________________________")
    Phone(e)
    print()
    data()
    connection.close()

def call():
    data()
    a=int(input("Find information with \n1.ID\n2.Phone\n3.Email\n4.Add info\n:"))
    if a==1:
        print()
        b=int(input("Enter the ID: "))
        Id(b)
    elif a==2:
        print()
        b=str(input("Enter the Phone number: "))
        Phone(b)
    elif a==3:
        print()
        b=str(input("Enter the Email: "))
        Email(b)
    else:
        Newinfo()



call()





















"""


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

print()

def addInfo():
    print()
    file='dbase1.db'
    connection = sqlite3.connect(file)
    cursor=connection.cursor()
    a=str(input("Enter the pet's name: "))
    b=str(input("Enter the pet's species: "))
    c=str(input("Enter the pet's breed: "))
    d=str(input("Enter the owner's name: "))
    e=str(input("Enter the owner's phone number: "))
    f=str(input("Enter the owner's email: "))
    g=str(input("Enter the owner's balance: "))
    h=str(input("Enter the date of first visit: "))
    query = f"insert into pets (pname,pspecies,pbreed,oname,ophone,email,obalance,date) values ('{a}','{b}','{c}','{d}','{e}','{f}','{g}','{h}');"
    cursor.execute(query)
    connection.commit()
    query = "select * from pets"
    cursor.execute(query)
    cursor.execute('select * from pets where ophone=:ophone',{"ophone":e})
    result = cursor.fetchall()
    for i in result:
        print(f"Tuple:{i}")
        print(f"Name:{i[1]}")

b=int(input("retrieve a record\n1.id?\n2.phone number?\n3.email?\n4.add information\n: #"))
print()
if b==1:
    a=int(input("Enter ID : "))
    cursor.execute('select * from pets where id=:id',{"id":a})
    result = cursor.fetchall()
    if result:
        for i in result:
            print(f"Tuple:{i}")
            print(f"Name:{i[1]}")
    else:
        print("records are not found")
        addInfo()
elif b==2:
    a=str(input("Enter phone number? : "))
    cursor.execute('select * from pets where ophone=:ophone',{"ophone":a})
    result = cursor.fetchall()
    if result:
        for i in result:
            print(f"Tuple:{i}")
            print(f"Name:{i[1]}")
    else:
        print("records are not found")
        addInfo()
elif b==3:
    a=str(input("Enter email? : "))
    cursor.execute('select * from pets where email=:email',{"email":a})
    result = cursor.fetchall()
    if result:
        for i in result:
            print(f"Tuple:{i}")
            print(f"Name:{i[1]}")
    else:
        print("records are not found")
        addInfo()
else:
    addInfo()


"""

"""
need a function that will ask users for their details, and then write the details to the database
query = f"insert into pets (pname,pspecies,pbreed,oname,ophone,email,obalance,date) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}');"
"""