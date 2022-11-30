import mysql.connector

def connection():
    dbcon = mysql.connector.connect(host="localhost",username="root",password="Sub@2019",port="3000",database="airwaytickersystem")
    return dbcon

def main():
    db = connection()
    print(db)
    db.close()

if __name__ == '__main__':
    main()