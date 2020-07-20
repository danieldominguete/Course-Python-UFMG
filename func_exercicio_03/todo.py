from functools import reduce

def firstChars(L):
    """ Maps strings in L to a list with the first character of each string.
    For instance:
    firstChars(['python', 'is', 'pythy']) == ['p', 'i', 'p']
    """
    if not L:
        return None
    else:
        return list(map(lambda x: x[0], L))

def sum(L):
    """ Sums the elements in L """
    if not L:
        return 0
    else:
        return reduce(lambda acc, b: acc + b, L, 0)

def avg(L):
    """ Returns the average of the elements in L """
    if not L:
        return 0
    else:
        return reduce(lambda acc, b: acc + b, L) / len(L)

def maxString(L):
    """ Retorna a maior string dentre as strings em L.
    Por exemplo: maxString(['python', 'is', 'pythy']) == 'python'
    Se houver empate, retorna a primeira string encontrada.
    """
    if not L:
        return None
    else:
        return list(filter(lambda word: len(word) == max(map(len, L)), L))[0]

def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    ins(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    if not L:
        return None
    else:
        D = {}
        return list(map(lambda x: add2Dict(D, len(x), x), L))[0]

def incValue(D, N):
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao
    Voce pode usar essa funcao para completar countFirsts
    """
    D[N] = D[N] + 1 if N in D else 1
    return D

def countFirsts(L):
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """
    if not L:
        return None
    else:
        D = {}
        return list(map(lambda x: incValue(D, x[0]), L))[0]

def mostCommonFirstChar(L):
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p'
    """
    if not L:
        return "Z"
    else:
        return max(countFirsts(L), key=lambda key: countFirsts(L)[key])