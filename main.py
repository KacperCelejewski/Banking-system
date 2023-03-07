#register
#staring speech and choosing opportunity from the menu
import ast
menu={1:"sign in", 2:"log in", 3:"Start Menu"}
print("Menu")
for x in menu:
    print (x,":",menu[x])
menuChoice=int(input("What you wanna do? -> "))
if menuChoice == 1:
            from modules import majorityCheck
            from modules import IdCheck 
            from modules import passWord_reg
            from modules import id_pass_connection as connection
            from modules import profiles
            
            major=majorityCheck()
            ID=IdCheck()
            print(ID)
            word=passWord_reg()
            connection=connection(str(ID[-1]),word)
            profiles=profiles(ID, word)
elif menuChoice == 2:
    from modules import login
    from modules import id_pass_connection as connection
    from modules import id_pass_connection_check as check
    users_input=login()
    #Stored ID and passwoord as lsit
    
    from modules import id_pass_check
    users_validation=id_pass_check(users_input)
    def again():
        next_step=input("If you want to try again enter 'yes', to sign in enter 'sign in'")
        if users_validation==False and next_step=="yes":
          return id_pass_check()
        elif next_step=="sign in":
             return  majorityCheck(),IdCheck(),passWord_reg(),connection(str(ID[-1]),word),profiles(ID, word)

elif menuChoice == 3:
    pass


































