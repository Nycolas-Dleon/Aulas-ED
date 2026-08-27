# Lista Sequencial -----------------

class Lista:
    def __init__(self, max):
        self.__dados = [None] * max
        self.__tamanho = 0

# [1] Imprimir

    def __str__(self):
        return str(self.__dados)

# [2] Inserir

    def inserir(self, dado, indice):
        if self.__tamanho == len(self.__dados):
            return False

        elif indice < 0:
            indice = 0

        elif indice > self.__tamanho:
            indice = self.__tamanho

        for i in range(self.__tamanho, indice, -1):
            self.__dados[i] = self.__dados[i-1]
        self.__dados[indice] = dado
        self.__tamanho += 1

# [3] Adicionar

    def adicionar(self, dado):
        if self.__tamanho == len(self.__dados):
            return False
        self.__dados[self.__tamanho] = dado
        self.__tamanho += 1
        return True

# [4] Retirar
    def retirar(self, indice):
        if indice < 0 or indice > self.__tamanho:
            return None
        
        dado = self.__dados[indice]
        
        for i in range(indice, self.__tamanho-1):
            self.__dados[i] = self.__dados[i+1]
        
        self.__dados[self.__tamanho-1] = None
        self.__tamanho -= 1
        
        return dado

# [5] Remover
    def remover(self, dado):
        
        indice = self.posicao(dado)
        
        if indice:
            self.retirar(indice)
            return indice

# [6] Valor

    def valor(self, indice):
        return self.__dados[indice]

# [7] Posição

    def posicao(self, dado):
        for i in range(self.__tamanho):
            if self.__dados[i] == dado:
                return i

        return None

# [8] Tamanho

    def tamanho(self):
        return self.__tamanho

# [9] Modificar

    def modificar(self, indice, valor):
        self.__dados[indice] = valor
        return self.__dados

def esvaziar_lista(lista):
    for i in range(lista.tamanho()):
        lista.retirar(0)

lista = Lista(10)

# Menu ------------------

while True:
    print(
    '''
    Editor de listas
    [1] Imprimir
    [2] Inserir
    [3] Adicionar
    [4] Retirar
    [5] Remover
    [6] Valor
    [7] Posição
    [8] Tamanho
    [9] Modificar
    [0] Encerrar\n
    [10] Esvaziar Lista\n
    '''
    )

    opcao = int(input('Digite sua opção: '))
    if opcao == 0:
        break
    else:
        if opcao == 1:
            print(f'\nLista: {lista.__str__()}')
        elif opcao == 2:
            dado = input('Dado a ser inserido: ')
            indice = int(input('Índice em que será inserido: '))
            lista.inserir(dado, indice)
            print(f'\nLista: {lista}')
        elif opcao == 3:
            dado = input('Dado a ser inserido: ')
            lista.adicionar(dado)
            print(f'\nLista: {lista}')
        elif opcao == 4:
            indice = int(input('Índice do item a ser retirado: '))
            lista.retirar(indice)
            print(f'\nLista: {lista}')
        elif opcao == 5:
            dado = input('Dado a ser removido: ')
            lista.remover(dado)
            print(f'Lista: {lista}')
        elif opcao == 6:
            indice = int(input('Índice a ser verificado: '))
            print(f'Valor do dado no índice {indice}: {lista.valor(indice)}')
        elif opcao == 7:
            dado = input('Dado a ser verificado: ')
            print(f'Índice do dado {dado}: {lista.posicao(dado)}')
        elif opcao == 8:
            print(f'Tamanho da lista: {lista.tamanho()}')
        elif opcao == 9:
            indice = -1
            while indice < 0 or indice > lista.tamanho():
                indice = int(input('Digite o índice do dado a ser modificado: '))
            valor = input('Digite o novo valor a ser atribuído: ')
            lista.modificar(indice, valor)
            print(f'\nLista: {lista}')
        elif opcao == 10:
            lista = esvaziar_lista(lista)
            print(lista)