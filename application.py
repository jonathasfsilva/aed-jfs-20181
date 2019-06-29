import os
from data_structure import RedBlackTree


# ÁRVORE DE TÍTULOS
titulos = RedBlackTree.RBTree()
quantidade_cadastrada = 0

os.system('clear')
while True:
    opcao = int(input("Títulos Cadastrados: %d" % quantidade_cadastrada+'\n\n' +
                      "1 - Cadastrar título" + '\n' +
                      "2 - Descadastrar título" + '\n' +
                      "3 - Carregar de um arquivo" + '\n' +
                      "4 - Exibir títulos cadastrados" + '\n' + '\n'
                      "5 - Finaliza cadastro de títulos" + '\n' + '\n'
                      "Escolha: "))
    if opcao == 1:
        os.system('clear')
        titulos.insert(titulo.Titulo.cadastrar())
        quantidade_cadastrada += 1
    elif opcao == 2:
        os.system('clear')
        if not titulos.isEmpty():
            eliminar = titulos.search(titulo.Titulo.descadastrar())
            # quando um ítem não é encontrado a função search retorna 'nil'
            # para não apagar a folha é feita a verificação abaixo
            if eliminar is not titulos.nil:
                titulos.delete(eliminar)
                quantidade_cadastrada -= 1
            else:
                print('Titulo nao encontrado!')
        else:
            print('Árvore vazia!')
    elif opcao == 3:
        os.system('clear')
        try:
            arquivo = input('Nome do arquivo: ')
            with open(arquivo) as lista:
                for i in lista.readlines():
                    titulos.insert(titulo.Titulo(i[0:8], i[8:11], i[11:-1]))
                    quantidade_cadastrada += 1
            print('\n')
        except Exception as exc:
            print('\nArquivo não encontrado!\n')
    elif opcao == 4:
        os.system('clear')
        titulos.inOrderTreeWalk(titulos.getRoot())
        print('\n')
    elif opcao == 5:
        os.system('clear')
        break

# CADASTRAMENTO DE CANDIDATOS
while True:
    opcao = int(input("1 - Cadastrar canditado" + '\n' +
                      "2 - Deletar canditado" + '\n' +
                      "3 - Listar candidatos" + '\n' +
                      "4 - Finalizar cadastro de candidatos" + '\n' + '\n' +
                      "Escolha: "))

    if opcao == 1:  # cadastrar canditado
        os.system('clear')
        numero = int(input('Número: '))
        nome = input('Nome: ')
        candidatos[numero] = [nome, 0]
        numeros.append(numero)
    elif opcao == 2:  # Deletar candidato
        os.system('clear')
        numero = int(input('Digite o número a ser apagado: '))
        del candidatos[numero]
    elif opcao == 3:  # listar candidatos
        os.system('clear')
        for i in candidatos:
            print(i, '-', candidatos[i][0])
        print('\n')
    elif opcao == 4:  # encerrar o loop
        os.system('clear')
        break
