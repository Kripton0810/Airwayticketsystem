import dbcon

def login(username,password):
    statement  = "SELECT * FROM ADMIN WHERE USERNAME = '"+username+"'"
    dbcn = dbcon.connection()
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
def createAdmin(name,username,password):
    statement = "INSERT INTO `admin`(`name`,`username`,`password`)VALUES('"+name+"','"+username+"','"+password+"');"
    dbcn = dbcon.connection()
    cursor = dbcn.cursor()
    cursor.execute(statement)
    result = cursor.rowcount
    dbcn.commit()
    dbcn.close()
    return  result
    

### TEST
def main():
    # login("Subhankar0810","12345")
    print(createAdmin("Aman Sharma","aman0812","12345"))

if __name__ == '__main__':
    main()
