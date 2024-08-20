class Cliente:
    def __init__(self, nome, agencia, numero_conta):
        self.nome = nome
        self.agencia = agencia
        self.numero_conta = numero_conta


class ContaBancaria:
    def __init__(self, cliente):
        self.cliente = cliente
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.historico.append(f"Saque: R${valor:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        print(f"Saldo: R${self.saldo:.2f}")
        print("Extrato bancário:")
        for transacao in self.historico:
            print(transacao)

    def transferencia(self, valor, conta_destino):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                conta_destino.depositar(valor)
                self.historico.append(f"Transferência para conta {conta_destino.cliente.numero_conta}: R${valor:.2f}")
                conta_destino.historico.append(f"Transferência recebida de conta {self.cliente.numero_conta}: R${valor:.2f}")
            else:
                print("Conta com saldo insuficiente para transferência")
        else:
            print("O valor da transferência deve ser positivo.")


class Banco:
    def __init__(self):
        self.contas = {}

    def incluir_conta(self):
        nome = input("Nome do cliente: ")
        agencia = input("Agência: ")
        numero_conta = input("Número da conta: ")
        cliente = Cliente(nome, agencia, numero_conta)
        if numero_conta not in self.contas:
            self.contas[numero_conta] = ContaBancaria(cliente)
            print("Conta incluída com sucesso.")
        else:
            print("Número da conta já existe.")

    def alterar_conta(self):
        numero_conta = input("Número da conta a ser alterada: ")
        if numero_conta in self.contas:
            novo_nome = input("Novo nome do cliente: ")
            novo_agencia = input("Nova agência: ")
            self.contas[numero_conta].cliente.nome = novo_nome
            self.contas[numero_conta].cliente.agencia = novo_agencia
            print("Conta alterada com sucesso.")
        else:
            print("Número da conta não encontrado.")

    def excluir_conta(self):
        numero_conta = input("Número da conta a ser excluída: ")
        if numero_conta in self.contas:
            del self.contas[numero_conta]
            print("Conta excluída com sucesso.")
        else:
            print("Número da conta não encontrado.")

    def exibir_todas_contas(self):
        for conta in self.contas.values():
            print(f"Nome: {conta.cliente.nome}, Agência: {conta.cliente.agencia}, Número da Conta: {conta.cliente.numero_conta}, Saldo: R${conta.saldo:.2f}")

    def exibir_uma_conta(self):
        numero_conta = input("Número da conta: ")
        if numero_conta in self.contas:
            conta = self.contas[numero_conta]
            print(f"Nome: {conta.cliente.nome}, Agência: {conta.cliente.agencia}, Número da Conta: {conta.cliente.numero_conta}, Saldo: R${conta.saldo:.2f}")
        else:
            print("Número da conta não encontrado.")

    def deposito(self):
        numero_conta = input("Número da conta para depósito: ")
        if numero_conta in self.contas:
            valor = float(input("Valor do depósito: R$"))
            self.contas[numero_conta].depositar(valor)
            print("Depósito realizado com sucesso.")
        else:
            print("Número da conta não encontrado.")

    def saque(self):
        numero_conta = input("Número da conta para saque: ")
        if numero_conta in self.contas:
            valor = float(input("Valor do saque: R$"))
            self.contas[numero_conta].sacar(valor)
            print("Saque realizado com sucesso.")
        else:
            print("Número da conta não encontrado.")

    def saldo(self):
        numero_conta = input("Número da conta: ")
        if numero_conta in self.contas:
            self.contas[numero_conta].extrato()
        else:
            print("Número da conta não encontrado.")

    def historico(self):
        numero_conta = input("Número da conta: ")
        if numero_conta in self.contas:
            self.contas[numero_conta].extrato()
        else:
            print("Número da conta não encontrado.")

    def transferencia(self):
        numero_conta_origem = input("Número da conta origem: ")
        numero_conta_destino = input("Número da conta destino: ")
        if numero_conta_origem in self.contas and numero_conta_destino in self.contas:
            valor = float(input("Valor da transferência: R$"))
            conta_origem = self.contas[numero_conta_origem]
            conta_destino = self.contas[numero_conta_destino]
            conta_origem.transferencia(valor, conta_destino)
            print("Transferência realizada com sucesso.")
        else:
            print("Número da conta origem ou destino não encontrado.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1 - Incluir conta")
            print("2 - Alterar conta")
            print("3 - Excluir conta")
            print("4 - Exibir todas as contas")
            print("5 - Exibir uma conta")
            print("6 - Depósito")
            print("7 - Saque")
            print("8 - Saldo")
            print("9 - Histórico (Extrato)")
            print("10 - Transferência")
            print("11 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.incluir_conta()
            elif opcao == '2':
                self.alterar_conta()
            elif opcao == '3':
                self.excluir_conta()
            elif opcao == '4':
                self.exibir_todas_contas()
            elif opcao == '5':
                self.exibir_uma_conta()
            elif opcao == '6':
                self.deposito()
            elif opcao == '7':
                self.saque()
            elif opcao == '8':
                self.saldo()
            elif opcao == '9':
                self.historico()
            elif opcao == '10':
                self.transferencia()
            elif opcao == '11':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


banco = Banco()
banco.menu()
