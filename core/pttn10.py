
for i in range(1,6):
    for j in range(1,i+1):
        if i==1 or i==j or j==1  or i==5:
            print("♥",end=" ")
        else:
            print(end="  ")
    print("\r")
for i in range(1,5):
    for j in range(1,6):
        if   i==4 or j==1 or j==5:
            print("♥",end=" ")
        else:
            print(end="  ")
    print("\r")
