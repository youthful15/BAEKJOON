a=int(input())
b=100-a
for i in range(1,a+1,1) :
    for k in range(b,100-a-a+1,-1) :
        print(" ",end='')
    for j in range(1,i+1,1) :
        print("*",end='')
    print("")
    b=b-1