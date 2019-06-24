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
        ## TODO: carregar
        """
        inserir atraves de um Arquivo
        """
    elif opcao == 4:
        ## TODO: exibir
        """
        lista em ordem
        """
    elif opcao == 5:
        ## TODO: finalizar
        """
        passar pra proxima etapa: candidatos
        """
