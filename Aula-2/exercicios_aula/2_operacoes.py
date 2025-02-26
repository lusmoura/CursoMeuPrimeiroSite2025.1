# # # # # # # 
# Inteiros  #
# # # # # # #
 
# Note que nos exemplos abaixo podemos utilizar variáveis para armazenar os valores que serão utilizados nas operações
# Mas também podemos utilizar variávais apenas para etapas intermediárias da operação ou até mesmo não utilizar variáveis

## Adição - cada variável contém um número inteiro e uma parte da operação de adição
from re import sub


numero_1 = 10
numero_2 = 5
soma = numero_1 + numero_2
print(soma)

## Subtração - cada variável contém um valor, mas a operação de subtração é feita diretamente no print
numero_1 = 10
numero_2 = 5
print(numero_1 - numero_2)

## Multiplicação - utilizamos variáveis apenas para armazenar o restulado da operação
multiplicacao = 10 * 5
print(multiplicacao)

## Divisão - reutilizamos variáveis com valores definidos anteriormente
print(numero_1 / numero_2)

## Resto da divisão - não utilizamos variáveis
print(10 % 5)

# # # # # # # # # # # # # # #
# Float - números decimais  #
# # # # # # # # # # # # # # #

# A partir de agora, vamos utilizar variáveis apenas para armazenar valores que serão utilizados em operações
# Essa é considerada uma boa prática de programação, pois facilita a leitura do código

numero_1 = 10.5
numero_2 = 5.5

## Adição
soma = numero_1 + numero_2
print(soma)

## Subtração
subtracao = numero_1 - numero_2
print(numero_1 - numero_2) 

## Multiplicação
multiplicacao = numero_1 * numero_2
print(multiplicacao)

## Divisão
divisao = numero_1 / numero_2
print(divisao)

## Divisão inteira
divisao_inteira = numero_1 // numero_2
print(divisao_inteira)

## Resto da divisão
resto = numero_1 % numero_2
print(resto)


# ... continuar
# thonny
# precendencia de operadores