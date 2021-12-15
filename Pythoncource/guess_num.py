secret_num = 9
attachment = 0
while attachment<3:
    quest=input("Guess Number: ")
    attachment+=1
    if int(quest)==9:
        print ("You win!")
        break
    elif attachment==3:
        print("Fail!!, out of chance.....")
