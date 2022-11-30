import dbcon
import utlitis
import datetime
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
    pnr = utlitis.makePnr()
    cost = utlitis.calculatePrice(distance,clas)
    statement = """INSERT INTO `ticket`(`pnr`,`name`,`phone`,`email`,`gender`,`age`,`boarding_city`,`arrival_city`,`seat_type`,`distance`,`date_of_journy`,`aadhar`,`passport`,`price`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    tup = (pnr,name,phone,email,gender,age,boarding_city,arrival_city,clas,distance,date,aadhar,passport,cost)
    db = dbcon.connection()
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
    db = dbcon.connection()
    cur = db.cursor()
    statement = "SELECT * FROM TICKET WHERE PNR = '"+pnr+"'"
    cur.execute(statement)
    result = cur.fetchall()
    db.close()
    return result

def cancleAticket(pnr):
    result = findTicket(pnr)
    if result == []:
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
            db = dbcon.connection()
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
    db = dbcon.connection()
    cur = db.cursor()
    cur.execute(statement,email)
    result = cur.fetchall()
    db.close()
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
        if diff<0:
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

            cost =  utlitis.calculatePrice(distance,clas)
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
            db = dbcon.connection()
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

def main():
    # if createTciket() > 0:
    #     print("Data inserted!!!")
    # else:
    #     print("System error")
    # print(cancleAticket("STS203338082533"))
    editTicket("STS203338082533")
    # findTravelHistory("Subhankar0810@gmail.com")

if __name__ == '__main__':
    main()

