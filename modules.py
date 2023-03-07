import pendulum
import ast

def IdCheck():
    while True:
        file = open("id.txt", "a")
        file.write(input("Enter your ID: ") + "\n")
        file.close()
        file = open("ID.txt", "r")
        if file.readable() == True:
            lines = file.readlines()
            new_lines=[]
            for str in  lines:
                new_lines.append(str.strip())
        else:
            return 
        
        length = len(new_lines[-1])
        if length < 3 or length > 4:
            print("ID consists of maximum 4 numbers and minimum 3, try again")
            file.close()
            file=open("ID.txt","w")
            for line in lines:
                if line!=lines[-1]:
                    file.write(line)
            continue
        elif new_lines[-1][0:2:] != "11":
            print("iD has to below 11 on the beginning!")
            file.close()
            file=open("ID.txt","w")
            for line in lines:
                if line!=lines[-1]:
                    file.write(line)
            continue
        else:
            break
    return new_lines

class ToOldToLive(Exception):
    pass


def majorityCheck():
    while True:
        utc_time = pendulum.now("UTC")
        wroclawTime = utc_time.in_timezone("Europe/Warsaw")

        TimeDelta = pendulum.duration(days=0,
                                      hours=0,
                                      years=18)
        TimeDelta100 = pendulum.duration(days=0,
                                         hours=0,
                                         years=120)

        dateOfBith = input("Enter date:")
        try:
            year, month, day = map(int, dateOfBith.split('-'))
            data = pendulum.datetime(year, month, day)
        except ValueError:
            print("Enter correct data format")
            continue
        try:
            if data > wroclawTime:
                raise ValueError("Date has to be in the past")
            if data < wroclawTime.subtract(100):
                raise ToOldToLive(
                    "It is not possible that you still exist! XD")
        except ValueError as valueerror:
            print(valueerror)
            continue
        except ToOldToLive as TooOld:
            print(TooOld)
            continue
        else:
            break

    return data


# create passwords and saves them in file, that will be used to login function
def passWord_reg():
    file_reg = open("RegPass.txt", "a")
    password = input("Enter your new password: ")
    #condition that check if password is empty
    while password == "":
        if password == "":
                print( "password has to contain letters!")
                password= input("Enter your new password: ")
    confirm = input("Confirm your new password: ")

    #confirmed password has to be the same password
    while password != confirm:
        num = int(input("Confimation failed(incorrect password) If you wwant to change your password, enter 1: or try again and enter 2: "))
        if num == 1:
            password = input("Enter your new password: ")
            confirm = input("Confirm your new password: ")
            continue
        elif num == 2:
            confirm = input("Confirm your new password: ")
            continue
    #storing confirmed password in file line by line      
    confirm += "\n"
    file_reg.write(confirm)
    file_reg.close()
    return password
#checks validation of inputed ID and password 
def login():
    ID=input("Enter your ID: ")
    password = input("Enter your password: ")
    #extra codnition on entry level, searches files to find out, if any password exist
    fileID = open("ID.txt","r")
    if fileID.readable()==True:
        text=fileID.readlines()
        for file_lines in text:
            if file_lines.strip() == ID:
                break
    with open("RegPass.txt", "r") as filePass:
        file_passes = filePass.readlines()
        while True:
            if len(file_passes) == 0:
                print("You are not registered.")
                return passWord_reg()
                # Menu
                """Place to write some code about getting back"""
            filePass.close()
            # return password and ID, to verify if they have correct matching
            return [password, ID]
        


def id_pass_connection(ID,password):
    users_data={ID:password}
    f=open("id_match.txt","a")
    f.write(str(users_data))
    f.write("\n")

def id_pass_connection_check(ID,password,users_data):
    if type(users_data) != dict:
        print("dic")
        exit()
        return 
    while users_data[password]!=ID:
        print(f"ID {ID} doesnt match to your password!")
        choice =input("""1 --> Change ID
                         2 --> Change Password""")
        if choice =="1": login()

        elif choice == "2":
            from Id import IDe
            IDe()
    return True




def profiles(ID, word):
    person={}
    surrname=input("Enter yout surrname: ")
    name=input("Enter yout name: ")
    person[name]=surrname
    #person["date of birth"]= major.format('dddd Do of MMMM YYYY')
    y=str()
    for x in ID:
        y=x
    person["ID"]=y
    passWord={"password":word}
    person.update(passWord)
    print(person)

def id_pass_check(users_input):
    f=open("id_match.txt","r")
    lines=f.readlines()
    match={users_input[1]:users_input[0]}
    for i in range(len(lines)):
        input_from_register=ast.literal_eval(lines[i].strip("\n"))
        if input_from_register == match:
            print("You are logged in!")
            return True
    else:
        print("You  cant log in")
        return False




