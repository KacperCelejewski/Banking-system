def passCheck(password):
    file= open("pass.txt","a")
    file.write(input("Enter your password: ") + "\n")
    file.close()
    file = open("pass.txt","r")
    if file.readable()==True:
        text=file.readlines()
        for x in text:
            oppo=[]
            oppo.append(x)
            x = x.strip()
            if x == password:
                print("Great")
                break
            file.close()
    return x == password