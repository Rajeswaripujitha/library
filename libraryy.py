import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123@Pujitha#1",
    database="library"
)

def addbook():
    bname = input("Enter book name: ")
    bcode = input("Enter book code:")
    total = input("Total books:")
    sub = input("Enter subject:")
    data = (bname,bcode,total,sub)
    sql = "insert into books(bname,bcode,total,subject) values(%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")
    main()
def updatebook():
    bcode = input("Enter book code to update: ")

    sql = "SELECT * FROM books WHERE bcode = %s"
    data = (bcode,)
    c = mydb.cursor()
    c.execute(sql,data)
    existing_book = c.fetchone()

    if existing_book:
        new_bname = input("Enter new book name: ")
        new_total = input("Enter new total books: ")
        new_sub = input("Enter new subject: ")

        sql = "UPDATE books SET bname = %s, total = %s, subject = %s WHERE bcode = %s"
        data = (new_bname, new_total, new_sub, bcode)

        c.execute(sql,data)
        mydb.commit()

        print(".............")
        print("Data updated successfully")
        main()
    else:
        print("Book with the given code does not exist.")
        main()


def dispbook():
    sql = "select * from books"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book id : ",i[0])
        print("Book name:",i[1])
        print("Book code:",i[2])
        print("Total:",i[3])
        print("Subject:",i[4])
        print("................")
    main()


def main():
    print("""............LIBRARY MANAGEMENT.............
    1.Add book
    2.Update book
    3.Display book
    """)
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        updatebook()
    elif(choice == '3'):
        dispbook()
    else:
        print("wrong choice")
        main()


main()




