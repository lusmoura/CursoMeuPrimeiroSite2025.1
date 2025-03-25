# # # #
# for #
# # # #

# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i)

# lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
    
# dicionario
dicionario = {"nome": "João", "idade": 20}
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
    
# # # # #
# while #
# # # # #

# contador
numero = 0
while numero < 10:
    print(numero)
    numero += 1

# chamada de atendimento
opcao = int(input("Digite uma opcao: "))

while opcao != 0:
    if opcao == 1:
        print("Voce quer falar com um atendente")
    elif opcao == 2:
        print("Voce quer resolver um problema")
    else:
        print("Essa opcao é invalida")
    
    opcao = int(input("Digite uma opcao: "))