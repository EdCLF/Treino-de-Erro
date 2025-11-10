"""
diaria = 300
se tiver menos de 15 dias taxa = 20
se igual taxa = 14
se mais taxa = 12
"""
hosp = []
diaria = []
while True:
    try:
        def cadastro():
            for i in range(1):
                while True:
                    nome = input("digite o nome do hospede: ")
                    if nome not in hosp:
                        hosp.append(nome)
                        diaria.append(int(input("digite a quantidade de dias: ")))
                        break
                    else:
                        print("nome ja existente\n")
        def pesquisa():
            procura = str(input("digite o nome do hospede: "))
            if procura in hosp:
                indice_nome = hosp.index(procura)
                print(f"O hospede {procura} se hospedou por {diaria[indice_nome]}\n")
                def taxa():
                    total = diaria[indice_nome] * 300
                    if diaria[indice_nome]< 15:
                        total = total + 20
                    elif diaria[indice_nome] == 15:
                        total = total + 14
                    else:
                        total = total + 12
                    return total
                print(f'E seu total para pagamente é de {taxa()}\n')
            else:
                print("Nome não encontrado\n")
                des= input("deseja cadastrar este hospede?(s/n): ")
                if des == "s":
                    cadastro()
                else:
                    print("ok")
    except ValueError:
        print("digite um numero valido")
    except TypeError:
        print("Tipo errado")
    finally:
        print(f"""{'='*30}Olá{'='*30}
    Bem vindo a hotel to com sono!
    começaremos a logica= 
""")
        menu = input("""O que voce deseja fazer:
        1 - cadastrar hospede
        2 - pesquisa
        3 - sair do programa: """)
        if menu == "1":
            cadastro()
        elif menu == "2":
            pesquisa()
        elif menu == "3":
            break
        else:
            print("Opção invalida\n")
