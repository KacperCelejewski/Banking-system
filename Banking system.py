#register
#staring speech and choosing opportunity from the menu

print('''Hello, dear client!
\t if you are new just join us and sign in!(Enter: 'sign in')''')

while True:
    signing_command = input("---> ")
     
    if signing_command=="sign in" or signing_command == "signin" or signing_command=="Sign in":
        print("Great,we enjoy that you stay with us! \nLets start!")
        break
    elif signing_command!="sign in" or signing_command != "signin" or signing_command!="Sign in":
        print("Try again!")
        continue

from modules import majorityCheck
majorityCheck()


from modules import IdCheck
IdCheck()

person={}
surrname=input("Enter yout surrname: ")
name=input("Enter yout name: ")
person[name]=surrname
person["date of birth"]= majorityCheck()
person["ID"]=IdCheck
print(person)












