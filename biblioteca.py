#Sistema de controle de biblioteca comunitaria

livro = ['expresso','restou 1']
reservado = ['restou 1']

while True:
    try:
        def adiciona_livro():
            while True:
                qual = input("digite o nome do livro: ")
                if qual not in livro:
                        livro.append(qual)
                else:
                    print("Livro já existe")
                parar = input("deseja cadastrar mais algum livro (s/n): ")
                if parar == "n":
                    break
                else:
                    continue
        def emprestar_livro():
            while True:
                nome = input("digite o nome do livro: ")
                existe = sorted(livro) == sorted(reservado)
                if existe == True:
                    print("Não ha livros disponiveis")
                    break
                elif nome not in reservado:
                    reservado.append(nome)
                else:
                    print("Livro alredy reserved")
                parar = input("deseja reservar mais algum livro (s/n): ")
                if parar == "n":
                    break
                else:
                    continue
        def devolver_livro():
            while True:
                nome = input("digite o nome do livro: ")
                if nome in reservado:
                    reservado.remove(nome)
                else:
                    print("Not in the list")
                parar = input("deseja devolver mais algum livro (s/n): ")
                if parar == "n":
                    break
                else:
                    continue
        def listar_livro():
            lista_livro = set(livro) - set(reservado)
            print(lista_livro)
        def busca_livro():
            while True:
                nome = input("digite o nome do livro: ")
                if nome in reservado:
                    print(f"O livro {nome} esta reservado no momento")
                elif nome in livro and nome not in reservado:
                    print(f"O livro {nome} esta disponivel no momento")
                else:
                    print(f"O livro {nome} não foi encontrado")
                para = input('deseja buscar mais algum livro (s/n): ')
                if para == "n":
                    break
                else:
                    continue

    except ValueError:
        print("Valor invalido")
    except TypeError:
        print("Tipo invalido")
    finally:
        print(f"""{'=' * 30}Olá{'=' * 30}
            Bem vindo a biblioteca soninho!
                =começaremos a logica= 
        """)
        menu = input("""O que voce deseja fazer:
                1 - cadastrar livro
                2 - emprestar livro
                3 - devolver livro
                4 - listar livro
                5 - buscar livro
                6 - sair do programa: """)
        if menu == "1":
            adiciona_livro()
        elif menu == "2":
            emprestar_livro()
        elif menu == "3":
            devolver_livro()
        elif menu == "4":
            listar_livro()
        elif menu == "5":
            busca_livro()
        elif menu == "6":
            break
        else:
            print("Opção invalida\n")