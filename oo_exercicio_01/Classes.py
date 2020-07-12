class Ponto2D:

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y


class Retangulo(object):

    def __init__(self, esq_sup: Ponto2D, dir_inf: Ponto2D):

        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf

    @property
    def esq_sup(self) -> Ponto2D:
        return self.__esq_sup

    @property
    def dir_inf(self) -> Ponto2D:
        return self.__dir_inf

    @property
    def width(self) -> float:
        return self.dir_inf.x - self.esq_sup.x

    @property
    def height(self) -> float:
        return self.esq_sup.y - self.dir_inf.y

    def calcularArea(self) -> float:
        return self.height * self.width

    def __calcularAreaPontos(self, p1: Ponto2D, p2: Ponto2D) -> float:
        return (abs(p1.x - p2.x)) * (abs(p1.y - p2.y))

    def __checarIntersecao(self, ret) -> bool:
        if (
                self.esq_sup.x > ret.dir_inf.x
                or self.dir_inf.x < ret.esq_sup.x
                or self.dir_inf.y > ret.esq_sup.y
                or self.esq_sup.y < ret.dir_inf.y
        ):
            return False

        return True

    def __areaIntersecao(self, ret) -> float:

        # calculando pontos comuns
        min_x = max(self.esq_sup.x, ret.esq_sup.x)
        max_x = min(self.dir_inf.x, ret.dir_inf.x)
        min_y = max(self.dir_inf.y, ret.dir_inf.y)
        max_y = min(self.esq_sup.y, ret.esq_sup.y)

        p1 = Ponto2D(x=min_x, y=min_y)
        p2 = Ponto2D(x=max_x, y=max_y)

        return self.__calcularAreaPontos(p1=p1, p2=p2)

    def calcularIntersecao(self, ret):

        if self.__checarIntersecao(ret=ret):
            return self.__areaIntersecao(ret=ret)

        return None


def main():
    r1_esq_sup = Ponto2D(-6.5, 5.0)
    r1_dir_inf = Ponto2D(-2.0, 2.5)
    ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
    area1 = ret1.calcularArea()
    print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))

    r2_esq_sup = Ponto2D(2.0, 7.0)
    r2_dir_inf = Ponto2D(5.0, 4.0)
    ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
    area2 = ret2.calcularArea()
    print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))

    intersecao = ret1.calcularIntersecao(ret2)
    print(intersecao)

    # Saída esperada:
    #
    # 4.50 2.50 11.25
    # 3.00 3.00 9.00
    # None


if __name__ == "__main__":
    main()
