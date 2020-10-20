import random
import math

def isPrime(n) : 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
  
    return True

def extendedEuclideanAlgorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extendedEuclideanAlgorithm(b % a, a)
        return g, x - (b // a) * y, y
        
def modinv(a, m):
    g, x, y = extendedEuclideanAlgorithm(a, m)
    if (g != 1):
        raise Exception('модульная инверсия не существует')
    else:
        return x % m     

def encrypt(message, e, n):
    encrypt = []
    for i in message:
        encrypt.append((ord(i) ** e) % n)

    return encrypt

def decrypt(messageEncrypt, d, n):
    decrypt = []
    for i in range(len(messageEncrypt)):
        decrypt.append(chr((messageEncrypt[i] ** d) % n))

    return ''.join(map(str, decrypt))

if __name__ == "__main__":
    p = 31
    while (isPrime(p) != True):
        p += 1

    q = 37
    while (isPrime(q) != True):
        q += 1

    n = p * q
    theFunctionOfEuler = (p-1) * (q-1)

    e = random.randint(1, n)
    while (math.gcd(theFunctionOfEuler, e) != 1):
        e += 1

    d = modinv(e, theFunctionOfEuler)

    print("---------------------------")
    print("p: " + str(p))
    print("q: " + str(q))
    # print("n: " + str(n))
    # print("theFunctionOfEuler: " + str(theFunctionOfEuler))
    print("---------------------------")

    print("Публичный ключ: (" + str(e) + "," + str(n) + ")")
    print("Приватный ключ: (" + str(d) + "," + str(n) + ")")

    print("---------------------------")

    message = "hello world"
    print("Исходный текст: " + message)

    messageEncrypt = encrypt(message, e, n)
    print("Зашифрованный текст: " + str(messageEncrypt))

    messageDecrypt = decrypt(messageEncrypt, d, n)
    print("Расшифрованный текст: " + messageDecrypt)

    print("---------------------------")