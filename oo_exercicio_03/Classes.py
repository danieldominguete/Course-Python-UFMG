from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, nome: str, valor: float):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @property
    @abstractmethod
    def desconto(self):
        pass

    @property
    @abstractmethod
    def tipo(self):
        pass


class Livro(Item):
    def __init__(self, nome: str, valor: float):
        super().__init__(nome, valor)
        self.__tipo = "Livro"
        self.__desconto = 0.03

    @property
    def desconto(self):
        return self.__desconto

    @property
    def tipo(self):
        return self.__tipo


class Brinquedo(Item):
    def __init__(self, nome: str, valor: float):
        super().__init__(nome, valor)
        self.__tipo = "Brinquedo"
        self.__desconto = 0.05

    @property
    def desconto(self):
        return self.__desconto

    @property
    def tipo(self):
        return self.__tipo


class Eletronico(Item):
    def __init__(self, nome: str, valor: float):
        super().__init__(nome, valor)
        self.__tipo = "Eletronico"
        self.__desconto = 0.08

    @property
    def desconto(self) -> float:
        return self.__desconto

    @property
    def tipo(self) -> str:
        return self.__tipo


class CestaCompras:
    def __init__(self):
        self.__itens = {}
        self.__valor_total = 0.0

    @property
    def itens(self) -> dict:
        return self.__itens

    @property
    def valor_total(self) -> float:
        return self.__valor_total

    def adicionar_item(self, item: Item, qtde: int) -> None:
        self.__itens[item] = qtde
        self.__valor_total += qtde * (item.valor - (item.valor * item.desconto))

    def relatorio_final(self) -> None:
        print(f"{self.valor_total:.2f}")

        for item, qtde in self.itens.items():
            tipo = f"{item.tipo}"
            nome = f"{item.nome}"
            valor_unit = f"{item.valor:.2f}"
            total_sem_desconto = f"{(qtde * item.valor):.2f}"
            total_com_desconto = f"{(qtde * (item.valor - (item.valor * item.desconto))):.2f}"

            print(
                f"{tipo}, {nome}, {qtde}, {valor_unit}, {total_sem_desconto}, {total_com_desconto}"
            )


def main():
    livro1 = Livro("Senhor dos Aneis", 15.00)
    brinq1 = Brinquedo("Carrinho", 12.99)

    cesta = CestaCompras()
    cesta.adicionar_item(livro1, 3)
    cesta.adicionar_item(brinq1, 4)

    cesta.relatorio_final()

# Saída esperada:
#
# 93.01
# Livro, Senhor dos Aneis, 3, 15.00, 45.00, 43.65
# Brinquedo, Carrinho, 4, 12.99, 51.96, 49.36

if __name__ == "__main__":
    main()
