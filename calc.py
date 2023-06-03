import math

# cores
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

# função para arredondamento
def arredondamento(x):
    valor_arredondado = math.ceil(x * 100) / 100
    return valor_arredondado

# recebendo e atribuindo valores
total = float(input("Digite o valor total: R$"))
g1 = float(input("Odd da casa 1: "))
g2 = float(input("Odd da casa 2: "))
sure = (100/g1) + (100/g2)
sure = arredondamento(sure)
lucro_aproximado = 100 - sure;
lucro_aproximado = arredondamento(lucro_aproximado)

# imprime as informações
print(BLUE, "############## Calculando ##############\n", RESET)
print(REVERSE, "Total: R$", total, " - Odd1: ", g1, " - Odd2: ", g2, " - lucro: ", arredondamento(100 - sure), "% ", RESET, "\n")

# verifica se é uma surebet
if sure < 100:
    txt_sure = "SIM"
    var_sure = 1
    print(BLUE, "É uma aposta segura\n", RESET)
    lucro_aproximado = 100 - sure
    lucro_aproximado = arredondamento(lucro_aproximado)
    x = (total/100)*((100 + lucro_aproximado)/g1)
    x = arredondamento(x)
    y = (total/100)*((100 + lucro_aproximado)/g2)
    y = arredondamento(y)
    lucro1 = (x * g1) - y
    lucro1 = arredondamento(lucro1)
    lucro2 = (y * g2) - x
    lucro2 = arredondamento(lucro2)
    
    # Imprimindo o resultado
    print(BOLD, "Valor ideal de entrada 1: R$", x, "\n")
    print(GREEN, "Valor de lucro na vitoria 1: R$", lucro1, " (R$" , arredondamento(x * g1), " (bruto) - R$", y, ")\n")
    print(BOLD, "Valor ideal de entrada 2: ", y, "\n")
    print(GREEN, "Valor de lucro na vitoria 2: ", lucro2, " (R$" , arredondamento(y * g2), " (bruto) - R$", x, ")\n")
    print(BLUE, "Lucro esperado: R$", arredondamento(lucro1 - x), "\n")
# se não for
else:
    txt_sure = "NÃO"
    var_sure = 0
    print(RED, "Não é uma aposta segura\n", RESET)
