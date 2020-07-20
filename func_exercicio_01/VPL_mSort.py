def head(L):
    return L[0]


def tail(L):
    return L[1]


def py2ll(L):
    # lista nativa python em lista encadeada
    if not L:
        return None
    else:
        return (L[0], py2ll(L[1:]))


def ll2py(L):
    # lista encadeada para lista nativa
    if not L:
        return None
    else:
        H = head(L)
        T = tail(L)
        return [H] + ll2py(T)


def size(L):
    # tamanho de uma lista encadeada
    if not L:
        return None
    else:
        return 1 + size(tail(L))


def sorted(L):
    # Retorna true quando L for lista ordenada ascendente e Falso ao contrario
    if not L:
        return True
    elif not tail(L):
        return True
    else:
        C1 = head((L)) <= head(tail(L))
        return C1 and sorted(tail(L))


def sum(L):
    # retorna a soma dos elementos da lista encadeada L
    if not L:
        return 0
    else:
        return head(L) + sum(tail(L))


def split(L):
    # Recebe uma lista encadeada e retorna duas listas encadeadas divididas equalitariamente
    if not L:
        return (None, None)
    if not tail(L):
        return (L, None)
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0, T1) = split(tail(tail(L)))
        return ((H0, T0), (H1, T1))


def merge(L0, L1):
    # Juntar duas listas
    if not L0:
        return L1
    if not L1:
        return L0
    else:
        H0 = head(L0)
        T0 = tail(L0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0, L1))
        else:
            return (H1, merge(L0, T1))


def mSort(L):
    # Recebe uma lista L e retorne uma lista ordenada
    if not (L):
        return None
    if not tail(L):
        return L
    else:
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))


def max(L):
    # retorna o maior elemento na lista encadeada L
    if not L:
        return 0
    if not tail(L):
        return head(L)
    if not sorted(L):
        return max(mSort(L))
    else:
        return max(tail(L))


def get(L, N):
    # retorna o n-ésimo elemento da lista encadeada L
    if not L:
        return None
    if N == 0:
        return head(L)
    else:
        return get(tail(L), N - 1)


def main():
    print(max(py2ll([3, 4, 2, 5, 2, 1])))
    print(max(py2ll([0, 0, 0, 0])))
    print(max(py2ll([0, 0, 1, 0])))
    print(sum(py2ll([0, 0, 1, 0])))
    print(sum(py2ll([1, 2, 3, 4])))
    print(get(py2ll([3, 4, 2, 5, 2, 1]), 0))
    print(get(py2ll([3, 4, 2, 5, 2, 1]), 1))
    print(get(py2ll([3, 4, 2, 5, 2, 1]), 2))


if __name__ == "__main__":
    main()
