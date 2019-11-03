import sqlite3

connBook = sqlite3.connect('books.db')
print("first db connected successfully")

connStud = sqlite3.connect('students.db')
print("second db connected successfully")


# defining view function here

def View():

    tp = input("Searching for (book/student) : ")

    Key = input("\n Enter ID : ")

    if tp == 'book' :
        curr = connBook.cursor()
        data = Key
        curr.execute("SELECT * from book where id = ?",data)
        rows = curr.fetchall()

        # for row in rows:
        #     print(row)

        print("ID = " + row[0])
        print("NAME = " + row[1])
        print("STATUS = " + row[2])
        print("BORROWER = " + row[3])
        print("RETURN DATE = " + row[4])

    if tp == 'student' :
        curr = connBook.cursor()
        data = Key
        curr.execute("SELECT * from student where id = ?",data)
        rows = curr.fetchall()

        # for row in rows:
        #     print(row)

        print("ID = " + row[0])
        print("NAME = " + row[1])
        print("STATUS = " + row[2])
        print("BOOK1 ID = " + row[3])
        print("RETURN DATE = " + row[4])
        print("BOOK2 ID = " + row[5])
        print("RETURN DATE = " + row[6])
        print("BOOK3 ID = " + row[7])
        print("RETURN DATE = " + row[8])    
        print("FINE = "+ row[9])    


#view function complete



#defining borrow function here

def Borrow():
    key1 = input("Enter student id : ")

    key2 = input("Enter book id : ")


    #updating book table

    currBook = connBook.cursor()

    data = (key1,key2)

    currBook.execute("update book set  BORROWER-ID = ? where ID = ?",data)

    connBook.commit()

    # now updating student table
    currStud = connStud.cursor()

    data = (key2,key1)

    currBook.execute("update book set BOOK-ID = ? where ID = ?",data)

    connBook.commit()


#borrow function complete

command = input("Enter the command : ")

if command == 'view':
    View()
elif command == 'borrow':
    Borrow()
elif command == 'return':
    Return()
elif command ==  'renew':
    Renew()


