class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def __str__(self):
        return self.modelo + " " + self.cor + " " + self.ano

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro foi ligado")
        else:
            print("O carro já está ligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print("O carro foi acelerado! Velocidade: "+str(self.velocidade)+"km/h")
        else:
            print("O carro não está ligado")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print("O carro foi freado! Velocidade: "+str(self.velocidade)+"km/h")
        else:
            print("O carro está parado")

palio = Carro("Cinza", "Palio", "2010")
print(palio)
palio.ligar()
palio.acelerar()
palio.acelerar()
palio.frear()
palio.acelerar()