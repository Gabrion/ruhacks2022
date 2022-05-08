import Int


def add(id, address, city, province, country, postalCode, name, info, language):
    Int.database.execute("INSERT INTO Address (id,address,city,province,country,postalCode) values (?,?,?,?,?,?)", \
                         (id, address, city, province, country, postalCode))

    Int.database.execute("INSERT INTO Information (id,name,info,language) VALUES (?,?,?,?)", (id,name, info, language))

def search(name):
    sql = '''SELECT Address.id, Address.address, Address.city, Information.name, Information.info, 
    Information.language FROM Address INNER JOIN Information ON Address.id = Information.id  
    WHERE Information.name LIKE '%{}%' COLLATE NOCASE;'''.format(name)

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result

def list():
    sql = '''SELECT Address.id, Address.address, Address.city, Information.name, Information.info, 
    Information.language FROM Address INNER JOIN Information ON Address.id = Information.id;'''

    Int.cursor.execute(sql)
    result = Int.cursor.fetchall()
    return result
    #for row in result:
    #    print(row)

