class CaixaEletronico:
    def __init__(self):
        self.estado_atual = "I"
        self.saldo = 1000
        self.senha_correta = "123456"
        self.senha_digitada = ""

    def transicao(self, simbolo):
        if self.estado_atual == "I" and simbolo == "CI":
            self.estado_atual = "E"
            print("Estado atual de Entrada (E), aguardando autenticação: ")
        elif self.estado_atual == "E" and simbolo == "Senha":
            self.estado_atual = "A"
            print("Estado atual A, aguardando autenticação")
        elif self.estado_atual == "A" and simbolo == self.senha_correta:
            self.estado_atual = "AS"
            print("Estado atual AS, Autenticação Segura")
        elif self.estado_atual == "AS" and simbolo == "OS":
            self.estado_atual = "S"
            print("Estado atual S, Aguardando Seleção de operação")
        elif self.estado_atual == "S" and simbolo == "OC":
            self.estado_atual = "P"
            print("Estado atual P, processando")
        elif self.estado_atual == "P" and simbolo == "OC":
            self.estado_atual = "S"
            print("Estado atual S, Aguardando Seleção de operação")
        elif self.estado_atual == "P" and simbolo == "OC":
            self.estado_atual = "C"
            print("Estado atual C, estado de conclusão")
        elif (self.estado_atual == "S" or self.estado_atual == "P") and simbolo == "Cancelar":
            self.estado_atual = "S"
            print("Estado atual S, Aguardando Seleção de operação")

    def operacao_concluida(self):
        return self.estado_atual == "C"

    def operacao_cancelada(self):
        return self.estado_atual == "S"

    def realizar_saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo restante: R${self.saldo}")
        else:
            print("Saldo insuficiente.")
