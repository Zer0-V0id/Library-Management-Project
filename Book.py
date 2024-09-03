from SQLcmds import *
from tabulate import tabulate

def addB():
    Isbn =  input("Enter book ISBN: ")
    Name = input("Enter book name: ")
    Author = input("Enter book author name: ")
    Publisher = input("Enter publisher name: ")
    Category = input("Enter book category: ")
    sqladdB(Isbn, Name, Author, Publisher, Category)
    return Isbn

def quaB():
    Isbn = input("Enter book ISBN: ")
    sqlquaB(Isbn)
    return Isbn

def issB():
    Isbn = input("Enter book ISBN: ")
    Id = input("Enter member ID: ")
    while True: 
        if checkissuem(Id) == False:
            return "Due"
            break
        if checkissueb(Isbn) == False:
            return "Issued"        
            break
        sqlissB(Isbn, Id)
        break

def retB():
    Id = input("Enter member ID: ")
    Isbn = sqlfind(Id)
    D = sqlfine(Id)
    sqlretB(Id)

    if int(D) > 7:
        fine = (int(D)-7)*10
    else:
        fine=0

    sqldep(Id, "Fine", fine)
    return Isbn, D, fine

def seaB(inp):
    try:
        if int(inp) == 1:
            Isbn = input("Enter book ISBN: ")
            Book = sqlseaB(Isbn,"ISBN")

        elif int(inp) == 2:
            Name = input("Enter book name: ")
            Book = sqlseaB(Name,"Books_Name")

        elif int(inp) == 3:
            Author = input("Enter book Author name:")
            Book = sqlseaB(Author,"Author_Name")

        elif int(inp) == 4:
            Pub = input("Enter book publications name:")
            Book = sqlseaB(Pub,"Publisher_Name")

        elif int(inp) == 5:
            Genre = input("Enter book genre:")
            Book = sqlseaB(Genre,"Categories")

        else:
            print("Please enter a valid choice.")
            return
           
    except TypeError:
        print("Please enter a valid choice.")
        return

    try:
        print(', '.join(map(str,Book)))
    except TypeError:
        print("Not found")

def dueB():
    C=0
    for x in sqldueB():
        print(', '.join(map(str,x)))
        C+=1
    if C==0:
        print("No Due Books.")

def report(inp):
    try:
        if int(inp) == 1:
            Result, field_names = curissue()
        elif int(inp) == 2:
            Result, field_names = mostissuedb()
        elif int(inp) == 3:
            Result, field_names = mostissuedauthor()
        elif int(inp) == 4:
            Result, field_names = mostissuedgenre()
        elif int(inp) == 5:
            Result, field_names = monthissue()
        elif int(inp) == 6:
            Result, field_names = monthquar()
        elif int(inp) == 7:
            Result, field_names = ordered()
        elif int(inp) == 8:
            Result, field_names = monthdue()
        elif int(inp) == 9:
            Result, field_names = monthfinance()
        elif int(inp) == 10:
            Result, field_names = monthmember()
        elif int(inp) == 11:
            Result, field_names = monthincome()
        elif int(inp) == 12:
            Result, field_names = listB()
        elif int(inp) == 13:
            Result, field_names = listM()
        else:
            print("Please enter a valid choice.")
            return
           
    except TypeError:
        print("Please enter a valid choice.")
        return

    try:
        print(tabulate(Result, headers=field_names, tablefmt='psql'))
    except TypeError:
        print("Not found")

def ordB():
    Isbn =  input("Enter book ISBN: ")
    sqlordB(Isbn)
    return Isbn
    
