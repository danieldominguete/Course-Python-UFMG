def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """
    if not L:
        return None
    else:
        return [name[-1] for name in L]

def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    """
    if not L:
        return None
    else:
        return [str(name[0][0].capitalize()) + ". " + str(name[-1].capitalize()) for name in L]

def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    """
    if not L:
        return None
    else:
        return [
            ". ".join(list(map(lambda name: name[0].capitalize(), group[:-1])))
            + ". "
            + str(group[-1])
            for group in L
        ]