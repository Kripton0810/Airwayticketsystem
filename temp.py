import pickle
import os
def create():
    rec=[]
    with open("xyz.dat", "wb") as fp:
        admno=int(input("Admission Form No"))
        issdt=input("Date of Issue")
        regno=int(input("Registration Number"))
        regdt=input("Registration Date")
        cname=input("Name of the Candidate")
        add=input("Residential Address")
        city=input("City Name")
        dist=input("District Name")
        state=input("State Name")
        pin=int(input("Pincode"))
        mob=input("Mobile Number")
        fname=input("Father Name")
        focc=input("Father Occupation")
        mname=input("Mother Name")
        mocc=input("Mother Occupation")
        dob=input("Date of Birth")
        adhar=input("Aadhar Card No")
        pob=input("Place of Birth")
        gen=input("Gender")
        mton=input("Mother Tongue")
        reg=input("Religion")
        cas=input("Caste")
        dis=input("Physical problem/Disability")
        blg=input("Blood Group")
        idmrk=input("Identification Mark")
        lstscatt=input("Name of the School Last Attended")
        adtak=input("Standard to which admission is sought")
        medinf=input("Any Medical Information")
        rec=[admno,issdt,regno,regdt,cname,add,city,dist,state,pin,mob,fname,focc,mname,mocc,dob,adhar,pob,gen,mton,reg,cas,dis,blg,idmrk,lstscatt,adtak,medinf]        
        pickle.dump(rec,fp)
        fp.close()
        menu()

def append():
    rec=[]
    with open("xyz.dat", "ab") as fp:
        admno=int(input("Admission Form No"))
        issdt=input("Date of Issue")
        regno=int(input("Registration Number"))
        regdt=input("Registration Date")
        cname=input("Name of the Candidate")
        add=input("Residential Address")
        city=input("City Name")
        dist=input("District Name")
        state=input("State Name")
        pin=int(input("Pincode"))
        mob=input("Mobile Number")
        fname=input("Father Name")
        focc=input("Father Occupation")
        mname=input("Mother Name")
        mocc=input("Mother Occupation")
        dob=input("Date of Birth")
        adhar=input("Aadhar Card No")
        pob=input("Place of Birth")
        gen=input("Gender")
        mton=input("Mother Tongue")
        reg=input("Religion")
        cas=input("Caste")
        dis=input("Physical problem/Disability")
        blg=input("Blood Group")
        idmrk=input("Identification Mark")
        lstscatt=input("Name of the School Last Attended")
        adtak=input("Standard to which admission is sought")
        medinf=input("Any Medical Information")
        rec=[admno,issdt,regno,regdt,cname,add,city,dist,state,pin,mob,fname,focc,mname,mocc,dob,adhar,pob,gen,mton,reg,cas,dis,blg,idmrk,lstscatt,adtak,medinf]        
        pickle.dump(rec,fp)
        fp.close()
        menu()

def dispall():
    rec=[]
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                print("Admission Form No   : ",rec[0])
                print("Date of Issue       : ",rec[1])
                print("Registration Number : ",rec[2])
                print("Registration Date   : ",rec[3])
                print("Name of the Candidate:",rec[4])
                print("Address             : ",rec[5])
                print("City                : ",rec[6])
                print("District            : ",rec[7])
                print("State               : ",rec[8])
                print("Pincode             : ",rec[9])
                print("Mobile Number       : ",rec[10])
                print("Father Name         : ",rec[11])
                print("Father Occupation   : ",rec[12])
                print("Mother Name         : ",rec[13])
                print("Mother Occupation   : ",rec[14])
                print("Date of Birth       : ",rec[15])
                print("Aadhar Card No      : ",rec[16])
                print("Place of Birth      : ",rec[17])
                print("Gender              : ",rec[18])
                print("Mother Tongue       : ",rec[19])
                print("Religion            : ",rec[20])
                print("Caste               : ",rec[21])
                print("Physical problem/Disability : ",rec[22])
                print("Blood Group         : ",rec[23])
                print("Identification Mark : ",rec[24])
                print("School Last Attended : ",rec[25])
                print("Standard Admission Taken : ",rec[26])
                print("Medical Information : ",rec[27])
                print("--------------------------------------------------------------------")
        except EOFError:
            fp.close()
        menu()

def searchadm():
    rec=[]
    scadm=int(input("Enter the Admission Number to be searched"))
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if scadm==rec[0]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
        except EOFError:
            fp.close()
        menu()

def searchreg():
    rec=[]
    screg=int(input("Enter the Registration Number to be searched"))
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if screg==rec[2]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
        except EOFError:
            fp.close()
        menu()

def searchregdate():
    rec=[]
    scregdt=input("Enter the Registration Date to be searched")
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if scregdt==rec[3]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
                    print("--------------------------------------------------------------------")
        except EOFError:
            fp.close()
        menu()

def searchname():
    rec=[]
    scname=input("Enter the Name to be searched")
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if scname==rec[4]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
        except EOFError:
            fp.close()
        menu()

def searchgen():
    rec=[]
    scgen=input("Enter the Gender to be searched")
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if scgen==rec[18]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
                    print("--------------------------------------------------------------------")
        except EOFError:
            fp.close()
        menu()

def searchcaste():
    rec=[]
    sccas=input("Enter the Caste to be searched")
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if sccas==rec[21]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
                    print("--------------------------------------------------------------------")
        except EOFError:
            fp.close()
        menu()
        
def searchaadhar():
    rec=[]
    scaad=input("Enter the Aadhar Card to be searched")
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if scaad==rec[16]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
        except EOFError:
            fp.close()
        menu()
        
def searchclass():
    rec=[]
    sccla=input("Enter the Class to be searched")
    with open("xyz.dat", "rb") as fp:
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if sccla==rec[26]:
                    print("Admission Form No   : ",rec[0])
                    print("Date of Issue       : ",rec[1])
                    print("Registration Number : ",rec[2])
                    print("Registration Date   : ",rec[3])
                    print("Name of the Candidate:",rec[4])
                    print("Address             : ",rec[5])
                    print("City                : ",rec[6])
                    print("District            : ",rec[7])
                    print("State               : ",rec[8])
                    print("Pincode             : ",rec[9])
                    print("Mobile Number       : ",rec[10])
                    print("Father Name         : ",rec[11])
                    print("Father Occupation   : ",rec[12])
                    print("Mother Name         : ",rec[13])
                    print("Mother Occupation   : ",rec[14])
                    print("Date of Birth       : ",rec[15])
                    print("Aadhar Card No      : ",rec[16])
                    print("Place of Birth      : ",rec[17])
                    print("Gender              : ",rec[18])
                    print("Mother Tongue       : ",rec[19])
                    print("Religion            : ",rec[20])
                    print("Caste               : ",rec[21])
                    print("Physical problem/Disability : ",rec[22])
                    print("Blood Group         : ",rec[23])
                    print("Identification Mark : ",rec[24])
                    print("School Last Attended : ",rec[25])
                    print("Standard Admission Taken : ",rec[26])
                    print("Medical Information : ",rec[27])
        except EOFError:
            fp.close()
        menu()
        
def modifyreg():
    rec=[]
    screg=int(input("Enter the Registration Number to be modified"))
    with open("xyz.dat", "rb") as fp:
        fs=open("temp.dat","wb")
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if screg==rec[2]:
                    ch1=input("Do you want to change address [Y/N]")
                    if ch1=="Y" or ch1=="Yes":
                        print("Old Name of the Candidate:",rec[4])
                        rec[4]=input("New Name of the Candidate:")
                        print("Old Address         : ",rec[5])
                        rec[5]=input("New Address  :")
                        print("Old City            : ",rec[6])
                        rec[6]=input("New City     :")
                        print("Old District        : ",rec[7])
                        rec[7]=input("New District :")
                        print("Old State               : ",rec[8])
                        rec[8]=input("New State    :")
                        print("Old Pincode             : ",rec[9])
                        rec[9]=input("New Pincode  :")
                    ch2=input("Do you want to change Mobile Number [Y/N]")
                    if ch2=="Y" or ch2=="Yes":    
                        print("Old Mobile Number       : ",rec[10])
                        rec[10]=input("New Mobile Number  :")
                    ch3=input("Do you want to change Caste [Y/N]")
                    if ch3=="Y" or ch3=="Yes": 
                        print("Old Caste               : ",rec[21])
                        rec[21]=input("New Caste   :")
                    ch4=input("Do you want to change Physical Problem [Y/N]")
                    if ch4=="Y" or ch4=="Yes": 
                        print("Old Physical problem/Disability : ",rec[22])
                        rec[22]=input("New Physical problem/Disability :")
                        print("Old Medical Information : ",rec[27])
                        rec[27]=input("New Medical Information  :")
                    pickle.dump(rec,fs)                    
        except EOFError:
            fp.close()
            fs.close() 
    os.remove("xyz.dat")
    os.rename("temp.dat","xyz.dat")
    menu()

def delreg():
    rec=[]
    screg=int(input("Enter the Registration Number to be modified"))
    with open("xyz.dat", "rb") as fp:
        fs=open("temp.dat","wb")
        try:
            while True:
                line = pickle.load(fp)
                rec=line
                if screg!=rec[2]:
                    pickle.dump(rec,fs)                    
        except EOFError:
            fp.close()
            fs.close() 
    os.remove("xyz.dat")
    os.rename("temp.dat","xyz.dat")
    menu()
    
def menu():      
    print("\t\tABC School Admission System")    
    print("\t1. Create a Table")
    print("\t2. Add a Record")
    print("\t3. Display all Records")
    print("\t4. Search a Record on Admission number ")
    print("\t5. Search a Record on Registration number ")
    print("\t6. Search Records on Registration Date ")
    print("\t7. Search Records on Name of Candidate ")
    print("\t8. Search Records on Gender ")
    print("\t9. Search a Record on Caste ")
    print("\t10. Search a Record on Aadhar Card number ")
    print("\t11. Search Records on Standard to which admission taken ")
    print("\t12. Modify the Information of the Student")
    print("\t13. Remove record from Table")
    print("\t14. Exit ")
    ch=int(input("Enter choice"))
    if(ch==1):
        create()
    if(ch==2):
        append()
    if(ch==3):
        dispall()
    if(ch==4):
        searchadm()   
    if(ch==5):
        searchreg()
    if(ch==6):
        searchregdate()
    if(ch==7):
        searchname()    
    if(ch==8):
        searchgen()
    if(ch==9):
        searchcaste()
    if(ch==10):
        searchaadhar()
    if(ch==11):
        searchclass()
    if(ch==12):
        modifyreg()
    if(ch==13):
        delreg()
    
menu()