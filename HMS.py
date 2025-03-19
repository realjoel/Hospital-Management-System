import mysql.connector as ms
mydb=ms.connect(host="localhost",user="root",passwd="abhi2003",database="hospital")
if mydb.is_connected():
    print("connected")
cr1=mydb.cursor()

def viewdoctor():
    print("""
              1.View whole data
              2.View a single data""")
    c=int(input("enter your choce"))
    print("")
    if c==1:
        q1="select * from docter"
        cr1.execute(q1)
        row=cr1.fetchall()
        print("""
        the details are:-""")
        for i in row:
            print(i)
    elif c==2:
        docid=input("enter the DoctorId to view the details of the doctor")
        if len(docid)==4:
            print("please wait")
            q1="select * from docter where DocId=(%s)"%(docid)
            cr1.execute(q1)
            row=cr1.fetchall()
            print("""
            the details are:-""")
            for i in row:
                print(i)
        else:
            print("Enter valid DoctorID")
    else:
        print("Please enter a valid choice")
def adddoctor():
    print("")
    DocId=input("Enter the DoctorId : ")
    if len(DocId)==4:
        name=input("Enter the name of the doctor : ")
        PhNo=int(input("Enter the phone number of the docter : "))
        age=int(input("Enter age of the doctor: "))
        specialisation=input("Enter the specialisation of the doctor : ")
        salary=int(input("enter the salary of the docter"))
        cr1.execute("insert into docter(DocId,name,age,PhNo,specialisation,salary)values('%s','%s',%s,%s,'%s',%s)"%(DocId,name,age,PhNo,specialisation,salary))
        mydb.commit()
    else:
        print("Please enter a valid DocId")

def modifydoctor():
    print("")
    DocId=input("Enter the DoctorId for which you want to modify the data: ")
    if len(DocId)==4:
        print("""
                  1.change salary.
                  2.change age.
                  3.change phone number.
                  4.delete the whole data.
                  """)
        choice=int(input("Enter your choice"))
        if choice==1:
            salary=int(input("Enter the new salary"))
            q1="update docter set salary=(%s) where DocId=('%s')"%(salary,DocId)
            cr1.execute(q1)
            mydb.commit()
            print("The value has been updated")
        elif choice==2:
            age=int(input("Enter the age"))
            q2="update docter set age=(%s) where DocId=('%s')"%(age,DocId)
            cr1.execute(q2)
            mydb.commit()
            print("The value has been updated")
        elif choice==3:
            phno=int(input("Enter the new phone numebr"))
            q3="update docter set PhNo=(%s) where DocId=('%s')"%(phno,DocId)
            cr1.execute(q3)
            mydb.commit()
            print("The value has been updated")
        elif choice==4:
            q4="delete from docter where DocId=('%s')"%(DocId)
            cr1.execute(q4)
            mydb.commit()
            print("The data has been deleted")
        else:
            print("Enter a valid input")
    else:
        print("Enter valid docterid")
        
def viewnurse():
    print("""
              1.View whole data
              2.View a single data""")
    c=int(input("enter your choce"))
    print("")
    if c==1:
        q1="select * from nurse"
        cr1.execute(q1)
        row=cr1.fetchall()
        print("""
        the details are:-""")
        for i in row:
            print(i)
    elif c==2:
        nurid=input("enter the NurseId to view the details of the Nurse")
        if len(nurid)==4:
            print("please wait")
            q1="select * from nurse where NurId=(%s)"%(nurid)
            cr1.execute(q1)
            row=cr1.fetchall()
            print("""
            the details are:-""")
            for i in row:
                print(i)
        else:
            print("Enter valid NurseID")
    else:
        print("Please input a vaild choice")
def addnurse():
    print("")
    NurId=input("Enter the NurseId : ")
    if len(NurId)==4:
        name=input("Enter the name of the nurse : ")
        PhNo=int(input("Enter the phone number of the nurse : "))
        age=int(input("Enter age of the nurse: "))
        salary=int(input("enter the salary of the nurse"))
        cr1.execute("insert into nurse(NurId,name,age,PhNo,salary)values('%s','%s',%s,%s,%s)"%(NurId,name,age,PhNo,salary))
        mydb.commit()
    else:
        print("Please enter a valid NurseId")
        
def modifynurse():
    print("")
    NurId=input("Enter the NurseId for which you want to modify the data: ")
    if len(NurId)==4:
        print("""
                  1.change salary.
                  2.change age.
                  3.change phone number.
                  4.delete the whole data.
                  """)
        choice=int(input("Enter your choice"))
        if choice==1:
            salary=int(input("Enter the new salary"))
            q1="update nurse set salary=(%s) where NurId=('%s')"%(salary,NurId)
            cr1.execute(q1)
            mydb.commit()
            print("The value has been updated")
        elif choice==2:
            age=int(input("Enter the age"))
            q2="update nurse set age=(%s) where NurId=('%s')"%(age,NurId)
            cr1.execute(q2)
            mydb.commit()
            print("The value has been updated")
        elif choice==3:
            phno=int(input("Enter the new phone numebr"))
            q3="update nurse set PhNo=(%s) where NurId=('%s')"%(phno,NurId)
            cr1.execute(q3)
            mydb.commit()
            print("The value has been updated")
        elif choice==4:
            q4="delete from nurse where NurId=('%s')"%(NurId)
            cr1.execute(q4)
            mydb.commit()
            print("The data has been deleted")
        else:
            print("Enter a valid input")
    else:
        print("Enter valid Nurid")
        
def viewotherw():
    print("""
              1.View whole data
              2.View a single data""")
    c=int(input("enter your choce"))
    print("")
    if c==1:
        q1="select * from otherworkers"
        cr1.execute(q1)
        row=cr1.fetchall()
        print("""
        the details are:-""")
        for i in row:
            print(i)
    elif c==2:
        othid=input("enter the Otherworkers Id to view the details of the Otherworkers")
        if len(othid)==4:
            print("please wait")
            q1="select * from otherworkers where OthId=(%s)"%(othid)
            cr1.execute(q1)
            row=cr1.fetchall()
            print("""
            the details are:-""")
            for i in row:
                print(i)
        else:
            print("Enter valid OtherworkersID")
    else:
        print("Please input a valid choice")
        
def addotherw():
    print("")
    OthId=input("Enter the OtherworkersId : ")
    if len(OthId)==4:
        name=input("Enter the name of the worker : ")
        PhNo=int(input("Enter the phone number of the worker: "))
        age=int(input("Enter age of the worker: "))
        occupation=input("Enter the occupation of the worker : ")
        salary=int(input("enter the salary of the worker"))
        cr1.execute("insert into otherworkers(OthId,name,age,PhNo,occupation,salary)values('%s','%s',%s,%s,'%s',%s)"%(OthId,name,age,PhNo,occupation,salary))
        mydb.commit()
    else:
        print("Please enter a valid OtherworkersId")
    
def modifyotherw():
    print("")
    OthId=input("Enter the OtherworkersId for which you want to modify the data: ")
    if len(OthId)==4:
        print("""
                  1.change salary.
                  2.change age.
                  3.change phone number.
                  4.delete the whole data.
                  """)
        choice=int(input("Enter your choice"))
        if choice==1:
            salary=int(input("Enter the new salary"))
            q1="update otherworkers set salary=(%s) where OthId=('%s')"%(salary,OthId)
            cr1.execute(q1)
            mydb.commit()
            print("The value has been updated")
        elif choice==2:
            age=int(input("Enter the age"))
            q2="update otherworkers set age=(%s) where OthId=('%s')"%(age,OthId)
            cr1.execute(q2)
            mydb.commit()
            print("The value has been updated")
        elif choice==3:
            phno=int(input("Enter the new phone numebr"))
            q3="update otherworkers set PhNo=(%s) where OthId=('%s')"%(phno,OthId)
            cr1.execute(q3)
            mydb.commit()
            print("The value has been updated")
        elif choice==4:
            q4="delete from Otherworkers where OthId=('%s')"%(OthId)
            cr1.execute(q4)
            mydb.commit()
            print("The data has been deleted")
        else:
            print("Enter a valid input")
    else:
        print("Enter valid Otherworkers id")


def viewpa():
    print("""
              1.View whole data
              2.View a single data""")
    c=int(input("enter your choce"))
    print("")
    if c==1:
        q1="select * from patient"
        cr1.execute(q1)
        row=cr1.fetchall()
        print("""
        the details are:-""")
        for i in row:
            print(i)
    elif c==2:
        PaId=input("enter the PaId to view the details of the patient")
        if len(PaId)==4:
            print("please wait")
            q1="select * from patient where PaId=(%s)"%(PaId)
            cr1.execute(q1)
            row=cr1.fetchall()
            print("""
            the details are:-""")
            for i in row:
                print(i)
        else:
            print("Enter valid PatientID")
    else:
        print("Please input a valid choice")
        
def addpa():
    print("")
    PaId=input("Enter the PatientId : ")
    if len(PaId)==4:
        name=input("Enter the name of the patient : ")
        PhNo=int(input("Enter the phone number of the patient: "))
        age=int(input("Enter age of the patient: "))
        cr1.execute("insert into patient(PaId,name,age,PhNo)values('%s','%s',%s,%s)"%(PaId,name,age,PhNo))
        mydb.commit()
    else:
        print("Please enter a valid PatientId")
        
        
def modifypa():
    print("")
    PaId=input("Enter the PatientId for which you want to modify the data: ")
    if len(PaId)==4:
        print("""
                  1.change age.
                  2.change phone number.
                  3.delete the whole data.
                  """)
        choice=int(input("Enter your choice"))
        if choice==1:
            age=int(input("Enter the age"))
            q2="update patient set age=(%s) where PaId=('%s')"%(age,PaId)
            cr1.execute(q2)
            mydb.commit()
            print("The value has been updated")
        elif choice==2:
            phno=int(input("Enter the new phone numebr"))
            q3="update patient set PhNo=(%s) where PaId=('%s')"%(phno,PaId)
            cr1.execute(q3)
            mydb.commit()
            print("The value has been updated")
        elif choice==3:
            q4="delete from patient where PaId=('%s')"%(PaId)
            cr1.execute(q4)
            mydb.commit()
            print("The data has been deleted")
        else:
            print("Enter a valid input")
    else:
        print("Enter valid Patient id")
        
def viewdocp():
    print("available docters are:-")
    q1="select name,specialisation from docter"
    cr1.execute(q1)
    row=cr1.fetchall()
    print("""
    the details are:-""")
    for i in row:
         print(i)
    

        
def docter1():
    print("your choice is-DOCTOR")
    print("")
    print("""
                 what would you like to do now
                 
                 1.VIEW DOCTORS DETAILS
                 2.ADD NEW DOCTOR
                 3.MODIFY DOCTOR DETAILS.
                 4.Exit""")
    cd=int(input("enter your choice"))
    if cd==1:
        print("your choice is-VIEW DOCTORS DETAILS")
        viewdoctor()
    elif cd==2:
        print("your choice is-ADD NEW DOCTOR")
        adddoctor()
    elif cd==3:
        print("your choice is-MODIFY DOCTOR DETAILS")
        modifydoctor()
    elif cd==4:
        print("Exiting")
    else:
        print("Invalid choice")

def nurse1():
    print("your choice is-Nurse")
    print("")
    print("""
                 what would you like to do now
                 
                 1.VIEW NURSE DETAILS
                 2.ADD NEW NURSE
                 3.MODIFY NURSE DETAILS.
                 4.Exiting.""")
    cn=int(input("enter your choice"))
    if cn==1:
        print("your choice is-VIEW NURSE DETAILS")
        viewnurse()
    elif cn==2:
        print("your choice is-ADD NEW NURSE")
        addnurse()
    elif cn==3:
        print("your choice is-MODIFY NURSE DETAILS")
        modifynurse()
    elif cn==4:
        print("Exiting")
    else:
        print("Invalid choice")
            
def otherworker1():
    print("your choice is-Nurse")
    print("")
    print("""
                 what would you like to do now
                 
                 1.VIEW OTHERWORKERS DETAILS.
                 2.ADD OTHERWORKERS.
                 3.MODIFY OTHERWORKERS DETAIL.
                 4.Exit.""")
    co=int(input("enter your choice"))
    if co==1:
        print("your choice is-VIEW OTHERWORKERS DETAILS")
        viewotherw()
    elif co==2:
        print("your choice is-ADD NEW OTHERWORKER")
        addotherw()
    elif co==3:
        print("your choice is-MODIFY OTHERWORKERS DETAILS")
        modifyotherw()
    elif co==4:
        print("Exiting")
    else:
        print("Invalid choice")
    
    
    
import webbrowser
print("""

          WELCOME TO AJ HOSPITAL
          ----------------------

          1.Admin(management)
          
          2.User
          
          3.open Hospital tips.
          
          4.Exit
          """)
choice=int(input("Enter your choice"))
while True:
    if choice==1:
        print("your choice is-Admin")
        print("")
        print("""
             which of the following would you like to access
             
             1.Docter
             2.Nurse
             3.Other worker(staff)
             4.Exit    """)
    
        c1=int(input("enter ur choice"))
    
        if c1==1:
            docter1()
            
        elif c1==2:
            nurse1()
        
        elif c1==3:
            otherworker1()
        elif c1==4:
            print("Exiting")
            break
        else:
            print("Invalid choice")
               
            
    elif choice==2:
        print("your choice is-User")
        print("")
        print("""what would you like to do now
                 
                 1.VIEW Patient DETAILS
                 2.ADD NEW Patient.
                 3.MODIFY Patient DETAILS.
                 4.view doctors.
                 5.Exit""")
        cp=int(input("enter your choice"))
        if cp==1:
            print("your choice is-VIEW PATIENT DETAILS")
            viewpa()
        elif cp==2:
            print("your choice is-ADD NEW PATIENT")
            addpa()
        elif cp==3:
            print("your choice is-MODIFY PATIENT DETAILS")
            modifypa()
        elif cp==4:
            viewdocp()
        elif cp==5:
            print("Exiting")
            break
        else:
            print("Invalid choice")
            
    elif choice==3:
        print("""
                1.Patient safety Tips.
                2.Tips on Corona safety.
                """)
        ch=int(input("Enter ur choice"))
        if ch==1:
            print("opening website")
            webbrowser.open('https://www.ahrq.gov/patients-consumers/diagnosis-treatment/hospitals-clinics/10-tips/index.html')
            print("......")
            print("website opened")
            break
        elif ch==2:
            print("opening website")
            webbrowser.open('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public')
            print("......")
            print("website opened")
            break
        else:
            print("Please input a valid choice")
    
    elif choice==4:
        print("Exiting")
        break

    else:
       print("Invalid Input")
       break
print("")    
print("HAVE A NICE DAY")
print("Stay Home & Stay Safe")
from emoji import emojize 
print(emojize(":red_heart:"))
