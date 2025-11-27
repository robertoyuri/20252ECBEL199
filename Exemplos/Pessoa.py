#Classe Pai

class Pessoa:
    def __init__(self, nome, cpf, nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco

    def exibir(self):
        print("Nome: " + str(self.nome))
        print("CPF: " + str(self.cpf))
        print("Nascimento: " + str(self.nascimento))
        print("Endereço: " + str(self.endereco))

#Classe Filho 1
class Aluno(Pessoa):
    def __init__(self, nome, cpf, nascimento, endereco, matricula, curso, turma):
        super().__init__(nome, cpf, nascimento, endereco)
        self.matricula = matricula
        self.curso = curso
        self.turma = turma

    def exibir(self):
        super().exibir()
        print("Matricula: " + str(self.matricula))
        print("Curso: " + str(self.curso))
        print("Turma: " + str(self.turma))

#Classe Filho 2
class Professor(Pessoa):
    def __init__(self, nome, cpf, nascimento, endereco, formacao, siape, salario):
        super().__init__(nome, cpf, nascimento, endereco)
        self.formacao = formacao
        self.siape = siape
        self.salario = salario

    def exibir(self):
        super().exibir()
        print("Formação: " + str(self.formacao))
        print("SIAPE: " + str(self.siape))
        print("Salario: " + str(self.salario))


vinicius = Aluno("Vinicius Louchard", "000.000.000-00","27/07/1996", "UFRA", "2025000001", "Eng. Cartografica", "2025")
vinicius.exibir()

roberto = Professor("Roberto Franco", "900.012.789-99", "17/10/1989", "UFRA", "Ciência da Computação", "1111175", "R$: 1.000.000,67")
roberto.exibir()