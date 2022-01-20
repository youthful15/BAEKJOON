h,m=map(int,input().split())
if h==0 and m<45 :
    print("23",15+m)
elif m<45 :
    print(h-1,15+m)
else :
    print(h,m-45)