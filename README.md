# Library-Management-Project
Library Management Project using Python and MySQL


1. PROBLEM STATEMENT
A library management is a system that manages and stores information of books electronically according to a student’s needs. The system helps both the user and admin to keep a constant track of all the books
available in the library. It allows both the user and admin to search for the desired book. This task if carried out manually will be tedious and includes chances of mistakes. These errors are avoided by allowing the system to keep track of information and thus there is no need to keep manual track of this information which thereby avoids chances of mistakes. Thus, this system primarily reduces manual work allowing smooth flow of library activities by removing chances of errors.
…
2. METHODOLOGY / PROCEDURE/ ALGORITHM
We have used a basic menu for all the choices the user will have on opening the system.
……………………..……………………..……………………..……………………..
The user can select from a number of menu choices within the program of:
……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..……………………..
1. Add book
2. Update book
3. Delete book
4. Search book
5. Issue book
6. Return book
7. Display books
8. Display students
Choice 1 → receive book data as input → add data to sql table → return to menu
Choice 2 → select book that needs to be updated → receive new data of book → update data in sql table → return to menu
Choice 3 → select book that needs to be delete → delete entry of the book from sql table → return to menu
Choice 4 → receive search data → display books according to search data
Choice 5 → select book that needs to be issued → add book data into student table in sql → return to menu
Choice 6 → show and select book that needs to be returned → remove book data from student table in sql → return to menu
Choice 7 → display the books table
Choice 8 → display the students table

3. FLOW CHART


![image](https://github.com/user-attachments/assets/9eb7c3c8-cf8f-425e-aaac-aa89c9961085)
![image](https://github.com/user-attachments/assets/b263cd6b-35a4-47ce-905d-1fd5ad3faee3)

4. MODULES OF THE PROPOSED WORK
I. pymysql
PyMySQL is a pure-Python MySQL client library, which means it is a Python package that creates an API interface for us to access MySQL relational databases.
……………………..………………………………..……………………..……………………..……………………..…………..……………………..……………………..
II. Pwinput
A cross-platform Python module that displays **** for password input.

This project on Library Management provides a computerized version of a physical library. This makes the working of the library much more efficient, quick and comfortable for students and the admin. User can search, issue and return books with a few clicks due to be returned books easily.
……………..……………………..……………..……………………..……………..……………………..……………..……………………..
A unique ID called ISBN is used in the system to provide unique identification to all users to effectively manage all students. This system saves a lot of time and solves the problems of a physical library.
……………………..……………………..……………..……………………..
It also eliminates the possibility of human error from the system. 

