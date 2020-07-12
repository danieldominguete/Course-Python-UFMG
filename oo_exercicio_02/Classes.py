class Conta:
    def __init__(self, num_conta: int):
        self.__num_conta = num_conta
        self.__saldo = 0

    @property
    def saldo(self) -> float:
        return self.__saldo

    def depositar(self, valor: float):
        self.__saldo = self.__saldo + valor

    def sacar(self, valor: float):
        self.__saldo = self.__saldo - valor


class ContaCorrente(Conta):
    def __init__(self, num_conta: int, taxa: float):
        super().__init__(num_conta=num_conta)
        self.__taxa = taxa

    def cobrar_taxa(self):
        self.sacar(self.__taxa)


class ContaPoupanca(Conta):
    def __init__(self, num_conta: int, juros: float):
        super().__init__(num_conta=num_conta)
        self.__juros = juros

    def aplicar_juros(self):
        valor = self.saldo * self.__juros
        self.depositar(valor)


def main():

    conta_corrente = ContaCorrente(1, 1.50)
    conta_corrente.depositar(10)
    conta_corrente.cobrar_taxa()
    print(conta_corrente.saldo)


if __name__ == "__main__":
    main()
