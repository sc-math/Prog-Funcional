def opcao():    #Função para receber a opção que a pessoa irá escolher
    opcao = input("Escolha uma opção:")
    if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        opcao = opcaoValida()
        return opcao
    else:
        return opcao

def opcaoValida():    #Caso a pessoa digite um valor errado para a opção essa função será chamada
    opcao = input("Escolha uma opção válida:")
    if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        return opcaoValida()
    else:
        return opcao

def TelaPrincipal():    #Função para imprimir a tela principal
    print(">--------------------------<")
    print("| 1 - Deposito             |")
    print("| 2 - Saque                |")
    print("| 3 - Saldo                |")
    print("| 4 - Relatório            |")
    print("| 5 - Finalizar            |")
    print(">--------------------------<")

def Saldo(n100,n50,n20,n10,n5,n2,n1):    #Calcula o saldo atual
    a = 100 * n100
    b = 50 * n50
    c = 20 * n20
    d = 10 * n10
    e = 5 * n5
    f = 2 * n2
    g = 1 * n1
    return a + b + c + d + e + f + g

def Operacoes(opcao,n100,n50,n20,n10,n5,n2,n1):   #Função para chamar as operações
    if opcao == "1":
        Operacao1(n100,n50,n20,n10,n5,n2,n1)        #Função para operação 1
        OutraOperacao(n100,n50,n20,n10,n5,n2,n1)
    if opcao == "2":
        Operacao2(n100,n50,n20,n10,n5,n2,n1)        #Função para operação 2
        OutraOperacao(n100,n50,n20,n10,n5,n2,n1)
    if opcao == "3":
        Operacao3(n100,n50,n20,n10,n5,n2,n1)        #Função para operação 3
        OutraOperacao(n100,n50,n20,n10,n5,n2,n1)
    if opcao == "4":
        Operacao4(n100,n50,n20,n10,n5,n2,n1)        #Função para operação 4
        OutraOperacao(n100,n50,n20,n10,n5,n2,n1)
    if opcao == "5":
        Operacao5(n100,n50,n20,n10,n5,n2,n1)        #Função para operação 5

def Operacao1(n100,n50,n20,n10,n5,n2,n1):    #Função para a operação 1
    print("--------------------------------")
    print("Você escolheu a função Deposito.")
    print("--------------------------------")
    print("Quanto deseja depositar?")
    v = float(input("R$"))
    qtn100 = v // 100
    x = v % 100
    qtn50 = x // 50
    x = x % 50
    qtn20 = x // 20
    x = x % 20
    qtn10 = x // 10
    x = x % 10
    qtn5 = x // 5
    x = x % 5
    qtn2 = x // 2
    qtn1 = x % 2
    if qtn1 > 0 and qtn1 < 1 or qtn1 > 1 and qtn1 < 2:    #Verifica se o valor digitado não possui decimal(moedas)
        print("Erro! Só aceitamos deposito com notas.")
    else:
        print("Você escolheu depositar R${:.2f}".format(v))
        print("Como deseja depositar este valor?")      #A pessoa colocará a quantidade de notas que irá depositar
        a = int(input("Notas de R$100,00:"))
        b = int(input("Notas de R$50,00:"))
        c = int(input("Notas de R$20,00:"))
        d = int(input("Notas de R$10,00:"))
        e = int(input("Notas de R$5,00:"))
        f = int(input("Notas de R$2,00:"))
        g = int(input("Notas de R$1,00:"))
        i = a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + g *1
        if i != v:      #Verifica se o valor digitado é igual ao valor de deposito selecionado
            print("Valor informado não correspondente ao valor selecionado para depósito.")
        else:            #Realiza o deposito
            n100 = n100 + a
            n50 = n50 + b
            n20 = n20 + c
            n10 = n10 + d
            n5 = n5 + e
            n2 = n2 + f
            n1 = n1 + g
            print("Deposito realizado.")
            return OutraOperacao(n100,n50,n20,n10,n5,n2,n1)         #Chama uma função para perguntar se a pessoa deseja sair ou fazer outra operação

def Operacao2(n100,n50,n20,n10,n5,n2,n1):    #Função para a operação 2
    print("-----------------------------")
    print("Você escolheu a função Saque.")
    print("-----------------------------")
    print("Quanto deseja sacar?")
    v = float(input("R$"))
    qtn100 = v // 100
    x = v % 100
    qtn50 = x // 50
    x = x % 50
    qtn20 = x // 20
    x = x % 20
    qtn10 = x // 10
    x = x % 10
    qtn5 = x // 5
    x = x % 5
    qtn2 = x // 2
    qtn1 = x % 2
    if qtn1 > 0 and qtn1 < 1 or qtn1 > 1 and qtn1 < 2:      #Verifica se o valor digito não possui decimal(moedas)
        print("Erro! Não sacamos moedas.")
    elif v > Saldo(n100,n50,n20,n10,n5,n2,n1):
        print("Não há notas suficientes para o valor do saque informado.")      #Verifica se há saldo suficiente para saque
    else:
        y = input("Você deseja escolher as notas?(S/N)")            #Pergunta se a pessoa deseja escolher as notas que irá sacar
        if y == "N" or y == "n":
            if qtn100 > n100 or qtn50 > n50 or qtn20 > n20 or qtn10 > n10 or qtn5 > n5 or qtn2 > n2 or qtn1 > n1:           #Confere a quantidade de notas no estoque
                print("Não há notas suficientes para o valor do saque informado.")
            else:
                n100 = n100 - qtn100
                n50 = n50 - qtn50
                n20 = n20 - qtn20
                n10 = n10 - qtn10
                n5 = n5 - qtn5
                n2 = n2 - qtn2
                n1 = n1 - qtn1
                print("Saque realizado com sucesso.")
                print("Retire seu dinheiro.")
                notas100(qtn100)
                notas50(qtn50)
                notas20(qtn20)
                notas10(qtn10)
                notas5(qtn5)
                notas2(qtn2)
                notas1(qtn1)
                return OutraOperacao(n100, n50, n20, n10, n5, n2, n1)
        else:
            print("Você escolheu sacar R${:.2f}".format(v))         #Forma que a pessoa deseja sacar
            print("Como deseja sacar este valor?")
            a = int(input("Notas de R$100,00:"))
            b = int(input("Notas de R$50,00:"))
            c = int(input("Notas de R$20,00:"))
            d = int(input("Notas de R$10,00:"))
            e = int(input("Notas de R$5,00:"))
            f = int(input("Notas de R$2,00:"))
            g = int(input("Notas de R$1,00:"))
            i = a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + g *1
            if i != v:      #Verifica se o valor digitado é igual ao valor selecionado para saque
                print("Valor informado não correspondente ao valor selecionado para saque.")
            else:
                if n100 < a or n50 < b or n20 < c or n10 < d or n5 < e or n2 < f or n1 < g:     #Verifica se há notas suficientes para saque
                    print("Não há notas suficientes para o valor do saque informado.")
                else:             #Realiza o saque
                    n100 = n100 - a
                    n50 = n50 - b
                    n20 = n20 - c
                    n10 = n10 - d
                    n5 = n5 - e
                    n2 = n2 - f
                    n1 = n1 - g
                    print("Saque realizado com sucesso.")
                    print("Retire seu dinheiro.")
                    notas100(a)
                    notas50(b)
                    notas20(c)
                    notas10(d)
                    notas5(e)
                    notas2(f)
                    notas1(g)
                    return OutraOperacao(n100,n50,n20,n10,n5,n2,n1)

def Operacao3(n100,n50,n20,n10,n5,n2,n1):    #Função para a operação 3 que imprime o saldo
    print("-----------------------------")
    print("Você escolheu a função Saldo.")
    print("-----------------------------")
    print("Saldo Total: R${:.2f}".format(Saldo(n100,n50,n20,n10,n5,n2,n1)))

def Operacao4(n100, n50, n20, n10, n5, n2, n1):    #Função para a opeção 4 que mostra o relatório
    print("---------------------------------")
    print("Você escolheu a função Relatório.")
    print("---------------------------------")
    print("Notas de R$ 100,00: {}".format(n100))
    print("Notas de R$ 50,00: {}".format(n50))
    print("Notas de R$ 20,00: {}".format(n20))
    print("Notas de R$ 10,00: {}".format(n10))
    print("Notas de R$ 5,00: {}".format(n5))
    print("Notas de R$ 2,00: {}".format(n2))
    print("Notas de R$ 1,00: {}".format(n1))
    print(" ")
    print("Saldo Total: {:.2f}".format(Saldo(n100,n50,n20,n10,n5,n2,n1)))

def Operacao5(n100,n50,n20,n10,n5,n2,n1):    #Encerra o programa
    if Saldo(n100,n50,n20,n10,n5,n2,n1) > 0:        #Se tiver saldo no caixa irá perguntar se a pessoa deseja sair tudo
        print("---------------------------")
        print("Ainda há dinheiro no caixa.")
        x = input(("Deseja sacar os R${:.2f} antes de finalizar?(S/N)".format(Saldo(n100,n50,n20,n10,n5,n2,n1))))
        if x == "S" or x == "s":
            x = Saldo(n100,n50,n20,n10,n5,n2,n1)
            print("Saque realizado com sucesso.")
            print("Retire seu dinheiro.")
            notas100(n100)
            notas50(n50)
            notas20(n20)
            notas10(n10)
            notas5(n5)
            notas2(n2)
            notas1(n1)
            print("Valor sacado: R${:.2f}".format(x))
    print("--------------------------")
    print("Obrigado, volte sempre! ^^")

def OutraOperacao(n100,n50,n20,n10,n5,n2,n1):    #Pergunta após uma operação se o usuario deseja fazer outra, caso contrario ela encerra o programa
    print("----------------------------------")
    x = input("Deseja fazer outra operação?(S/N)")
    if x == "N" or x == "n":
        if Saldo(n100, n50, n20, n10, n5, n2, n1) > 0:          #Fala que tem saldo no caixa e pergunta se deseja sacar
            print("---------------------------")
            print("Ainda há dinheiro no caixa.")
            x = input(("Deseja sacar os R${:.2f} antes de finalizar?(S/N)".format(Saldo(n100, n50, n20, n10, n5, n2, n1))))
            if x == "S" or x == "s":
                x = Saldo(n100, n50, n20, n10, n5, n2, n1)
                print("Saque realizado com sucesso.")
                print("Retire seu dinheiro.")
                notas100(n100)
                notas50(n50)
                notas20(n20)
                notas10(n10)
                notas5(n5)
                notas2(n2)
                notas1(n1)
                print("Valor sacado: R${:.2f}".format(x))
        print("--------------------------")
        print("Obrigado, volte sempre! ^^")
        quit()
    else:
        principal(n100,n50,n20,n10,n5,n2,n1)

def notas100(i):            #Função para imprimir as notas
    if i > 0:
        print("R$100,00")
        return notas100(i - 1)

def notas50(i):             #Função para imprimir as notas
    if i > 0:
        print("R$50,00")
        return notas50(i - 1)

def notas20(i):             #Função para imprimir as notas
    if i > 0:
        print("R$20,00")
        return notas20(i - 1)

def notas10(i):             #Função para imprimir as notas
    if i > 0:
        print("R$10,00")
        return notas10(i - 1)

def notas5(i):             #Função para imprimir as notas
    if i > 0:
        print("R$5,00")
        return notas5(i - 1)

def notas2(i):             #Função para imprimir as notas
    if i > 0:
        print("R$2,00")
        return notas2(i - 1)

def notas1(i):             #Função para imprimir as notas
    if i > 0:
        print("R$1,00")
        return notas1(i - 1)

def principal(n100,n50,n20,n10,n5,n2,n1):       #Função Main
    TelaPrincipal()
    x = opcao()
    Operacoes(x,n100,n50,n20,n10,n5,n2,n1)

principal(1,1,1,1,1,1,1)