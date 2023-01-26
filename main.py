print("Initializing...")
import sqlite3
from operator import contains
import array

conn = sqlite3.connect('phonedata.db')
conn.execute('CREATE TABLE IF NOT EXISTS data(number TEXT, realname TEXT, grade TEXT, nickname TEXT, address TEXT, description TEXT)')
c = conn.cursor()

print('''
____________________
|  ----------   |  |    ___________________
|  ----------   |  |   | The Big Phonebook |
|  ----------   |  |   |___________________|
|  ----------   |  |
|  ----------   |  |
|  ----------   |  |
|  ----------   |  |
|  ----------   |  |
|  ----------   |  |
|               |  |
|_______________|__|

Status : ready

1 | Search by number
2 | Search by nickname
3 | Search by realname
4 | Input Data
5 | Delete Data
''')

menu = input("Enter a number to continue : ")
if menu == "1":
    print("===Search by number===")
    srch_input1 = input("Number : ")
    c.execute("SELECT * FROM data WHERE number=?", (srch_input1,))
    for row in c.fetchall():
        tempdata = row
        for list in tempdata:
                        print(list)
elif menu == "2":
    print("===Search by nickname===")
    srch_input2 = input("Nick Name : ")
    c.execute("SELECT * FROM data WHERE nickname=?", (srch_input2,))
    for row in c.fetchall():
        tempdata = row
        for list in tempdata:
                        print(list)
elif menu == "3":
    print("===Search by realname===")
    srch_input3 = input("Real Name : ")
    c.execute("SELECT * FROM data WHERE realname=?", (srch_input3,))
    for row in c.fetchall():
        tempdata = row
        for list in tempdata:
                        print(list)
elif menu == "4":
    while True:
        def input_data():
            print("===Input Data===")
            nmbr_input = input("Phone Number : ".lower())
            realname_input = input("Real Name : ".lower())
            nickname_input = input("Nick Name : ".lower())
            grade_input = input("Grade : ".lower())
            addr_input = input("Address : ".lower())
            description_input = input("Description : ".lower())
            c.execute("INSERT INTO data(number, realname, grade, nickname, address, description) VALUES(?, ?, ?, ?, ?, ?)", [nmbr_input, realname_input, grade_input, nickname_input, addr_input, description_input])
        input_data()
        inp_opt_continue = input("Input another data? (y/n) ")
        if inp_opt_continue == "y":
            pass
        else:
            break
elif menu == "5":
    print("===Delete data===")
    srch_input5 = input("Number : ")
    try:
        c.execute("DELETE FROM data WHERE number = ?", (srch_input5,))
        print("Successfully deleted " + srch_input5 + " data")
    except:
        print("Error! Cannot delete data.")
else:
    print("Error! please input a valid number")
conn.commit()
c.close()
conn.close()
