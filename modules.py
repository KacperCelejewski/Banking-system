def IdCheck():
    while True:
        ID=list(input("Enter your ID:"))
        length=len(ID)
        if length < 3 or length > 4:
            print("ID consists of maximum 4 numbers and minimum 3, try again")
            continue
        elif ID[0:2:] != ["1","1"]:
            print("iD has to below 11 on the beginning!")
            continue
        else:
            print("You are approved!")
            break
    return ID

import pendulum

class ToOldToLive(Exception):
    pass


def majorityCheck():
    while True:
        utc_time = pendulum.now("UTC")
        wroclawTime= utc_time.in_timezone("Europe/Warsaw")
        
        TimeDelta = pendulum.duration(days=0,
                                    hours=0,
                                    years=18)
        TimeDelta100 = pendulum.duration(days=0,
                                    hours=0,
                                    years=120)
        
        
        dateOfBith = input("Enter date:")
        try:
            year, month, day = map(int,dateOfBith.split('-'))
            data = pendulum.datetime(year, month, day)
        except ValueError:
            print("Enter correct data format")
            continue
        try:
            if data>wroclawTime:
                raise ValueError("Date has to be in the past") 
            if data<wroclawTime.subtract(100):
                raise ToOldToLive("It is not possible that you still exist! XD") 
        except ValueError as valueerror:
            print(valueerror)
            continue
        except ToOldToLive as TooOld:
            print(TooOld)
            continue
        else:
            break

    return data





#create password
def passWord():
    password=input("Enter your new password: ")
    confirm=input("Confirm your new password: ")

    while password !=confirm:
        num=int(input("Confimation failed(incorrect password) If you wwant to change your password, enter 1: or try again and enter 2: "))
        if num==1:
            password=input("Enter your new password: ")
            confirm=input("Confirm your new password: ")
            continue
        elif num==2:
            confirm=input("Confirm your new password: ")   
            continue 

    return password
plot=passWord()



def passCheck(person_dic):
    password=input("Enter your password: ")
    if password==person_dic.get("password"):
        print("Password is correct!")




    





