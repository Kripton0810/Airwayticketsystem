'''
this file is to run all thr required config in the database
and check all the config
first check all the db is present or not 
then check all the required tables
#required db is airwaytickersystem
'''
import mysql.connector

#make the statement and check the required database
def connectDatabase(host="localhost",username="root",password="Sub@2019",port="3306",database="airwaytickersystem"):
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

startConfig()
        
        