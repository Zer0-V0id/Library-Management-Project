def Create():
	import pymysql
	pwd=input("Enter MySQL password for necessary Database and Table creation: ")
	con = pymysql.connect(host="localhost", user="root", passwd=pwd, autocommit="True")
	cur=con.cursor()
	s="CREATE DATABASE Library"
	cur.execute(s)

	con1 = pymysql.connect(host="localhost", user="root", passwd=pwd, database="Library", autocommit="True")
	cur1=con1.cursor()

	s1="CREATE TABLE `Members` (`ID` INT NOT NULL, `Name` VARCHAR(30) NOT NULL, `DOR` DATE NOT NULL, `Issued_Book` VARCHAR(13),`Mail_ID` VARCHAR(40), PRIMARY KEY (`ID`))"
	cur1.execute(s1)

	s2="CREATE TABLE `Books` (`ISBN` VARCHAR(13) NOT NULL, `Books_Name` VARCHAR(30) NOT NULL, `Author_Name` VARCHAR(30) NOT NULL, `Publisher_Name` VARCHAR(40) NOT NULL, `Categories` TEXT, `Current_Issuer` INT, FOREIGN KEY (`Current_Issuer`) REFERENCES `Members`(`ID`))"
	cur1.execute(s2)

	s3="CREATE TABLE `Issued` (`ISBN` VARCHAR(13) NOT NULL, `ID` INT NOT NULL, `Issue_Date` DATE NOT NULL, FOREIGN KEY (`ID`) REFERENCES `Members`(`ID`))"
	cur1.execute(s3)

	s4="CREATE TABLE `Ordered` (`ISBN` VARCHAR(13) NOT NULL, `Ordered_On` DATE NOT NULL, PRIMARY KEY (`ISBN`))"
	cur1.execute(s4)

	s5="CREATE TABLE `Quarantined` (`ISBN` VARCHAR(13) NOT NULL, `Quarantined_On` DATE NOT NULL, PRIMARY KEY (`ISBN`))"
	cur1.execute(s5)

	s6="CREATE TABLE `Finance` (`ID` VARCHAR(13) NOT NULL, `Received_On` DATE NOT NULL, `Source` VARCHAR(30) NOT NULL, `Amount` INT NOT NULL)"
	cur1.execute(s6)

	s7="CREATE TABLE `Record` (`ISBN` VARCHAR(13) NOT NULL, `ID` INT NOT NULL, `Issue_Date` DATE NOT NULL)"
	cur1.execute(s7)

def Updateid():
    with open("lastID.txt",'w') as file2:
        file2.write("0")