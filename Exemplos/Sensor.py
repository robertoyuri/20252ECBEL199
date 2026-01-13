class Sensor:
    def __init__(self, local, valor):
        self.local = local
        self.valor = valor

    def calcular_risco(self):
        return 0

    def gerar_alerta(self):
        risco = self.calcular_risco()
        return f"Sensor em {self.local} - Risco: {risco}"

class SensorTemperatura(Sensor):
    def calcular_risco(self):
        if self.valor < 25:
            return 1
        elif self.valor < 40:
            return 2
        else:
            return 3

class SensorUmidade(Sensor):
    def calcular_risco(self):
        if self.valor < 30:
            return 3
        elif self.valor < 70:
            return 1
        else:
            return 2

class SensorFumaca(Sensor):
    def calcular_risco(self):
        if self.valor < 50:
            return 1
        else:
            return 4

sensores = [
    SensorTemperatura("Lab2", 40),
    SensorUmidade("Lab1", 75),
    SensorFumaca("Lab3", 80)
]

for sensor in sensores:
    print(sensor.gerar_alerta())