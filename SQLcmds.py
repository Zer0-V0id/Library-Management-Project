import pymysql
pwd=input("Enter MySQL password: ")
con = pymysql.connect(host="localhost", user="root", passwd=pwd, database="Library", autocommit="True")
cur=con.cursor()

def sqladdB(Isbn, Name, Author, Publisher, Category):
	s="INSERT INTO Books (ISBN, Books_Name, Author_Name, Publisher_Name, Categories) VALUES('{}', '{}', '{}', '{}', '{}')".format(Isbn,Name,Author,Publisher,Category)
	cur.execute(s)

def sqlquaB(Isbn):
	s1="INSERT INTO Quarantined (ISBN, Quarantined_On) VALUES('{}', curdate())".format(Isbn)
	cur.execute(s1)

	s2="DELETE from Books WHERE ISBN = '{}'".format(Isbn)
	cur.execute(s2)

def checkissueb(Isbn):
	s="SELECT Current_Issuer from Books where ISBN = {}".format(Isbn)
	cur.execute(s)
	r=list(cur.fetchall())
	if r[0][0] != None:
		return False

def checkissuem(Id):
	s="SELECT Issued_Book from Members where ID = {}".format(Id)
	cur.execute(s)
	r=list(cur.fetchall())
	if r[0][0] != None:
		return False

def sqlissB(Isbn,Id):
	s="UPDATE Books set Current_Issuer = '{}' WHERE ISBN = '{}'".format(Id,Isbn)
	s0="UPDATE Members set Issued_Book = '{}' WHERE ID = '{}'".format(Isbn,Id)
	s1="INSERT into Issued (ISBN,ID,Issue_Date) VALUES('{}', '{}', curdate())".format(Isbn,Id)
	s2="INSERT into Record (ISBN,ID,Issue_Date) VALUES('{}', '{}', curdate())".format(Isbn,Id)
	cur.execute(s)
	cur.execute(s0)
	cur.execute(s1)
	cur.execute(s2)

def sqlretB(Id):
	s="DELETE FROM Issued WHERE ID = '{}'".format(Id)
	s0="UPDATE Books set Current_Issuer = null where Current_Issuer = '{}'".format(Id)
	s1="UPDATE Members set Issued_Book = null where ID = '{}'".format(Id)
	cur.execute(s)
	cur.execute(s0)
	cur.execute(s1)

def sqlseaB(Keyword, Column):
	s="SELECT * FROM Books WHERE {} = '{}'".format(Column, Keyword)
	cur.execute(s)
	r= cur.fetchall()
	for Book in r:
		return(Book)

def sqlordB(Isbn):
	s="INSERT into Ordered (ISBN, Ordered_On) VALUES('{}', curdate())".format(Isbn)
	cur.execute(s)

def sqladdM(Id,Name,Mail):
	s="INSERT into Members (ID, Name, DOR, Mail_ID) VALUES('{}', '{}', curdate(), '{}')".format(Id,Name,Mail) 
	cur.execute(s)

def sqldelM(Id):
	s="DELETE FROM Members WHERE ID = '{}'".format(Id)
	cur.execute(s)

def sqlseaM(Keyword,Column):
	s="SELECT * FROM Members WHERE {} = '{}'".format(Column, Keyword)
	cur.execute(s)
	r= cur.fetchall()
	for Member in r:
		return(Member)

def sqlfine(Id):
	s="SELECT DATEDIFF(Issue_Date, curdate()) from Issued WHERE ID = '{}'".format(Id)
	cur.execute(s)
	if r[0][0] != None:
		return False
	return cur.fetchone()[0]

def sqlfind(Id):
	s="SELECT ISBN FROM Issued WHERE ID = {}".format(Id)
	cur.execute(s)
	Isbn = cur.fetchone()
	return Isbn[0]

def sqldep(Id, Source, Amount):
	s="INSERT INTO Finance (ID, Received_On, Source, Amount) VALUES('{}', curdate(), '{}', '{}')".format(Id, Source, Amount)
	cur.execute(s)

def curissue():
	s="SELECT * FROM Issued"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def mostissuedb():
	s="SELECT ID, COUNT(ID) FROM Record GROUP BY ID ORDER BY COUNT(ID) DESC"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def mostissuedauthor():
	s="SELECT RECORD.ISBN, COUNT(RECORD.ISBN) FROM RECORD INNER JOIN Books ON RECORD.ISBN = Books.ISBN GROUP BY RECORD.ISBN ORDER BY COUNT(Books.Author_Name) DESC"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def mostissuedgenre():
	s="SELECT RECORD.ISBN, COUNT(RECORD.ISBN) FROM RECORD INNER JOIN Books ON RECORD.ISBN = Books.ISBN GROUP BY RECORD.ISBN ORDER BY COUNT(Books.Categories) DESC"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def monthissue():
	s="SELECT * FROM Record WHERE MONTH(Issue_Date) = MONTH(curdate())"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def monthquar():
	s="SELECT * FROM Quarantined WHERE MONTH(Quarantined_On) = MONTH(curdate())"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def ordered():
	s="SELECT * FROM Ordered"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def monthdue():
	s="SELECT * FROM Issued WHERE Issue_Date < DATE_ADD(curdate(), INTERVAL -30 DAY)"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def monthfinance():
	s="SELECT * FROM Finance WHERE MONTH(Received_On) = MONTH(curdate())"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def monthmember():
	s="SELECT COUNT(DISTINCT ID) FROM Finance WHERE MONTH(Received_On) = MONTH(curdate()) and Amount = 500"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def monthincome():
	s="SELECT SUM(Amount) FROM Finance WHERE MONTH(Received_On) = MONTH(curdate())"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def listB():
	s="SELECT * FROM Books"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

def listM():
	s="SELECT * FROM Members"
	cur.execute(s)
	r= cur.fetchall()
	if r[0][0] != None:
		return False
	field_names = [i[0] for i in cur.description]
	return r, field_names

