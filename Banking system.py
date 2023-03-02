#register
#staring speech and choosing opportunity from the menu

menu={1:"sign in", 2:"log in", 3:"Start Menu"}
print("Menu")
for x in menu:
    print (x,":",menu[x])
menuChoice=int(input("What you wanna do?"))
from modules import majorityCheck
from modules import IdCheck
from modules import passWord as password
from modules import passCheck
if menuChoice==1:
        major=majorityCheck()
        ID=IdCheck()
        word=password()
elif menuChoice==2:
     Password=passCheck(person)
elif menuChoice==3:
     pass




















person={}
surrname=input("Enter yout surrname: ")
name=input("Enter yout name: ")
person[name]=surrname
person["date of birth"]= major.format('dddd Do of MMMM YYYY')
y = str()
for x in ID:
    y=y+x
person["ID"]=y
passWord={"password":word}
person.update(passWord)
print(person)












