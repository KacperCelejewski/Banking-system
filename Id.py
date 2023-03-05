def IDe():
    ID=input("Enter your ID: ")
    fileID = open("ID.txt","r")
    if fileID.readable()==True:
        text=fileID.readlines()
        for x in text:
                oppo=[]
                oppo.append(x)
                x = x.strip()
                if x == ID:
                    break
                fileID.close()
    
   
