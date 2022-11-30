import mysql.connector
import datetime

rootName = "STS"
port = 3000
username = "root"
host = "localhost"
password = "Sub@2019"
database = "airwaytickersystem"


def connection():
    dbcon = mysql.connector.connect(host=host,username=username,password=password,port=port,database=database)
    return dbcon

def makePnr():
    x = datetime.datetime.now()
    return rootName+x.strftime("%H%M%S%f")
'''
The price of your ticket consists of a number of things.
Base fare
Taxes and airport fees
Fuel surcharge
Service fee to issue
Food
Seat selection
Baggage
'''
def calculatePrice(dis,clas):
    if clas == 1:
        base = 2000
        airline_fule = 700
        cute = 50
        service = 239
        user_dev = 150
        if dis<500:
            base = 2000
        elif dis>=500 and dis<2000:
            base = 4000
        elif dis>=2000 and dis<4000:
            base = 7000
        else:
            base = dis*500
        amount = base + airline_fule + cute + service + user_dev 
        gst_calce = amount * 0.05
        total = gst_calce + 12 +amount
        return total
    elif clas == 2:
        base = 8000
        airline_fule = 2800
        cute = 200
        service = 700
        user_dev = 400
        if dis<500:
            base = 8000
        elif dis>=500 and dis<2000:
            base = 16000
        elif dis>=2000 and dis<4000:
            base = 30000
        else:
            base = dis*1500
        amount = base + airline_fule + cute + service + user_dev 
        gst_calce = amount * 0.12
        total = gst_calce + 100 +amount
        return total
    else:
        return -1
    
'''
11) get no. of passenger
1) Ticket No. auto generated
2) PNRStatus call make PNR
3) get name
4) get phone number
5) get email
6) get gender
7) get boarding city
8) get arrival city
9) get distance
10) calculate price
11) get age
12) 
'''
def createTciket():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    gender = input("Enter your gender (M/F): ")
    age = int(input("Enter your age: "))
    boarding_city = input("Enter your boarding city: ")
    arrival_city = input("Enter your arrival city: ")
    date = input("Enter date of Journey in (YYYY-MM-DD): ")
    distance = float(input("Enter the distance between both the cities: "))
    clas = int(input("Enter you preference class 1)Economy 2)Business: "))
    aadhar = input("Enter your aadhar card number: ")
    passport = input("Enter your passport number: ")
    pnr = makePnr()
    cost = calculatePrice(distance,clas)
    statement = """INSERT INTO `ticket`(`pnr`,`name`,`phone`,`email`,`gender`,`age`,`boarding_city`,`arrival_city`,`seat_type`,`distance`,`date_of_journy`,`aadhar`,`passport`,`price`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    tup = (pnr,name,phone,email,gender,age,boarding_city,arrival_city,clas,distance,date,aadhar,passport,cost)
    db = connection()
    cur = db.cursor()
    cur.execute(statement,tup)
    db.commit()
    ct = cur.rowcount
    print("Your PNR is",pnr)
    print("You have to pay ₹",cost)
    db.close()
    if ct>0:
        return ct
    else:
        return -1

def findTicket(pnr):
    db = connection()
    cur = db.cursor()
    statement = "SELECT * FROM TICKET WHERE PNR = '"+pnr+"'"
    cur.execute(statement)
    result = cur.fetchall()
    db.close()
    return result

def cancleAticket(pnr):
    result = findTicket(pnr)
    if result == []:
        print("No ticket found!!!")
        return 404
    elif result[0][15] == 0:
        print("Ticket is already Canceled !!!")
        return 400
    else:
        print("Ticket Details")
        print(result[0])
        tick_pnr = (result[0][0])
        status = 0
        ch = input("Are you sure you want to cancel you ticket? (Y/N): ")
        if ch == 'Y' or ch == 'y':
            statement = "UPDATE TICKET SET STATUS = "+str(status)+" WHERE PNR = '"+result[0][0]+"'"
            print(statement)
            db = connection()
            cur = db.cursor()
            cur.execute(statement)
            db.commit()
            ct = cur.rowcount
            db.close()
            if ct>0:
                print("Ticket Canceled!!! ")
                return 200
            else:
                print("System Error!!! ")
                return 503
        elif ch == 'N' or ch == 'n':
            print("Transaction Canceled !!!")
            return 499
        else:
            print("Wrong input!! ")
            return 400

def findTravelHistory(email):
    statement = "SELECT * FROM TICKET WHERE EMAIL = %s"
    #get all the information from email and show to the customer
    email = (email,)
    db = connection()
    cur = db.cursor()
    cur.execute(statement,email)
    result = cur.fetchall()
    db.close()
    if result == []:
        print("xxxxxxxxxxxxxx No history found xxxxxxxxxxxxxxxx")
    else:
        print(result)
    return 1

def editTicket(pnr):
    info = findTicket(pnr=pnr)
    if info == []:
        print("No such Ticket found!!! ")
        return 404
    else:        
        info = info[0]
        cst = info[13]
        now = datetime.date.today()
        joindate = info[10]
        diff = now - joindate
        if diff.days < 0:
            ch = input("Your current name is "+info[1]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                name = input("Enter your name: ")
            else:
                name = info[1]
            ch = input("Your current phone number is "+info[2]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                phone = input("Enter your phone number: ")
            else:
                phone = info[2]
            ch = input("Your current email is "+info[3]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                email = input("Enter your email: ")
            else:
                email = info[3]
            ch = input("Your current gender is "+info[4]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                gender = input("Enter your gender (M/F): ")
            else:
                gender = info[4]
            ch = input("Your current age is "+str(info[5])+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                age = int(input("Enter your age: "))
            else:
                age = info[5]
            ch = input("Your current boarding city is "+info[6]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                boarding_city = input("Enter your boarding city: ")
            else:
                boarding_city = info[6]
            ch = input("Your current arrival city is "+info[7]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                arrival_city = input("Enter your arrival city: ")
            else:
                arrival_city = info[7]
            ch = input("Your current Journey in (YYYY-MM-DD) is "+str(info[10])+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                date = input("Enter date of Journey in (YYYY-MM-DD): ")
            else:
                date = info[10]
            ch = input("Your current distance between both the cities is "+str(info[9])+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                distance = float(input("Enter the distance between both the cities: "))
            else:
                distance = info[9]
            if info[8] == 1:
                ch = input("Your current email is Economy. do you want to update? (Y/N): ")
            elif info[8] == 2:
                ch = input("Your current email is Business. do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                clas = int(input("Enter you preference class 1)Economy 2)Business: "))
            else:
                clas = info[8]
            ch = input("Your current aadhar card is "+info[11]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                aadhar = input("Enter your aadhar card number: ")
            else:
                aadhar = info[12]
            ch = input("Your current passport number is "+info[12]+". do you want to update? (Y/N): ")
            if ch == 'Y' or ch == 'y':
                passport = input("Enter your passport number: ")
            else:
                passport = info[13]

            cost =  calculatePrice(distance,clas)
            statement = """UPDATE `airwaytickersystem`.`ticket`
                        SET
                        `name` = %s,
                        `phone` = %s,
                        `email` = %s,
                        `gender` = %s,
                        `age` = %s,
                        `boarding_city` = %s,
                        `arrival_city` = %s,
                        `seat_type` = %s,
                        `distance` = %s,
                        `date_of_journy` = %s,
                        `aadhar` = %s,
                        `passport` = %s,
                        `price` = %s
                        WHERE `pnr` = '"""+pnr+"""'"""
            tup = (name,phone,email,gender,age,boarding_city,arrival_city,clas,distance,date,aadhar,passport,cost)
            db = connection()
            cur = db.cursor()
            cur.execute(statement,tup)
            db.commit()
            db.close()
            print("The information",pnr,"has been updated !!! ")
            if cst != cost:
                print("Your new cost is ",cost," the price difference is ",(cst-cost))
        else:
            print("Ticket Expire")
        return 200

def login(username,password):
    statement  = "SELECT * FROM ADMIN WHERE USERNAME = '"+username+"'"
    dbcn = connection()
    cursor = dbcn.cursor()
    cursor.execute(statement)
    result = cursor.fetchone()
    dbcn.close()
    if result == None:
        return 404
    else:
        if password == result[3]:
            return 200
        else:
            return 403
        
def createAdminForDB(name,username,password):
    statement = "INSERT INTO `admin`(`name`,`username`,`password`)VALUES('"+name+"','"+username+"','"+password+"');"
    dbcn = connection()
    cursor = dbcn.cursor()
    cursor.execute(statement)
    result = cursor.rowcount
    dbcn.commit()
    dbcn.close()
    return  result

def authenticate():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    code  = login(username,password)
    if code == 404:
        print("User is not valid Create one!! ")
    elif code == 403:
        print("Password is invalid!!! ")
    elif code == 200:
        welcome()
        menu()
    else:
        print("System Error!!! ")
    
def createAdmin():
    name = input("Enter the name of admin: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    result = createAdminForDB(name,username,password)
    if result > 0:
        print("User Created Successfully")
    else:
        print("User not created")


#make the statement and check the required database
def connectDatabase(host=host,username=username,password=password,port=port,database=database):
    if database != "":
        dbcon = mysql.connector.connect(host=host,username=username,password=password,port=port,database=database)
        return dbcon
    else:
        dbcon = mysql.connector.connect(host=host,username=username,password=password,port=port)
        return dbcon

def startConfig():
    dbcon = connectDatabase(port = 3000, database = "")
    statement = "Show databases"
    cursor = dbcon.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    flag = 0
    for i in result:
        if i == ('airwaytickersystem',):
            flag = 1
            break
    dbcon.close()
    if flag == 0:
        dbcon = connectDatabase(port = 3000, database = "")
        statement = "create database airwaytickersystem"
        print("creating database ...")
        cursor = dbcon.cursor()
        cursor.execute(statement)
        dbcon.commit()
        dbcon.close()
    if flag == 1:
        print("Database already created")
    checkTables()
    makeAdmin()


def checkTables():
    tables = [("admin",),("ticket",),("temp",)]
    table_info = {
        "admin":"""CREATE TABLE `admin` (
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(45) DEFAULT NULL,
        `username` varchar(45) DEFAULT NULL,
        `password` varchar(45) DEFAULT NULL,
        `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`),
        UNIQUE KEY `username_UNIQUE` (`username`)
        )
                """,
        "ticket":"""
        CREATE TABLE `ticket` (
            `pnr` varchar(100) NOT NULL,
            `name` varchar(100) DEFAULT NULL,
            `phone` varchar(12) DEFAULT NULL,
            `email` varchar(100) DEFAULT NULL,
            `gender` varchar(10) DEFAULT NULL,
            `age` int DEFAULT NULL,
            `boarding_city` varchar(45) DEFAULT NULL,
            `arrival_city` varchar(45) DEFAULT NULL,
            `seat_type` int DEFAULT NULL,
            `distance` float DEFAULT NULL,
            `date_of_journy` date DEFAULT NULL,
            `aadhar` varchar(45) DEFAULT NULL,
            `passport` varchar(45) DEFAULT NULL,
            `price` float DEFAULT NULL,
            `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
            `status` int DEFAULT '1',
            PRIMARY KEY (`pnr`)
            )
        """,
        "temp":"""
        CREATE TABLE `temp` (
        `pnr` varchar(100) NOT NULL,
        `name` varchar(100) DEFAULT NULL,
        `phone` varchar(12) DEFAULT NULL,
        `email` varchar(100) DEFAULT NULL,
        `gender` varchar(10) DEFAULT NULL,
        `age` int DEFAULT NULL,
        `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
        `status` int DEFAULT '1',
        PRIMARY KEY (`pnr`)
        );
        """

    }
    dbcon = connectDatabase(port = 3000, database = "airwaytickersystem")
    statement = "show tables"
    cursor = dbcon.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    for i in tables:
        if i not in result:
            print("Creating table",i[0],"... ")
            create_table_statement = table_info[i[0]]
            cursor.execute(create_table_statement)
            print("table",i[0]," created ... ")
            dbcon.commit()
        else:
            print("table",i[0],"already created ... ")
        
    dbcon.close()

def makeAdmin():
    statement = "SELECT * FROM ADMIN WHERE username = 'admin'"
    dbcon = connectDatabase(port = 3000, database = "airwaytickersystem")
    cursor = dbcon.cursor()
    cursor.execute(statement)
    cursor.fetchall()
    count = cursor.rowcount
    dbcon.close()
    if count>0:
        print('admin user present')
        return 1
    else:
        dbcon = connectDatabase(port = 3000, database = "airwaytickersystem")
        statement = """INSERT INTO `admin`
                        (`name`,
                        `username`,
                        `password`)
                        VALUES
                        ("admin","admin","admin123")"""
        cursor = dbcon.cursor()
        cursor.execute(statement)
        count = cursor.rowcount
        dbcon.commit()
        dbcon.close()
        print('creating admin user...')

        if count>0:
            print('admin created')
            return 1
        else:
            print('system error')
            return 0

def welcome():
    print("+-----------------------------------------------------------------+")
    print("|  *******************      WELCOME      *******************      |")
    print("|         PROJECT CREATED BY: SIMRAN, TULIKA, SHRUTI              |")
    print("+-----------------------------------------------------------------+")

def menu():
    print("===================== Enter Your Choice ===========================")
    print("1) Create Admin") #done
    print("2) Book a ticket")  #done
    print("3) Cancel a ticket") #done
    print("4) Find ticket history")
    print("5) Find ticket") #done
    print("6) Edit Booking") #done
    print("7) Logout")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        createAdmin()
        menu()
    elif ch== 2:
        createTciket()
        menu()
    elif ch == 3:
        pnr = input("Enter your PNR number: ")
        cancleAticket(pnr)
        menu()
    elif ch == 4:
        email = input("Enter your email: ")
        findTravelHistory(email=email)
        menu()
    elif ch == 5:
        pnr = input("Enter your PNR number: ")
        result = findTicket(pnr=pnr)
        if result == []:
            print("No ticket found!!!")
        else:
            print(result)
        menu()
    elif ch == 6:
        pnr = input("Enter your PNR number: ")
        editTicket(pnr=pnr)
        menu()
    elif ch == 7:
        print("+-----------------------------------------------------------------+")
        print("|  *******************      Thank You    *******************      |")
        print("+-----------------------------------------------------------------+")
    
    
    else:
        print("Wrong Input")
        menu()

def main():
    authenticate()

if __name__ == '__main__':
    startConfig()
    main()