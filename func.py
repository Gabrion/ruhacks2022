import Int

# Function to add locations to the database
def add(address, city, province, country, postalCode, name, info, language, type):
    Int.database.execute("INSERT INTO Address (id,address,city,province,country,postalCode) values (?,?,?,?,?,?)", \
                         (None, address, city, province, country, postalCode))

    Int.database.execute("INSERT INTO Information (id,name,info,language,type) VALUES (?,?,?,?,?)", (None, name, info, language, type))

# Function to search database for restaurant by name and city
def searchEat(name, city):
    sql = '''SELECT Address.id, Address.address, Address.city, Information.name, Information.info, 
    Information.language FROM Address INNER JOIN Information ON Address.id = Information.id  
    WHERE name LIKE '%{}%' COLLATE NOCASE AND type LIKE 'RES' AND city LIKE '%{}%' COLLATE NOCASE;'''\
        .format(name, city)

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result

# Function to search database for hotel by name and city
def searchStay(name, city):
    sql = '''SELECT Address.id, Address.address, Address.city, Information.name, Information.info, 
    Information.language FROM Address INNER JOIN Information ON Address.id = Information.id  
    WHERE name LIKE '%{}%' COLLATE NOCASE AND type LIKE 'SLE' AND city LIKE '%{}%' COLLATE NOCASE;'''\
        .format(name, city)

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result

# Function to search database for tour guide by city and language
def searchTour(city, language):
    sql = '''SELECT GuideID, name, info, language, city FROM Tour WHERE city 
    LIKE '%{}%' COLLATE NOCASE AND language LIKE '%{}%' COLLATE NOCASE;'''\
        .format(city, language)

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result

# Function to list all entries in Address table
def Loclist():
    sql = '''SELECT Address.id, Address.address, Address.city, Information.name, Information.info, 
    Information.language FROM Address INNER JOIN Information ON Address.id = Information.id;'''

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result

def Tourlist():
    sql = '''SELECT * FROM Tour;'''

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result

# Function to register user
# def register(userId, username, password, securityQuestion, securityAnswer, email):
#    Int.database.execute("INSERT INTO User (userId,username,password,securityQuestion,securityAnswer,email) "
#                         "values (?,?,?,?,?,?)", \
#                         (userId, username, password, securityQuestion, securityAnswer, email))
