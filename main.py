#register
#staring speech and choosing opportunity from the menu
import ast
while True:
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
        from modules import again
        users_validation=id_pass_check(users_input)
        
        
    elif menuChoice == 3:
        continue



































