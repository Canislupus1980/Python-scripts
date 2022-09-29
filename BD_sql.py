import pypyodbc

mySQLServer = "\\fs01\Отделы\Управление ИТ и РП\ОРСИРП\Группа эксплуатации сетевой инфраструктуры офиса\ITInvent.mdb"
myDatabase  = "COMPANY"
connection  = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';'
                              'uid=username;'
                              'pwd=pypassword;')

cursor = connection.cursor()

mySQLQuery = ("""
                SELECT CompanyName, ContactName, country
                FROM dbo.Customers
                WHERE country = 'Belarus'
                """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    companyname = row[0]
    contactname = row[1]
    contryname  = row[2]

    print("Welcome :" + str(companyname) + " User: " + str(contactname) + " From: " + str(contryname))

connection.close()
