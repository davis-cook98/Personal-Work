def Fib(x):
    f0 = 0
    f1 = 1
    ans = 0
    while f1 < int(x):
        if f1 % 2 == 0:
            ans += curr
        curr = f1 + f0
        f0 = f1
        f1 = curr

    print(ans)

Fib(4000000)
