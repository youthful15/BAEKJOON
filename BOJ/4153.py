while True:

    a, b, c = map(int,input().split())
    max_abc = max([a, b, c]) ** 2

    if a == 0 and b == 0 and c == 0:
        break
    elif max_abc == a ** 2 + b ** 2 or max_abc == b ** 2 + c ** 2 or max_abc == a ** 2 + c ** 2:
        print("right")
    else:
        print("wrong")