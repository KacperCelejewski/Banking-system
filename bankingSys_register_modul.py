#register



#current date in int type
import datetime
today_d=datetime.date.today()    
day_cur = int(today_d.strftime("%d"))
month_cur = int(today_d.strftime("%m"))
year_cur = int(today_d.strftime("%Y"))





class users_personality:
    def __init__(self,name, surrname, ID_number, place_of_birth, email,phone_number,birth_date):
        self.name=name
        self.surrname=surrname
        self.ID_number=ID_number
        self.place_of_birth=place_of_birth
        self.phone_number=phone_number
        self.birth_date=birth_date


#staring speech and choosing opportunity from the menu

print('''Hello, dear client!
\t if you are new just join us and sign in!(Enter: 'sign in')''')
while 1<2:
    signing_command = input("---> ")
    if signing_command=="sign in" or signing_command == "signin" or signing_command=="Sign in":
        print("Great,we enjoy that you stay with us! \nLets start!")
        date_entry = input('Enter a date in YYYY-MM-DD format: ')
        break
    elif signing_command!="sign in" or signing_command != "signin" or signing_command!="Sign in":
        print("Try again!")
        continue

 #splitting data and mapping individual parts of data into intposzczegolne
year, month, day = map(int,date_entry.split('-'))
'''majority condition that check every value of splitted YYYY-MM-DD format(which number is bigger or smaller example 2003 is smaller than current year(2023) so automatically user goes to the next step;
when the earlier conditional was false and the user's birthday is in a month that will be etc, the user isn't able to get an account...'''
if year_cur-year>18:
    print("Congratulations, you are approved!")
elif year_cur-year==18:
        if month<month_cur:
            print("Congratulations, you are approved!")
        else:
            print("U are not able to create an account")
            quit()
elif month==month_cur:
    if day<=day_cur:
        print("Congratulations, you are approved!")
    else:
        print("You are not able to create an account")
        quit()
else:
    print("You are not able to create an account")
    quit()


#getting id's and limiting thet (1<ID<4)
ID= input("Enter your ID: ")
while len(ID)<=1:  
    print("ID is too short (min. 2 numbers), try again")
    ID= input("Enter your ID: ")
    continue
def ID_check_1(ID):
    if ID[0] == "1" and ID[1] == "1" :
        print("Your ID starts with double 1, its looks good!",1)
    while ID[1]!="1" or ID[0]!="1":
        while len(ID)<=1:  
                print("ID is too short, try again")
                ID= input("Enter your ID: ")
                continue
        if ID[0] != "1" or ID[1] != "1" :
            print("Your ID doesnt match!")
            ID= input("Enter your ID: ")
            while len(ID)<=1:  
                print("ID is too short, try again")
                ID= input("Enter your ID: ")
                continue
            continue
        if ID[0] == "1" and ID[1]== "1" :
            while len(ID)<=1:  
                print("ID is too short, try again")
                ID= input("Enter your ID: ")
                continue
            print("Your ID starts with double 1, its looks good!") 
    return (ID[1]=="1"and ID[1]=="1")

i=ID_check_1(ID)

while i==True:
    if len(ID)>4 :
        print("ID consists of maximum  4 numbers, try again ")
        ID= input("Enter your ID: ")
        while len(ID)<=1:  
            print("ID is too short, try again")
            ID= input("Enter your ID: ")
            continue
        continue
    elif len(ID)==0:
        ID= input("Enter your ID: ")
    else:
        print("Good job")
        break

person={}
surrname=input("Enter yout surrname: ")
name=input("Enter yout name: ")
person[name]=surrname
person["date of birth"]= date_entry
person["ID"]=ID
print(person)












