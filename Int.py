import sqlite3

database = sqlite3.connect('locations.db')
cursor = database.cursor()


def int():
    database.execute('''CREATE TABLE Address (id int, address text, city text, province text, 
    country text, postalCode text)''')

    database.execute('''CREATE TABLE Information (id int, name text, info text, language text)''')

    database.execute('''CREATE TABLE User (userId int, username text, password text, securityQuestion text, 
    securityAnswer, email text)''')

    database.execute("INSERT INTO Address VALUES ('1','123 lane','Toronto','Ontario','Canada','1a1a1a')")
    database.execute("INSERT INTO Information VALUES ('1','ElCubano','Cuban Bar','Spanish')")

    database.execute("INSERT INTO Address VALUES ('2','456 lane','Toronto','Ontario','Canada','2a2a2a')")
    database.execute("INSERT INTO Information VALUES ('2','Cafeee','Serbian Cafe','Serbian')")

    database.execute("INSERT INTO Address VALUES ('3','789 lane','Toronto','Ontario','Canada','3a3a3a')")
    database.execute("INSERT INTO Information VALUES ('3','McDonalds','McDonalds','English')")
