from livro import Livro


def menu():
    op = int(input('MENU\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   '1 - CADASTRO\n'
                   '2 - MOSTRAR TUDO \n'
                   '3 - ATUALIZAR\n'
                   '4 - DELETAR \n'
                   '5 - BUSCAR UM\n'
                   '6 - SAIR\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   'DIGITE A OPÇÃO DESEJADA: '))
    return op

l = Livro()

while True:

    op = menu()

    if op == 1:
        print('CADASTRAR!')
        autor = input("Digite o autor: ")
        tipo = input("Digite o tipo: ")

        l.cadastrar(autor, tipo)

    elif op == 2:
        print('Mostrar TUDO!')

        l.mostrar_tudo()

    elif op == 3:
        print('Editar')
        editar = input("Digite o ID do autor para editar: ")
        autor = input("Digite novo nome do autor: ")
        tipo = input("Digite o novo tipo: ")

        l.atualizar(editar, autor, tipo)

    elif op == 4:
        print('Deletar')
        delete = input("Digite o ID do autor para deletar: ")

        l.deletar(delete)

    elif op == 5:
        print('Find One')
        find = int(input("Digite o ID: "))
        l.find_one(find)

    elif op == 6:
        print("Finalizando...")
        break

    else:
        print(f'Opção inválida. Tente novamente!')
print("FIM!")
