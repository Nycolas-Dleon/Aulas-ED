class ContaCorrente:
    def __init__ (self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f'Novo saldo: R${self.saldo:.2f}\n')

    def saque(self, valor):
        self.saldo -= valor
        print(f'Novo saldo: R${self.saldo:.2f}\n')

        

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular    

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero


    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo


conta1 = ContaCorrente('Nycolas', 1111, 0)
print(f'---Olá {conta1.titular}---')
print(f'Número da conta: {conta1.numero}')
print(f'Saldo disponível: R${conta1.saldo:.2f}\n')

action = None
while action != 3:
    print('---Ações---')
    print('1- Depositar\n2- Sacar\n3- Sair\n')
    action = int(input('Digite o número da ação: '))
    
    if action == 1:
        valor = 0
        while valor <= 0:
            valor = float(input('Digite o valor do depósito: '))
        conta1.deposito(valor)
    

    elif action == 2:
        valor = 0
        if conta1.saldo == 0:
            print('\n- Nenhum saldo disponível para saque -\n')
        
        else:
            print(f'\nSaldo disponível: R${conta1.saldo:.2f}\n')
            while valor <= 0:
                valor = float(input('Digite o valor do saque: '))
                if valor < 0:
                    print('Valor inválido!\n')
                elif (conta1.saldo - valor) < 0:
                    print('\nSaldo insuficiente')
                    print(f'Saldo disponível na conta: R${conta1.saldo:.2f}\n')
                    valor = 0
            conta1.saque(valor)
    
    elif action == 3:
        print('Obrigado, tenha um ótimo dia!')
        break

    else:
        action = int(input('Digite uma ação válida: '))
    action = None