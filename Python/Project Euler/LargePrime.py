def largePrime(x):
    half = int(x / 2)
    while half > 0:
        if isPrime(half) and x % half == 0:
            print(half)
            break
        print(half) 
        half -= 1


def isPrime(x):
    half = x / 2
    i = 2
    while i < half:
        if x % i == 0:
            return(False)
        else:
            return(True)

# print(isPrime(13))
largePrime(600851475143)
