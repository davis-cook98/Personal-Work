def multiples(x):
    ans = 0
    for i in range(1,int(x)):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    print(ans)

multiples(1000)
