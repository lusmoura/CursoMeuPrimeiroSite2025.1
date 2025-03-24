# # # #
# if  #
# # # #

# if verdadeiro
if True:
    print("Isso será impresso na tela")
    
# if falso
if False:
    print("Isso não será impresso na tela")
    
# if com variável
texto = input("Digite um texto: ")
if texto == "python":
    print("Você digitou 'python'")

# if com numero
numero = int(input("Digite um número: "))
if numero > 10:
    print("O número é maior que 10")
    
texto = input("Digite um texto: ")
tamanho_texto = len(texto)
if tamanho_texto > 10:
    print("O texto tem mais de 10 caracteres")
    
# # # # #
# else  #
# # # # #
if True:
    print("Isso será impresso na tela")
else:
    print("Isso não será impresso na tela")
    
# if com texto
texto = input("Digite um texto: ")
if texto == "python":
    print("Você digitou 'python'")
else:
    print("Você não digitou 'python'")
    
# if com numero
numero = int(input("Digite um número: "))
if numero > 10:
    print("O número é maior que 10")
else:
    print("O número não é maior que 10")
    
# # # # #
# elif  #
# # # # #
numero = int(input("Digite um número: "))
if numero > 10:
    print("O número é maior que 10")
elif numero > 20:
    print("O número é maior que 20")
else:
    print("O número não é maior que 10 nem que 20")
