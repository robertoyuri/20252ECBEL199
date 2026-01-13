class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def som(self):
        print("Som genérico de animal")

class Gato(Animal):
    def __init__(self, nome, raca, pelo):
        super().__init__(nome, raca)
        self.pelo = pelo

    def som(self):
        print("Miau Miau")

class Vaca(Animal):
    def __init__(self, nome, raca, tamanho):
        super().__init__(nome, raca)
        self.tamanho = tamanho

    def som(self):
        print("Muuuuuu")

class Cachorro(Animal):
    def __init__(self, nome, raca, porte):
        super().__init__(nome, raca)
        self.porte = porte

    def som(self):
        print("Au Au")

g = Gato("Pitú", "SRD", "Branco")
g.som()
v = Vaca("vaca", "SRD", "grande")
v.som()
c = Cachorro("dog", "pitbull", "Medio")
c.som()