'''
ED Lineares -

- Lista | Seq e Enc 
- Pilha | Seq e Enc
- Fila  | Seq e Enc

Implementação:
- Sequencial: Variáveis estáticas
- Encadeada: Variáveis dinâmicas
'''

# Lista Sequencial -----------------

class Lista:
    def __init__(self, max):
        self.__dados = [None] * max
        self.__tamanho = 0

#Insere um novo valor ao final da lista
    def inserir_final(self, dado):
        if self.__tamanho == len(self.__dados):
            return False
        self.__dados[self.__tamanho] = dado
        self.__tamanho += 1
        return True

# Insere um novo valor em qualquer posição da lista
    def inserir(self, dado, posicao):
        if self.__tamanho == len(self.__dados):
            return False

        elif posicao < 0:
            posicao = 0

        elif posicao > self.__tamanho:
            posicao = self.__tamanho

        for i in range(self.__tamanho, posicao, -1):
            self.__dados[i] = self.__dados[i-1]
        self.__dados[posicao] = dado
        self.__tamanho += 1

# Busca a posição de um dado na lista
    def buscar(self, dado):
        for i in range(self.__tamanho):
            if self.__dados[i] == dado:
                return i

        return None


# Remove um dado de acordo com a posição fornecida
    def remover_posicao(self, posicao):
        if posicao < 0 or posicao > self.__tamanho:
            return None
        
        dado = self.__dados[posicao]
        
        for i in range(posicao, self.__tamanho-1):
            self.__dados[i] = self.__dados[i+1]
        
        self.__dados[self.__tamanho-1] = None
        self.__tamanho -= 1
        
        return dado

# Remove um dado, buscando sua posição na lista
    def remover_dado(self, dado):
        '''
        posicao = self.buscar(dado)
        
        if posicao:
            self.remover_posicao(posicao)
            return posicao
        '''

    def __str__(self):
        return str(self.__dados)

# Testes ---------------------
lista = Lista(5)
print(lista)
lista.inserir_final('Valor')
print(lista)
lista.inserir_final('X')
print(lista)
lista.inserir('Y', 0)
print(lista)

print(lista.buscar('X'))

lista.inserir_final('A')
lista.inserir_final('B')
print(lista)


lista.remover_posicao(2)
print(lista)