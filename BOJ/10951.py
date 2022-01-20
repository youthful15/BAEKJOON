a=1
b=1
while a != 0 :
    try:
        a,b=map(int,input().split())
        print(a+b)
    except EOFError :
        break