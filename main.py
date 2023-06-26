from caixa import CaixaEletronico

def inicio(caixa):
    print("- Iniciar operação inserindo o cartão")
    caixa.transicao("CI")
    return True


def inserir_senha_autenticando(caixa):
    if caixa.estado_atual == "E" or caixa.estado_atual == "A":
        senha = input("Digite a senha da conta: ")
        caixa.transicao("Senha")
        caixa.senha_digitada = senha
        caixa.transicao(caixa.senha_digitada)

        if(caixa.senha_correta == caixa.senha_digitada):
            return True
        return False

def movimentacao(caixa):
    inicio(caixa)

    while caixa.estado_atual != "AS":
        inserir_senha_autenticando(caixa)

    ciAndSenhaOk(caixa)

def ciAndSenhaOk(caixa):
    while True:
        caixa.transicao("OS")
        print("Selecionando operação (S)")
        print("1. Realizar saque")
        print("2. Cancelar operação")
        print("0. Encerrar")
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do saque: "))
            caixa.realizar_saque(valor)
            caixa.transicao("OC")
        elif opcao == "2":
            caixa.transicao("Cancelar")
        elif opcao == "0":
            caixa.transicao("C")
            break
        else:
            print("Escolher valor valido")
        
        if caixa.operacao_concluida():
            print("Operação concluída")
        elif caixa.operacao_cancelada():
            print("Operação cancelada")

def main():
    caixa = CaixaEletronico()

    movimentacao(caixa)

if __name__ == "__main__":
    main()