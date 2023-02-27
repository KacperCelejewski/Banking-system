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
def majorityCheck():
    utc_time = pendulum.now("UTC")
    wroclawTime= utc_time.in_timezone("Europe/Warsaw")
    TimeDelta = pendulum.duration(days=0,
                                hours=0,
                                years=18)
    dateOfBith = input("Enter date:")
    year, month, day = map(int,dateOfBith.split('-'))
    data = pendulum.datetime(year, month, day)
    if wroclawTime-data<TimeDelta:
        print("You are too young to create an account")
    else:
        print("Age confirmed!")
    return data

    