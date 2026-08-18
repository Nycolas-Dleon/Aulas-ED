# ----- Exercício -----

# Q1 -
'''
class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def __str__(self):
        return f'{self.dia:02d}/{self.mes:02d}/{self.ano}'

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia    

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes


    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

data1 = Data(18, 8, 2026)
print(data1.__str__())
'''
# Q2 -

class Aluno:
    def __init__(self, nome, matricula, notas = []):
        self.__nome = nome
        self.__matricula = matricula 
        self.__notas = notas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    def s_matricula(self):
        matricula = str(self.__matricula)
        return f'{matricula[0:4]}.{matricula[4:6]}.{matricula[6:8]}.{matricula[8:]}'

    def media(self, notas):
        return round(sum(self.__notas) / len(self.__notas))

    def adiciona_nota(self, nota):
        self.__notas.append(nota)

aluno1 = Aluno('João', 202614320023)
aluno1.adiciona_nota(70)
aluno1.adiciona_nota(80)
print(f'Matricula:{aluno1.s_matricula}')
print(f'Nome:{aluno1.nome}')
print(f'Media:{aluno1.media}')