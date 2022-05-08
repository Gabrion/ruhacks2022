import sqlite3

# initialize variables
# database = sqlite3.connect('locations.db')
database = sqlite3.connect(':memory:')
cursor = database.cursor()

# Initialize database tables
def int():
    database.execute('''CREATE TABLE Address (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , address text, city text, province text, 
    country text, postalCode text)''')

    database.execute(
        '''CREATE TABLE Information (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , name text, info text, language text, type text)''')

    database.execute(
        '''CREATE TABLE Tour (GuideId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , name text, info text, language text, city text)''')

    database.execute('''CREATE TABLE User (userId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username text, password text, securityQuestion text, 
    securityAnswer text, email text)''')


# populate database tables
def populate():
# Insert Restaurants
    database.execute("INSERT INTO Address VALUES (?,?,?,?,?,?)",
                     (None, '123 lane', 'Toronto', 'Ontario', 'Canada', '1a1a1a'))
    database.execute("INSERT INTO Information VALUES (?,?,?,?,?)", (None, 'ElCubano', 'Cuban Bar', 'Spanish', 'RES'))

    database.execute("INSERT INTO Address VALUES (?,?,?,?,?,?)",
                     (None, '456 road', 'Toronto', 'Ontario', 'Canada', '2a2a2a'))
    database.execute("INSERT INTO Information VALUES (?,?,?,?,?)", (None, 'cafeee', 'Serbian cafe', 'Serbian', 'RES'))

# Insert Hotels
    database.execute("INSERT INTO Address VALUES (?,?,?,?,?,?)",
                     (None, '789 Court', 'Calgary', 'Alberta', 'Canada', '3a3a3a'))
    database.execute("INSERT INTO Information VALUES (?,?,?,?,?)", (None, 'HomeStar', 'Hotel', 'english', 'SLE'))

# Insert Tour guides
    database.execute("INSERT INTO Tour VALUES (?,?,?,?,?)",
                     (None, 'Dwayne Johnson', 'Is a rock', 'English', 'Toronto'))