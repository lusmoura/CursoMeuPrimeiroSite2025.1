# Sistema de Cadastro de Voos
# Este programa permite cadastrar, listar, buscar e remover voos de uma lista.
# O sistema armazena os dados dos voos em um dicionário e utiliza uma lista para gerenciar os voos cadastrados.

# Funções do sistema
# 1. cadastrar_voo: Cadastra um novo voo, verificando se o código já existe.
# 2. listar_voos: Lista todos os voos cadastrados.
# 3. buscar_por_destino: Busca voos por destino, permitindo ao usuário encontrar voos específicos.
# 4. remover_voo: Remove um voo pelo código, caso ele exista na lista.
# 5. Menu principal: Apresenta um menu para o usuário interagir com o sistema.

def cadastrar_voo(voos):
    codigo = input("Digite o código do voo: ")
    # Verificar se código já existe (não é obrigatório, mas é uma boa prática de programação)
    for voo in voos:
        if voo['codigo'] == codigo:
            print("Erro: Já existe um voo com esse código.")
            return 0
    destino = input("Digite o destino do voo: ")
    preco = float(input("Digite o preço da passagem: "))
    horario = input("Digite o horário de partida (ex: 14:30): ")

    novo_voo = {
        "codigo": codigo,
        "destino": destino,
        "preco": preco,
        "horario": horario
    }
    voos.append(novo_voo)
    print("Voo cadastrado com sucesso!")

def listar_voos(voos):
    if len(voos) == 0:
        print("Nenhum voo cadastrado.")
    else:
        print("\n--- Lista de Voos ---")
        for voo in voos:
            print(f"Código: {voo['codigo']} | Destino: {voo['destino']} | Preço: R${voo['preco']:.2f} | Horário: {voo['horario']}")

def buscar_por_destino(voos):
    destino_busca = input("Digite o destino para buscar: ")
    # Criando uma lista para armazenar os voos encontrados
    # Isso é útil para evitar a impressão de voos não encontrados
    encontrados = []
    for voo in voos:
        if voo['destino'].lower() == destino_busca.lower():
            encontrados.append(voo)

    if len(encontrados) == 0:
        print("Nenhum voo encontrado para esse destino.")
    else:
        print("\n--- Voos encontrados ---")
        for voo in encontrados:
            print(f"Código: {voo['codigo']} | Preço: R${voo['preco']:.2f} | Horário: {voo['horario']}")

def remover_voo(voos):
    codigo_remover = input("Digite o código do voo a ser removido: ")
    for voo in voos:
        if voo['codigo'] == codigo_remover:
            voos.remove(voo)
            print("Voo removido com sucesso!")
            return
    print("Voo não encontrado.")

voos = []
while True:
    print("\n--- Planejador de Voos ---")
    print("1. Cadastrar novo voo")
    print("2. Listar todos os voos")
    print("3. Buscar voos por destino")
    print("4. Remover voo pelo código")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_voo(voos)
    elif opcao == "2":
        listar_voos(voos)
    elif opcao == "3":
        buscar_por_destino(voos)
    elif opcao == "4":
        remover_voo(voos)
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
