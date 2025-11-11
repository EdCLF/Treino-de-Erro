#Sistema de controle de mecanica

contagem= {'nome':'joao','veiculo':'ford k','servico':'lataria'}
chave =0

while True:
    try:
        def registra_veiculo():
            while True:
                nome = input("digite o nome do proprietario: ")
                veiculo = input("digite o veiculo: ")
                servico = input("digite o servico: ")
                contagem[f'{'nome'+str(chave+1)}']=[nome]
                contagem[f'{'veiculo'+str(chave+1)}']=[veiculo]
                contagem[f'{'servico' + str(chave + 1)}'] = [servico]
                para = input('deseja registrar mais algum carro (s/n): ')
                if para == "n":
                    break
                else:
                    continue
        def listar_veiculos():
            print(contagem)
    except TypeError:
        print("Erro de tipo de dados")
    except ValueError:
        print("Erro de valor de dados")
    finally:
        print('ola')
        registra_veiculo()
        listar_veiculos()
        break