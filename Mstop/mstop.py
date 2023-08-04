from termcolor import colored, cprint
import os
import time
import random
import pwinput
import webbrowser
from prettytable import from_db_cursor
import mysql.connector as sql
import logo
from datetime import datetime, date

My_Sql_Password=''
database = 'mstop'
ctime = datetime.now()
print("\n")
print(colored(f'[+]{ctime}','light_cyan'))
cmpl = ['Great!','Good job','Attaboy!!','Noice','Keep it up',"let's go!"]
un_cmpl = ["We expected more!","You let us down","should'nt have done it","just why?"]

def motivation():
	print("\n")
	print(colored('[+]Opening browser...','green'))
	time.sleep(0.5)
	webbrowser.open("https://www.youtube.com/shorts/lWS1vQKJER4")
	temp=input(colored("[+]Press Enter to continue...",'green'))
	webbrowser.open("https://www.youtube.com/shorts/p_4Jyw04mis")
	temp=input(colored("[+]Press Enter to continue...",'green'))
	webbrowser.open("https://www.youtube.com/shorts/tuKsZCJHWC0")
	return 0

def facts():
	print("\n")
	print("-"*56)
	with open('facts.txt','r') as fact_file:
		data = fact_file.read()
		print(data)
	fact_file.close()
	print("\n")
	print("This tool was developed by TPsAREENx.",colored("https://github.com/TPsAREENx/Python-Projects/",'blue',attrs=['underline']),"<=[ctrl + click]")
	temp=input(colored("[+]Press Enter to continue...",'green'))
	return 0	

def display_all():
	print("\n")
	try:
		mycursor.execute(f"""select * from record""")
		data = from_db_cursor(mycursor)
		print(data)
		mycursor.execute("select count(record) from record where record = 'Y'")
		Y = mycursor.fetchall()
		mycursor.execute("select count(record) from record where record = 'N'")
		N = mycursor.fetchall()
		print(f"Y:{Y}, N:{N}")
		temp=input(colored("[+]Press Enter to continue...",'green'))
		return 0
	except:
		print(colored('[-]Error occured','red'))
		time.sleep(0.5)
		return 0

def search():
	print("\n")
	date=input(colored("Enter date(YYYY-MM-DD):",'light_cyan'))
	try:
		mycursor.execute(f"""select * from record where timestamp = '{date}'""")
	except sql.errors.DatabaseError as e:
		print(colored("[-]Invalid date input",'red'))
		search()
	check=mycursor.fetchall()
	if check==[]:
		print(colored("[-]No record found",'red'))
		time.sleep(0.5)
		return 0
	elif check!=[]:
		mycursor.execute(f"""select * from record where timestamp = '{date}'""")
		data = from_db_cursor(mycursor)
		print(data)
		time.sleep(0.5)
		temp=input(colored('[+]Press Enter to continue...','green'))
		return 0

def edit_rec():
	print("\n")
	date=input(colored("Enter date(YYYY-MM-DD):",'light_cyan'))
	try:
		mycursor.execute(f"""select * from record where timestamp = '{date}'""")
	except sql.errors.DatabaseError as e:
		print(colored("[-]Invalid date input",'red'))
		edit_rec()
	check=mycursor.fetchall()
	if check==[]:
		print(colored("[-]No record found",'red'))
		time.sleep(0.5)
		return 0
	elif check!=[]:
		mycursor.execute(f"""select * from record where timestamp = '{date}'""")
		data = from_db_cursor(mycursor)
		print(data)
		rec=input(colored("Enter new status(Y=won/N=lost):",'light_cyan'))
		mycursor.execute(f"""update record set record='{rec}' where timestamp='{date}'""")
		mycon.commit()
		print(colored('[+]Record updated successfuly!','green'))
		temp=input(colored('[+]Press Enter to continue...','green'))
		return 0

def adrec2():
	print("\n")
	date = input(colored("Enter date(YYYY-MM-DD):",'light_cyan'))
	rec = input(colored("Enter status(Y=won/N=lost):",'light_cyan'))
	if rec.lower() not in ['y','n']:
		print(colored("[-]Wrong input",'red'))
		time.sleep(0.5)
		adrec2()
	elif rec.lower() == 'y':
		print(colored(f'[+]{cmpl[random.randint(0,5)]}','green'))
		time.sleep(0.5)
	elif rec.lower() == 'n':
		import unsigma
		time.sleep(0.5)
		print(colored(f'[-]{un_cmpl[random.randint(0,3)]}','red'))
		time.sleep(0.5)
	try:
		mycursor.execute(f"""insert into record values('{date}','{rec}')""")
		mycon.commit()
		print(colored("Record successfuly added", 'green'))
		time.sleep(0.5)
		temp=input(colored('[+]Press Enter to continue...','green'))
		return 0
        
	except:
		print(colored(f"[-]Record already added on {date} or maybe another Error", 'red'))
		time.sleep(0.5)
		temp=input(colored('[+]Press Enter to continue...','green'))
		return 0

def adrec():
	print("\n")
	date1 = date.today()
	print(colored(date1,'light_cyan'))
	rec = input(colored("Enter status(Y=won/N=lost):",'light_cyan'))
	if rec.lower() not in ['y','n']:
		print(colored("[-]Wrong input",'red'))
		time.sleep(0.5)
		adrec()
	elif rec.lower() == 'y':
		print(colored(f'[+]{cmpl[random.randint(0,5)]}','green'))
		time.sleep(0.5)
	elif rec.lower() == 'n':
		import unsigma
		time.sleep(0.5)
		print(colored(f'[-]{un_cmpl[random.randint(0,3)]}','red'))
		time.sleep(0.5)
	try:
		mycursor.execute(f"""insert into record values('{date1}','{rec}')""")
		mycon.commit()
		print(colored("Record successfuly added", 'green'))
		time.sleep(0.5)
		temp = input(colored('[+]Press Enter to continue...','green'))
		return 0

	except:
		print(colored(f"[-]Record already added on {date1}", 'red'))
		time.sleep(0.5)
		temp=input(colored('[+]Press Enter to continue...','green'))
		return 0

def menu():
	print("\n")
	print(colored("********** MENU **********",'blue'))
	print(colored("1. Add record\n2. Add record with custom timestamp\n3. Edit a record\n4. Search a record\n5. Display all records\n6. Motivation\n7. Facts\n8. Exit",'light_cyan'))
	try:
		ch = int(input(colored("[+]Enter option:",'green')))
	except:
		print(colored('[-]Wrong input','red'))
		time.sleep(0.5)
		menu()
	if ch not in [1,2,3,4,5,6,7,8]:
		print(colored('[-]Wrong input','red'))
		time.sleep(0.5)
		menu()
	elif ch == 1:
		temp=adrec()
	elif ch==2:
		temp=adrec2()
	elif ch==3:
		temp=edit_rec()
	elif ch == 4:
		temp=search()
	elif ch == 5:
		temp=display_all()
	elif ch == 6:
		temp=motivation()
	elif ch == 7:
		temp=facts()
	elif ch == 8:
		print('Bye\n')
		print("Clearing output in 5......", end="\r")
		time.sleep(1)
		print("Clearing output in 4.....", end="\r")
		time.sleep(1)
		print("Clearing output in 3....", end="\r")
		time.sleep(1)
		print("Clearing output in 2...", end="\r")
		time.sleep(1)
		print("Clearing output in 1..", end="\r")
		time.sleep(1)
		os.system('clear')
		time.sleep(1)
		mycon.close()
		time.sleep(0.5)
		os._exit(1)
	menu()

def s_check():
	mycursor.execute(f"""select record from record""")
	data = mycursor.fetchall()
	count=0
	y=0
	n=0
	for x in data:
		for i in x:
			if str(i) == 'Y':
				y+=1
				count+=1
			elif str(i) == 'N':
				n+=1
				count=0
	print(colored('[+]Checking for streak...','green'))
	time.sleep(0.5)
	if count!=0:
		if count%10==0:
			print(colored(f"[+]{count} day streak",'green',attrs=['blink']))
			import sigma
		elif count<10:
			print(colored(f"[+]{count} day streak",'green',attrs=['blink']))
			print('Complete 10 days streak for surprise')
		elif count%10!=0:
			print(colored(f"[+]{count} day streak",'green',attrs=['blink']))
	elif count==0:
		print(colored(f"[-]Build up your streak",'red',attrs=['blink']))
	menu()

def login(check):
	if check == 1:
		print("\n")
		print(colored("********** NEW LOGIN **********",'blue'))
		user = input(colored("Set a UserName(Max. 20):","light_cyan"))
		passw = pwinput.pwinput(colored("Set a PassWord(Max. 20):","light_cyan"))
		if user!='' and passw!='':
			mycursor.execute(f"""insert into login values('{user}', '{passw}')""")
			mycon.commit()
			login(0)
		else:
			print(colored("[-]UserName or Password cannot be NULL","red"))
			time.sleep(0.5)
			login(1)
	elif check==0:
		print("\n")
		print(colored("********** LOGIN **********",'blue'))
		user = input(colored("Enter UserName:",'light_cyan'))
		passw = pwinput.pwinput(colored("Enter PassWord:",'light_cyan'))
		mycursor.execute(f'use {database}')
		mycursor.execute(f"""select * from login where user_name = '{user}' and passw = '{passw}'""")
		info = mycursor.fetchall()
		user_pass=''
		for a, b in info:
			user_pass=a + b
		if user and passw in user_pass:
			print(colored('[+]Logged in','green'))
			time.sleep(0.5)
			s_check()
		else:
			print(colored("[-]Wrong Username or Password",'red','on_white'))
			time.sleep(0.5)
			ch = input(colored("[+]Try again?(y/n):",'cyan'))
			if ch.lower()=='y':
				login(0)
			else:
				mycon.close()
				exit()

def install():
	time.sleep(0.5)
	print(colored("[+]Creating database...",'green'))
	mycursor.execute(f"""CREATE DATABASE {database}""")
	mycursor.execute(f"use {database}")
	mycursor.execute("""create table login(user_name varchar(20) primary key, passw varchar(20) NOT NULL)""")
	mycursor.execute("""create table record(timestamp date primary key, record varchar(10) NOT NULL)""")
	mycon.commit()
	login(1)

def connect():
	print(colored("[+]Connecting to database...", 'green'))
	global mycon
	global mycursor
	try:
		mycon = sql.connect(host='localhost',user='root',passwd=My_Sql_Password)
	except:
		print(colored("[-]Failed to connect to MySQL", 'red'))
		exit()
	mycursor = mycon.cursor(buffered=True)
	mycursor.execute(f"""show databases like '{database}'""")
	data = mycursor.fetchall()
	if data==[]:
		print(colored("[-]Database not found",'red'))
		install()
	if data!=[]:
		print(colored("[+]Succesfully connected to database",'green'))
		print("\n")
		time.sleep(0.5)
		login(0)

connect()
