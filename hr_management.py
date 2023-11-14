# kanoume import to mysql connector
import mysql.connector

# kanoume connect to programma mas me thn database
mycon = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='hr')

# ftiaxnoume to cursor mas
mycur = mycon.cursor()


# gia na dhmiourgisoume ena keno space sto terminal mas
def space():
    for i in range(1):
        print()


# ftiaxnoume query me ola ta ids twn employee
def check():
    qry = 'select emp_id from emp;'
    mycur.execute(qry)

    ids = mycur.fetchall()

    id_list = []
    for i in ids:
        id_list.append(i[0])
    return id_list


# xrhsimopoiontas to add_emp() mporoume na pros8esoume neo employee sthn bash mas
def add_emp():
    ask = 'Y'
    id_list = check()
    while ask in 'yY':
        employee_id = int(input('Give the employee id... '))
        if employee_id in id_list:
            print('This Id already exists....\n'
                  'Try a different id.')
        else:
            emp = ()
            emp_name = input('First Name : ')
            emp_last = input('Last Name : ')
            emp_email = input('Email : ')
            emp_phone = int(input('Phone Number : '))
            emp_address = input('Address : ')
            emp_payment = float(input('Payment : '))
            emp = (employee_id, emp_name, emp_last, emp_email, emp_phone, emp_address, emp_payment)

            qry = 'insert into emp values(%s,%s,%s,%s,%s,%s,%s);'
            val = emp
            mycur.execute(qry, val)
            mycon.commit()
            print('New employee was added')
            space()
            ask = input('Do you want to add more employees?\n'
                        'Y for yes\n'
                        'N for no\n'
                        'Enter your choice: ')
            if ask not in 'Yy':
                space()
                break


# xrhsimopoioume thn view_emp() gia na doume ola ta stoixeia ths bashs mas
def view_emp():
    qry = 'select * from emp;'
    mycur.execute(qry)
    d = mycur.fetchall()
    dic = {}
    for i in d:
        dic[i[0]] = i[1:]
    print('_' * 122)
    print("{:<17} {:<18} {:<18} {:<22} {:<16} {:<17} {:<19}".format(
        'Employee id', 'First Name', 'Last Name', 'Email', 'Phone', 'Address', 'Payment'))
    print('_' * 122)
    for k, v in dic.items():
        a, b, c, d, e, f = v
        print("{:<17} {:<18} {:<18} {:<22} {:<16} {:<17} {:<19}".format(k, a, b, c, d, e, f))
    print('_' * 122)


# me thn del_emp() mporoume na diagrapsoume kapoion employee apo thn bash mas
def del_emp():
    # rwtame prwta na mas epibebaiwsh o xrhsths oti 8elei na sunexisei thn diadikasia
    delt = input('Are you sure you want to fire an employee?\n'
                 'Y to continue\n'
                 'N to cancel\n'
                 'Enter _ ')

    # apo thn stigmh pou mas epibebaiwnei oti 8elei na sunexisei thn diadikasia
    # rwtame na mas pei to id tou employee pou 8elei na apolusei
    if delt in 'Yy':
        confirm = int(input('Please enter the Employee ID : '))
        qry = 'delete from emp where emp_id=%s;'
        mycur.execute(qry, (confirm,))
        mycon.commit()
        print("Employee was fired from the company.")
    # an mas pei oti den 8elei na sunexisei thn diadikasia, thn akurwnoume
    elif delt in 'Nn':
        print('Delete action was cancelled and you will be moved back to the menu.')
    else:
        print('The input you gave is not valid so the action was terminated.')


# mesa sthn actions_emp() kanoume oles tis aparaithtes diadikasies
# epeksergasia employee
# proagwgh (aukshsh mis8ou)
# mexri kai apolush
def actions_emp():
    # zhtame to id tou employee
    ask = int(input('Enter Employee ID : '))
    qry = 'select * from emp where emp_id=%s;'
    mycur.execute(qry, (ask,))
    d = mycur.fetchall()
    # Using check function to check whether this account exists or not
    id_list = check()
    if ask in id_list:
        while True:
            print("The employee you searched for is :")

            dic = {}
            for i in d:
                dic[i[0]] = i[1:]
            print('_' * 122)
            # fernoume ta stoixeia tou employee me ena format
            print("{:<17} {:<18} {:<18} {:<22} {:<16} {:<17} {:<19}".format(
                'Employee id', 'First Name', 'Last Name', 'Email', 'Phone', 'Address', 'Payment'))
            print('_' * 122)
            for k, v in dic.items():
                a, b, c, d, e, f = v
                print("{:<17} {:<18} {:<18} {:<22} {:<16} {:<17} {:<19}".format(k, a, b, c, d, e, f))
            print('_' * 122)
            space()
            print('What do you want to do:\n'
                  '1)Edit the registry\n'
                  '2)Promote the employee (money raise)\n'
                  '3)Fire the employee\n'
                  '4)To go back')
            ccc = input('enter choice - ')
            # kanoume epeksergasia stoixeiwn
            if ccc == '1':
                qry = 'select emp_id, email, phone, address from emp where emp_id=%s;'
                mycur.execute(qry, (ask,))
                d = mycur.fetchone()
                details = ['Email', 'Phone Number', 'Address']
                dic = {}
                print('The available details to edit are :')
                for i in range(3):
                    dic[details[i]] = d[i + 1]
                    print(i + 1, ')', details[i], ': ', d[i + 1])

                for i in range(len(d)):
                    toupdate = int(input('enter choice to update : '))
                    updating = input('enter the new ' + details[toupdate - 1] + ' : ')
                    # Change the value corresponding to the required field
                    dic[details[toupdate - 1]] = updating
                    conupdt = input(
                        'Do you want to update other details?\n'
                        'Y for yes\n'
                        'N for no\n'
                        'Enter your choice : ')
                    if conupdt in 'Nn':
                        qry = 'update emp set email=%s,phone=%s,address=%s where emp_id=%s;'

                        updated = tuple(dic.values()) + (ask,)
                        val = (updated)
                        mycur.execute(qry, val)
                        mycon.commit()
                        print('Registry has been updated. ')
                        break
                break
            # kanoume proagwgh employee
            if ccc == '2':
                qry = 'select emp_id, payment from emp where emp_id=%s;'
                mycur.execute(qry, (ask,))
                d = mycur.fetchone()
                details = ['Payment']
                dic = {}
                for i in range(1):
                    dic[details[i]] = d[i + 1]
                    print(details[i], ': ', d[i + 1])

                for i in range(len(d)):
                        updating = float(input('Please enter the new payment amount : '))
                        dic[details[i]] = updating

                        qry = 'update emp set payment=%s where emp_id=%s;'

                        updated = tuple(dic.values()) + (ask,)
                        val = (updated)
                        mycur.execute(qry, val)
                        mycon.commit()
                        print('Payment has been updated. ')
                        break
                break
            # kanoume apolush employee
            if ccc == '3':
                delt = input("Do you really want to fire this employee?\n"
                             "Y for yes\n"
                             "N for no\n"
                             "Enter your choice : ")
                if delt in 'Yy':
                    qry = 'delete from emp where emp_id=%s;'
                    mycur.execute(qry, (ask,))
                    mycon.commit()
                    print("Employee was fired from the company.")
                else:
                    print('Delete action was cancelled and you will be moved back to the menu.')
                    break
                break
            # epistrefoume sto prohgoumeno menu
            if ccc == '4':
                break


# mesa sthn employer() exoume ola ta boss actions gia thn database
def employer():
    while True:
        space()
        print('''Welcome to the database:
        1)Add a New Employee
        2)View Employee list registry
        3)Search an Employee
        4)Fire an employee
        5)To go back to the main menu ''')
        ccc = input('Enter __ ')
        if ccc == '1':
            add_emp()
        if ccc == '2':
            view_emp()
        if ccc == '3':
            actions_emp()
        if ccc == '4':
            view_emp()
            space()
            del_emp()
        if ccc == '5':
            break


# trexoume ena sunexomeno loop to programma mas mexri na to termatisei o xrhsths
while True:
    space()
    print('''Welcome to the company's database
    
Please choose what you want to do:												
A)Enter database
B)Exit the program ''')
    actions = input('Enter _ ')
    try:
        if actions in 'Aa':
            employer()
        if actions in 'Bb':
            print("Thank you for using company's database program!")
            break
    except Exception:
        print('The input you gave is not valid so the action was terminated.')
    space()
