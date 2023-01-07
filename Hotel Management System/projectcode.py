from datetime import datetime
from prettytable import from_db_cursor
import time
import mysql.connector as sql
sqlpass='' #Enter MySQL password here
db_name='hotel_system' #Database name

#connect() function will check for database 'hotel_system' and redirect to/run install() function if no 'hotel_system' database found, if found it will redirect to/run login().
def connect():
    print('connecting to mysql...')
    global mycon
    global mycursor
    mycon = sql.connect(host='localhost',user='root',passwd=sqlpass)
    mycursor = mycon.cursor(buffered=True)
    mycursor.execute(f"""show databases like '{db_name}'""")
    data=mycursor.fetchall()
    if data==[]:
        print('database not found')
        instresp=input('Do you want to install neccessary resources?(y/n):')
        if instresp=='y':
            install()
        else:
            print('connection to mysql failed')
            connect()
    elif data!=[]:
        time.sleep(1)
        print('connection to mysql successful')
        print('\n')
        time.sleep(1)
        login()

#install() function will create database 'hotel_system' and all the tables required and redirect to/run creatuser().
def install():
    time.sleep(1)
    print('installing resources...')
    time.sleep(1)
    with open('commands.txt','r') as inserts: #If does'nt work then use absolute path.
        n=inserts.read()
        results=mycursor.execute(n, multi=True)
        for cur in results:
            if cur.with_rows:
                cur.fetchall()
    mycon.commit()
    print('Installation completed.')
    createuser()

#menu() function will display a menu with options and redirect to/run menu_options().
def menu():
    print('\n\n\n\n')
    print(' '*15, 'Hotel Management System', ' '*20)
    print('-'*55)
    print(' '*15, 'M e n u   O p t i o n s', ' '*10)
    print('-'*55)
    print('1. Instert a New Record.')
    print('2. Update an Existing Record.')
    print('3. Remove an Existing Record.')
    print('4. Display All Records.')
    print('5. Search Record by Room.')
    print('6. Search Record by Guest Name.')
    print('7. Search Record by Guest id.')
    print('8. Search Record by Staff Name.')
    print('9. Search Record by staff id.')
    print('10. Search Record by Food Items.')
    print('11. Reset Username or password.')
    print('12. Print Bill')
    print('13. Exit the Program.')
    print('-'*55)
    menu_options()

#Menu_options() will redirect to functions according to menu options.   
def menu_options():
    global uresponse
    uresponse=int(input('Please enter your response:'))
    if uresponse > 13 or uresponse < 1:
        print('Invalid Response, Please try again...')
        time.sleep(1)
        menu()
    else:
        time.sleep(1)
        if uresponse in [1,2,3,4]:
            print('\n')
            print(' '*20, 'Choose Table',' '*20)
            print('-'*55)
            print('1.Staff')
            print('2.Rooms')
            print('3.Login')
            print('4.Guests')
            print('5.Restaurant')
            print('-'*55)
            global table_n
            table_n=int(input('Choose option:'))
            if table_n in [1,2,3,4,5]:
                if uresponse == 1:
                    insert()
                elif uresponse == 2:
                    if table_n in [1,2,4,5]:
                        update()
                    elif table_n==3:
                        time.sleep(1)
                        print('Cannot Update Login Table.')
                        print('Redirecting to Menu...')
                        time.sleep(1)
                        menu()
                elif uresponse==3:
                    if table_n in [1,2,4,5]:
                        delete()
                    elif table_n==3:
                        time.sleep(1)
                        print('Cannot Delete User')
                        print('Redirecting to Menu...')
                        time.sleep(1)
                        menu()
                elif uresponse==4:
                    if table_n in [1,2,4,5]:
                        display()
                    elif table_n==3:
                        time.sleep(1)
                        print('Cannot display usernames and passwords')
                        print('Redirecting to menu')
                        time.sleep(1)
                        menu()
            else:
                print('invalid input')
                time.sleep(1)
                print('redirecting to menu...')
                menu()
        elif uresponse in [5,6,7,8,9,10]:
                if uresponse==5:
                    search_rooms()
                elif uresponse in [6,7]:
                    search_guests()
                elif uresponse in [8,9]:
                    search_staff()
                elif uresponse==10:
                    search_food()
        elif uresponse==11:
            reset()
        elif uresponse==12:
            bill()
        elif uresponse==13:
            print('Thank you for using hotel managemnet system.')
            mycon.close()

#insert() will insert new records in table.
def insert(): 
    avlble=True
    x=None
    if table_n==1:
        r0=input('Please Enter Staff id:')
        r1=input('Please Enter First Name:')
        r2=input('Please Enter Last Name:')
        r3=input('Please Enter a Valid Id Proof:')
        r4=input('Please Enter Department:')
        r5=input('Please Enter Salary:')
        r6=input('Please Enter Designation:')
        r7=input('Please Enter Mobile no.:')
        try:
            x=mycursor.execute(f"""insert into staff values('{r0}','{r1}','{r2}','{r3}','{r4}','{r5}','{r6}','{r7}')""")
        except:
            print('Error Record not added, try again')
            time.sleep(0.5)
            insert()
    elif table_n==2:
        r1=input('Please Enter S.no:')
        r2=input('Please Enter Room type:')
        r3=input('Please Enter Price:')
        r4=input('Please Enter Bed size:')
        r5=input('Please Enter No. of rooms:')
        try:
            x=mycursor.execute(f"""insert into rooms values({r1},'{r2}','{r3}','{r4}',{r5})""")
        except:
            print('Error Record not added, try again')
            time.sleep(0.5)
            insert()
    elif table_n==4:
        r0=input('Please Enter Guest id:')
        r1=input('Please Enter First Name:')
        r2=input('Please Enter Last Name:')
        r3=input('Please Enter Age:')
        r4=input('Please Enter Gender:')
        r5=input('Please Enter a Valid Id Proof:')
        r6=input('Please Enter Room Type:')
        r7=input('Please Enter Check in date,YYYY-MM-DD:')
        r8=input('Please Enter Check Out date,YYYY-MM-DD:')
        try:
            y=mycursor.execute(f"update rooms set avlble = avlble - 1 where room_type='{r6}'")
            mycon.commit()
        except:
            print(f'{r6} rooms not available!!!')
            avlble=False
        if avlble==True:
            try:
                x=mycursor.execute(f"""insert into guests values('{r0}','{r1}','{r2}',{r3},'{r4}','{r5}','{r6}','{r7}','{r8}')""")
            except:
                print('Error Record not added, try again')
                time.sleep(0.5)
                insert()
        elif avlble==False:
            print('Redirecting to menu...')
            time.sleep(0.5)
            menu()
    elif table_n==5:
        r1=input('Please Enter S.no:')
        r2=input('Please Enter Food Item Name:')
        r3=input('Please Enter Price:')
        try:
            x=mycursor.execute(f"""insert into restaurant values({r1},'{r2}',{r3})""")
        except:
            print('Error Record not added, try again')
            time.sleep(0.5)
            insert()
    elif table_n==3:
        r1=input('Please Enter Username:')
        r2=input('Please Enter Password:')
        try:
            x=mycursor.execute(f"""insert into login values('{r1}','{r2}')""")
        except:
            print('Error Record not added, try again')
            time.sleep(0.5)
            insert()
    mycon.commit()
    if x==None and avlble==True:
        print('Record added successfully')
        time.sleep(1)
        print('Redirecting to menu...')
        menu()
        
#update() will update existing records in a table.
def update():
    print('-'*50)
    if table_n==1:
        print('1.Update Firstname')
        print('2.Update Lastname')
        print('3.Update Mobile no.')
        print('4.Redirect to Menu')
        print('-'*50)
        ch=int(input('Choose Option:'))
        global s_id
        s_id=input('Enter Staff id:')
        if ch==1:
            fname=input('Enter Firstname:')
            mycursor.execute(f"""update staff set f_name='{fname}' where staff_id='{s_id}'""")
        elif ch==2:
            lname=input('Enter Lastname:')
            mycursor.execute(f"""update staff set l_name='{lname}' where staff_id='{s_id}'""")
        elif ch==3:
            m_no=input('Enter Mobile no.:')
            mycursor.execute(f"""update staff set mobile_no='{m_no}' where staff_id='{s_id}'""")
        elif ch==4:
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            print('Try Again')
            update()
    elif table_n==2:
        print('1.Update Room Type')
        print('2.Update Bed Size')
        print('3.Redirect to menu')
        print('-'*50)
        ch=int(input('Choose Option:'))
        global s_no
        s_no=int(input('Please Enter S.no:'))
        if ch==1:
            rt=input('Please Enter Room Type:')
            mycursor.execute(f"""update rooms set room_type='{rt}' where s_no={s_no}""")
        elif ch==2:
            bs=input('Please Enter Bed Size:')
            mycursor.execute(f"""update rooms set bed_size='{bs}' where s_no={s_no}""")
        elif ch==3:
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            print('Try Again')
            update()
    elif table_n==4:
        print('1.Update Firstname')
        print('2.Update Lastname')
        print('3.Update Age')
        print('4.Update Gender')
        print('5.Update Room')
        print('6.Update check out date')
        print('7.Redirect to menu')
        print('-'*50)
        ch=int(input('Choose Option:'))
        global g_id
        g_id=input('Pleasee Enter Guest id:')
        if ch==1:
            fng=input('Enter Firstname:')
            mycursor.execute(f"""update guests set f_name='{fng}' where g_id='{g_id}'""")
        elif ch==2:
            lng=input('Enter Lastname:')
            mycursor.execute(f"""update guests set l_name='{lng}' where g_id='{g_id}'""")
        elif ch==3:
            age_g=int(input('Enter Age:'))
            mycursor.execute(f"""update guests set age={age_g} where g_id='{g_id}'""")
        elif ch==4:
            gend=input('Enter Gender:')
            mycursor.execute(f"""update guests set gender='{gend}' where g_id='{g_id}'""")
        elif ch==5:
            uroom=input('Enter Room Type:')
            mycursor.execute(f"""update guests set room='{uroom}' where g_id='{g_id}'""")
        elif ch==6:
            ch_d=input('Enter Check Out Date,YYYY-MM-DD:')
            mycursor.execute(f"""update guests set checkout='{ch_d}' where g_id='{g_id}'""")
        elif ch==7:
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            print('Try Again')
            update()
    elif table_n==5:
        print('1.Update Food Item')
        print('2.Update Price')
        print('3.Redirect to Menu')
        print('_'*50)
        ch=int(input('Choose Option:'))
        global sno
        sno=int(input('Enter S.no:'))
        if ch==1:
            food=input('Enter Food Item:')
            mycursor.execute(f"""update restaurant set itemname='{food}' where sno={sno}""")
        elif ch==2:
            price=input('Enter Price:')
            mycursor.execute(f"""update restaurant set rate='{price}' where sno={sno}""")
        elif ch==3:
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            print('Try Again')
            update()
    mycon.commit()
    check()      

#delete() will delete a record from a table.
def delete():
    if table_n==1:
        global s_id
        s_id=input('Enter Staff id:')
        
        mycursor.execute(f"""delete from staff where staff_id='{s_id}'""")
    elif table_n==2:
        global s_no
        s_no=int(input('Enter S.no:'))
        mycursor.execute(f"""delete from rooms where s_no={s_no}""")
    elif table_n==4:
        global g_id
        g_id=input('Enter Guest id:')
        mycursor.execute(f"""delete from guests where g_id='{g_id}'""")
    elif table_n==5:
        global sno
        sno=int(input('Enter S.no:'))
        mycursor.execute(f"""delete from restaurant where sno={sno}""")
    mycon.commit()
    check()

#display() will display all records from selected table.
def display():
    if table_n==1:
        query="select * from staff"
    elif table_n==2:
        query="select * from rooms"
    elif table_n==4:
        query="select * from guests"
    elif table_n==5:
        query="select * from restaurant"
    mycursor.execute(query)
    count=mycursor.rowcount
    if count>0:
        print('No. of rows in table:', count)
        mycursor.execute(query)
        x=from_db_cursor(mycursor)
        print(x)
        time.sleep(1)
        choice=input('Go to Menu now?(y/n):')
        if choice == 'y':
            menu()
        elif choice == 'n':
            print('Redirecting to Menu in 60 seconds...')
            time.sleep(60)
            menu()
        else:
            print('invalid input')
            time.sleep(1)
            print('Try again')
            time.sleep()
            display()
    else:
        print('Table is empty')
        time.sleep(1)
        print("Redirecting to Menu...")
        time.sleep(1)
        menu()

#search_rooms will search a record by room name.
def search_rooms():
    print('-'*50)
    print('1. Search Record by Room')
    print('2. Redirect to Menu')
    ch=int(input('Choose Option:'))
    if ch==1:
        roomt=input('Enter Room Type:')
        try:
            mycursor.execute(f"""select * from rooms where room_type='{roomt}'""")
            x=from_db_cursor(mycursor)
            print(x)
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        except:
            print('Error Occured')
            time.sleep()
            print('Please try again...')
            search_rooms()
    elif ch==2:
        time.sleep(1)
        print('Redirecting to Menu...')
        time.sleep(1)
        menu()
    else:
        print('invalid input')
        time.sleep()
        search_rooms()

#search_guests() will search a record by guest name or guest id.
def search_guests():
    print('-'*50)
    if uresponse==6:
        print('1. Search Record by Guest Name')
        print('2. Redirect to Menu')
        ch=int(input('Choose Option:'))
        if ch==1:
            gname=input('Enter Guest FirstName:')
            try:
                mycursor.execute(f"""select * from guests where f_name='{gname}'""")
                x=from_db_cursor(mycursor)
                print(x)
                time.sleep(1)
                print('Redirecting to Menu...')
                time.sleep(1)
                menu()
            except:
                print('Error Occured')
                time.sleep()
                print('Please try again...')
                search_guests()
        elif ch==2:
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            time.sleep()
            search_guests()
    if uresponse==7:
        print('1. Search Record by Guest id')
        print('2. Redirect to Menu')
        ch=int(input('Choose Option:'))
        if ch==1:
            g_id=input('Enter Guest id:')
            try:
                mycursor.execute(f"""select * from guests where g_id='{g_id}'""")
                x=from_db_cursor(mycursor)
                print(x)
                time.sleep(1)
                print('Redirecting to Menu...')
                time.sleep(1)
                menu()
            except:
                print('Error Occured')
                time.sleep()
                print('Please try again...')
                search_guests()
        elif ch==2:
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            time.sleep()
            search_guests()

#search_staff() will search record by staff name or id.
def search_staff():
    print('-'*50)
    if uresponse==8:
        print('1. Search Record by Staff Name')
        print('2. Redirect to Menu')
        ch=int(input('Choose Option:'))
        if ch==1:
            sname=input('Enter Staff FirstName:')
            try:
                mycursor.execute(f"""select * from staff where f_name='{sname}'""")
                x=from_db_cursor(mycursor)
                print(x)
                time.sleep(1)
                print('Redirecting to Menu...')
                time.sleep(1)
                menu()
            except:
                print('Error Occured')
                time.sleep()
                print('Please try again...')
                search_staff()
        elif ch==2:
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            time.sleep()
            search_staff()
    if uresponse==9:
        print('1. Search Record by staff id')
        print('2. Redirect to Menu')
        ch=int(input('Choose Option:'))
        if ch==1:
            s_id=input('Enter staff id:')
            try:
                mycursor.execute(f"""select * from staff where staff_id='{s_id}'""")
                x=from_db_cursor(mycursor)
                print(x)
                time.sleep(1)
                print('Redirecting to Menu...')
                time.sleep(1)
                menu()
            except:
                print('Error Occured')
                time.sleep()
                print('Please try again...')
                search_staff()
        elif ch==2:
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            time.sleep()
            search_staff()

#search_food() will search record by fooditem.
def search_food():
    print('-'*50)
    if uresponse==10:
        print('1. Search Record by Food item')
        print('2. Redirect to Menu')
        ch=int(input('Choose Option:'))
        if ch==1:
            food=input('Enter Food item:')
            try:
                mycursor.execute(f"""select * from restaurant where itemname='{food}'""")
                x=from_db_cursor(mycursor)
                print(x)
                time.sleep(1)
                print('Redirecting to Menu...')
                time.sleep(1)
                menu()
            except:
                print('Error Occured')
                time.sleep()
                print('Please try again...')
                search_food()
        elif ch==2:
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else:
            print('invalid input')
            time.sleep()
            search_food()

#reset() will reset username and password.
def reset():
    print('-'*50)
    print('1.Change Username')
    print('2.Change Password')
    print('3.Redirect to menu')
    print('-'*50)
    ch=int(input('Choose Option:'))
    time.sleep(1)
    if ch==3:
        print('Redirecting to menu...')
        time.sleep(1)
        menu()
    elif ch<1 or ch>3:
        print('Invalid input')
        time.sleep(1)
        print('Try again...')
        reset()
    usrname=input('Enter Your Username:')
    passw=input('Enter Your Password:')
    mycursor.execute(f"""select * from login where user_name = '{usrname}' and passw = '{passw}'""")
    info=mycursor.fetchall()
    user_pass=''
    for a, b in info:
        user_pass=a + b
    if usrname and passw in user_pass:
        print('User Found')
        time.sleep(1)
        print('\n')
        if ch==1:
            newusr=input('Please Enter New Username,(Max:20 Characters):')
            if newusr==usrname:
                print('New Username Cannot Be Same as Old Username')
                time.sleep(1)
                print('Try again...')
                time.sleep(1)
                reset()
            try:
                mycursor.execute(f"""update login set user_name='{newusr}'""")
            except:
                print('Error or Username already exists.')
                time.sleep(1)
                print('Please try again...')
                time.sleep(1)
                reset()
        elif ch==2:
            newpass=input('Please Enter New Password,(Max:10 Characters):')
            if newpass==passw:
                print('New Password Cannot Be Same as Old Password')
                time.sleep(1)
                print('Try Again...')
                reset()
            try:
                mycursor.execute(f"""update login set passw='{newpass}'""")
            except:
                print('Error')
                time.sleep(1)
                print('Try again...')
                time.sleep(1)
                reset()
        mycon.commit()
        print('Changes Done!')
        time.sleep(1)
        print('Redirecting to Menu...')
        time.sleep(1)
        menu()

#bill() will search guest record by guest id, calculate total amount with gst and print bill.
def bill():
    print('-'*50)
    try:
        gid=input('Enter Guest id:')
        mycursor.execute(f"""select * from bill where g_id='{gid}'""")
        x=mycursor.rowcount
        if x>0:
            print('Record already exists')
            op=input('Print existing record(y,n)?:')
            if op=='y':
                exrec=from_db_cursor(mycursor)
                print(exrec)
                print('Redirecting to menu...')
                time.sleep(1)
                menu()
            elif op=='n':
                print('Redirecting to menu...')
                time.sleep(1)
                menu()
            else:
                print('Invalid input, Try again...')
                time.sleep(1)
                bill()
        else:
            mycursor.execute(f"""select checkin, checkout, room, f_name, l_name from guests where g_id='{gid}'""")
            x=mycursor.fetchall()
            for a,b,c,d,e in x:
                checkin=a
                checkout=b
                room=c
                fname=d
                lname=e
            checkin1=checkin.strftime("%y-%m-%d")
            checkout1=checkout.strftime("%y-%m-%d")
            days=checkout-checkin
            y=str(days).split()
            nights=int(y[0])
            mycursor.execute(f"""select price from rooms where room_type='{room}'""")
            x=mycursor.fetchall()
            for a1 in x:
                data=a1
            for a2 in data:
                data1=a2
            total=nights*data1
            if total >= 7500:
                calc=total*18
                gst=calc/100
                gtotal=total+gst
            elif total<7500:
                calc=total*12
                gst=calc/100
                gtotal=total+gst
            name=fname+' '+lname
            mycursor.execute(f"""insert into bill values('{gid}','{name}','{room}','{checkin1}','{checkout1}',{nights},{total},{gst},{gtotal})""")
            mycon.commit()
            mycursor.execute(f"""select * from bill where g_id='{gid}'""")
            reciept=from_db_cursor(mycursor)
            print(reciept)
            print('Redirecting to menu...')
            time.sleep(1)
            menu() 
    except:
        print('Error, Please try again')
        time.sleep(1)
        bill()



#createuser() function will be called after database is created if database does'nt exist, this function will accept new username and password and create a new user.
def createuser():
    print('Creating New User...')
    time.sleep(1)
    user=input('Please Enter Your Username:')
    time.sleep(1)
    passw=input('Please Enter Your Password:')
    mycursor.execute(f"""insert into login values('{user}', '{passw}')""")
    mycon.commit()
    print('New User Created Successfully')
    print('\n')
    login()

#login() will accept username & password and check it against records in table login, if correct then it will redirect to menu.  
def login():
    print(' '*18,'Login Page', ' '*20)
    print('-'*50)
    user=input('Please Enter Your Username:')
    time.sleep(1)
    passw=input('Please Enter Your Password:')
    print('-'*50)
    mycursor.execute(f'use {db_name}')
    mycursor.execute(f"""select * from login where user_name = '{user}' and passw = '{passw}'""")
    info=mycursor.fetchall()
    user_pass=''
    for a, b in info:
        user_pass=a + b
    if user and passw in user_pass:
        print('logged in successfully!!')
        time.sleep(1)
        print('\n')
        print('Redirecting to Menu...')
        time.sleep(1)
        menu()
    else:
        time.sleep(1)
        print('Wrong Username or Password')
        res=input('Try again?(y/n):')
        if res=='y':
            login()
        elif res=='n':
            print('Thank you for using hotel management system.')
            mycon.close()
        else:
            print('Invalid input')
            login()

#check() will check if a record exists or not.
def check():
    if table_n==1:
        mycursor.execute(f"""select * from staff where staff_id='{s_id}'""")
    elif table_n==2:
        mycursor.execute(f"""select * from rooms where s_no={s_no}""")
    elif table_n==4:
        mycursor.execute(f"""select * from guests where g_id='{g_id}'""")
    elif table_n==5:
        mycursor.execute(f"""select * from restaurant where sno={sno}""")
    mycon.commit()
    x=mycursor.rowcount
    if uresponse==2:
        if x!=0:
            print('Record updated successfully')
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else: 
            print('Record not found')
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
    elif uresponse==3:
        x=mycursor.fetchall()
        print(x)
        if x==[]:
            print('Record deleted successfully')
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        else: 
            print('Record not found')
            time.sleep(1)
            print('Redirecting to Menu...')
            time.sleep(1)
            menu()
        
if __name__=="__main__":
    connect()
