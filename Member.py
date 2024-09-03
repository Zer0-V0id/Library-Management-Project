from SQLcmds import *

def last():
    with open("lastID.txt",'r') as file1:
        x=file1.read()
    return x

def lastupdate(Id):
    with open("lastID.txt",'w') as file2:
        file2.write(str(Id))

def addM():
    Id = int(last())
    Name = input("Enter Member name: ")
    Id = Id + 1
    Mail = input("Enter Mail id: ")
    sqladdM(Id, Name, Mail)
    lastupdate(Id)
    sqldep(Id, "Membership", 500)
    return Id

def delM():
    Id = input("Enter Member Id: ")
    sqldelM(Id)
    return Id
    
def seaM(inp):
    try: 
        if int(inp) == 1:
            Id =  int(input("Enter Member ID: "))
            Member = sqlseaM(Id, "ID")
        elif int(inp) == 2:
            Name = input("Enter Member Name: ")
            Member = sqlseaM(Name, "Name")
        else:
            print("Please enter a valid choice.")
            return
           
    except TypeError:
        print("Please enter a valid choice.")
        return

    try:
        print(', '.join(map(str,Member)))
    except TypeError:
        print("Not found")