import os

def soma():

    os.system("cls")
    numero1 = int(input("Digite o numero 1:"))
    numero2 = int(input("Digite o numero 2:"))
    print(f"Resultado da soma é {numero1+numero2}")
    print("="*20)

def subtracao():

    os.system("cls")
    numero1 = int(input("Digite o numero 1:"))
    numero2 = int(input("Digite o numero 2:"))
    print(f"Resultado da subtração é {numero1-numero2}")
    print("="*20)

def multiplicacao():

    os.system("cls")
    numero1 = int(input("Digite o numero 1:"))
    numero2 = int(input("Digite o numero 2:"))
    print(f"Resultado da multiplicação é {numero1*numero2}")
    print("="*20)

def divisao():

    os.system("cls")
    numero1 = int(input("Digite o numero 1:"))
    numero2 = int(input("Digite o numero 2:"))
    print(f"Resultado da divisão é {numero1/numero2}")
    print("="*20)


if __name__=="__main__":

    print ("===========* CALCULADORA SIMPLES *===========")
    opcao = -1
    while opcao:
        print("[1] - SOMA")
        print("[2] - SUBTRAÇÃO")
        print("[3] - MULTIPLICAÇÃO")
        print("[4] - DIVISÃO")
        print("[0] - SAIR")
        opcao = input("Escolha uma opção:")

        if opcao=='1':
            soma()
        elif opcao=='2':
            subtracao()
        elif opcao == '3':
            multiplicacao()
        elif opcao == '4':
            divisao()
        elif opcao=='0':
            print("saindo da calculadora")
            break
        else:
            print("essa opção é invalida!")
