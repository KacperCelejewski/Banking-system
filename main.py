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
    
    f=open("id_match.txt","r")
    lines=f.readlines()
    match={users_input[-1]:users_input[0]}
    for i in range(len(lines)):
        lines_stripped= lines[i].strip("\n")
        input_from_register = ast.literal_eval(lines_stripped)
        if input_from_register == match:
            print("You are logged in!")
            break
    else:
        print("You  cant log in")
    

          
    check=check(users_input[0],users_input[1],match)

elif menuChoice == 3:
    pass


































