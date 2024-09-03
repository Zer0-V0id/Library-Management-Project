from DB_and_table_creation import *
inp = input("Is this the first time running program on the system?(Y/N): ")
if inp in ['Y','y']:
    Create()
    Updateid()

from Book import *
from Member import *
import pwinput

def Login():
    print("~Log-In~")
    Authorized={"test":"1234"}
    UserId=input("Enter Your Username: ")
    Password=pwinput.pwinput(prompt='Enter your password: ', mask='*')
    
    if UserId in Authorized and Authorized[UserId] == Password:
        print("Successful Login!")
        print()
        print('''
            ~~~~~~~~~~LIBRARY MANAGEMENT SYSTEM ZERO~~~~~~~~~~''')
        Menu()
    else:
        print("Please enter a valid Username and Password.")
        Login()
        
def Menu():
    print("--------------------------------------------------------------")
    print("1. Add a Book")
    print("2. Quarantine a Book")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. Search for a Book")
    print("6. Add a Member")
    print("7. Remove a Member")
    print("8. Search for a Member")
    print("0. More")
    
    inp = input("Enter your choice: ")
    print()
    
    try:
        if int(inp) == 0:
            print("9. Generate report")
            print("10. Order a Book")
            print("11. Log Out")
            print("12. Exit")
            inp = input("Enter your choice: ")
            print()
    
        if int(inp) == 1:
            i=addB()
            print("Book {} has been successfully added.".format(i))

        elif int(inp) == 2:
            i=quaB()
            print("Book {} has been successfully quarantined.".format(i))

        elif int(inp) == 3:
            try:
                r = issB()
                if r == "Due":
                    print("Member already has a book issued.")
                elif r == "Issued":
                    print("Book is already issued.")
                else: 
                    print("Book has been successfully issued.")
            except:
                print("Book or Member not found.")


        elif int(inp) == 4:
            i, d, fine = retB()
            print("Days since issue: ",d,". Late fine to be collected (at 10 rupees/day after a week): ",fine)
            print("Book {} has been successfully returned.".format(i))

        elif int(inp) == 5:
            print("--------------------------------------------------------------")
            print("1. Search using ISBN")
            print("2. Search using Name")
            print("3. Search using Author")
            print("4. Search using Publications")
            print("5. Search using Genre")
            inp = input("Enter your choice: ")
            print()
            seaB(inp)

        elif int(inp) == 6:
            i=addM()
            print("Member {} has been successfully added.".format(i))
            print("Please collect the membership amount of Rs. 500")

        elif int(inp) == 7:
            i=delM()
            print("Member {} has been successfully deleted.".format(i))

        elif int(inp) == 8:
            print("--------------------------------------------------------------")
            print("1. Search using ID")
            print("2. Search using Name")
            inp = input("Enter your choice: ")
            print()
            seaM(inp)

        elif int(inp) == 9:
            print("--------------------------------------------------------------")
            print("1. All Currently Issued Books")
            print("2. Most issued books")
            print("3. Most issued author")
            print("4. Most issued genre")
            print("5. All books issued this month")
            print("6. All Books quarantined this month")
            print("7. All ordered books")
            print("8. All books due over a month")
            print("9. This month's financial transactions")
            print("10. No. of Members registered this month")
            print("11. Total income this month")
            print("12. All books in library")
            print("13. All members of library")

            inp = input("Enter your choice: ")
            print()
            report(inp)        

        elif int(inp) == 10:
            i=ordB()
            print("Book {} has been successfully ordered.".format(i))

        elif int(inp) == 11:
            print("Logout Successful.")
            print("--------------------------------------------------------------")
            Login()

        elif int(inp) == 12:
            quit()
            
        else:
            print("Please enter a Valid choice: ")
            Menu()
    except ValueError:
        print("Please enter a Valid choice: ")
        Menu()
    Menu()


Login()
