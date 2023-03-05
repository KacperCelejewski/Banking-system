#register
#staring speech and choosing opportunity from the menu

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
    login=login()
    print(login[-1])
    f=open("id_match.txt","r")
    k=f.readlines()
    
    match={login[-1]:login[0]}
    for i in k:
          if i == match:
                print("You are logged in!")

          
    check=check(login[0],login[1],match)

elif menuChoice == 3:
    pass


































