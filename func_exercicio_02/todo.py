def head(L):
    return L[0]
 
def tail(L):
    return L[1]

def py2ll(L):
    if not L:
        return None
    else:
        return (L[0], py2ll(L[1:]))

def ll2py(L):
    if not L:
        return []
    else:
        return [head(L)] + ll2py(tail(L))

def fact(N):
    if N > 1:
        return N * fact(N-1)
    else:
        return 1

def prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def mapL(L, f):
    if not L:
        return None
    else:
        return (f(head(L)), mapL(tail(L), f))

def factAll(L):
    # retorna uma nova lista com o fatorial de cada número em L
    if not L:
        return None
    else:
        return (fact(head(L)), factAll(tail(L)))

def strAll(L):
    # retorna uma nova lista com cada elemento de L convertido para uma string
    if not L:
        return None
    else:
        return (str(head(L)), strAll(tail(L)))

def incAll(L):
    # retorna uma nova lista com cada elemento de L incrementado de 1
    if not L:
        return None
    else:
        return (head(L) + 1, incAll(tail(L)))

def sqrAll(L):
    # retorna uma nova lista com cada elemento de L elevado ao quadrado
    if not L:
        return None
    else:
        return (head(L) ** 2, sqrAll(tail(L)))

def isPrimeAll(L):
    # retorna uma nova lista (de booleanos), em que a posição n é verdade se o elemento n de L for primo.
    if not L:
        return None
    else:
        return (prime(head(L)), isPrimeAll(tail(L)))

def incAllN(L, N):
    # retorna uma nova lista com cada elemento de L incrementado de N
    if not L:
        return None
    else:
        return (head(L) + N, incAllN(tail(L), N))

def filterL(L, f):
    if not L:
        return None
    else:
        T = filterL(tail(L), f)
        H = head(L)
        return (H, T) if f(H) else T

def filterOdd(L):
    # retorna uma nova lista somente com os números de L que são ímpares.
    return filterL(L, lambda x: x % 2 != 0)

def filterPositive(L):
    # retorna uma nova lista somente com os números de L que são maiores que zero.
    return filterL(L, lambda x: x > 0)

def filterGtN(L, N):
    # retorna uma nova lista somente com os números de L que são maiores que N.
    return filterL(L, lambda x: x > N)

def filterPrimes(L):
    # torna uma nova lista somente com os números primos que estão em L.
    return filterL(L, prime)