
def d2Valid(a, b, c):
    Ai = 0
    Bi = 0
    cTest = []
    while (Ai < len(a) or Bi < len(b)):
        if (a[Ai] == b[Bi]):
            cTest.append(a[Ai])
            Ai += 1
            Bi += 1
        if (a[Ai] > b[Bi]):
            cTest.append(a[Ai])
            a[Ai] -= b[Bi]
            Bi += 1
        if (b[Bi] > a[Ai]):
            cTest.append(b[Bi])
            b[Bi] -= a[Ai]
            Ai += 1
    cTest.sort()
    c.sort()
    print(c == cTest)


aIn = [2, 2, 4, 1, 4, 2, 4]
bIn = [6, 3, 1, 2, 1, 2, 4]
cIn = [2, 2, 2, 2, 1, 1, 2, 1, 2, 4]

aIn2 = [9, 2, 3, 6, 4, 2, 8, 9, 2, 5, 5, 8, 6, 9, 6, 5, 4, 9, 4, 2]
bIn2 = [8, 5, 7, 7, 6, 7, 9, 6, 7, 9, 5, 6, 7, 5, 5, 9]
cIn2 = [8, 1, 2, 2, 1, 6, 4, 2, 1, 6, 1, 6, 3, 2, 4, 1, 5, 7, 1, 6, 2, 5, 2, 4, 2, 5, 4, 1, 5, 3, 2, 4]

d2Valid(aIn, bIn, cIn)
