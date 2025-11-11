#Sistema de controle de mecanica

servicos= {'servico':'lataria'}
veiculo={'veiculo':'ford k'}
dono={'nome':'joao'}
chave =0

while True:
    try:
        def registra_veiculo():
            while True:
                nome = input("digite o nome do proprietario: ")
                veiculo = input("digite o veiculo: ")
                servico = input("digite o servico: ")
                dono[f'{'nome'+str(chave+1)}']=[nome]
                veiculo[f'{'veiculo'+str(chave+1)}']=[veiculo]
                servicos[f'{'servico' + str(chave + 1)}'] = [servico]
                para = input('deseja registrar mais algum carro (s/n): ')
                if para == "n":
                    break
                else:
                    continue
        def listar_veiculos():
            print(veiculo)
    except TypeError:
        print("Erro de tipo de dados")
    except ValueError:
        print("Erro de valor de dados")
    finally:
        print('ola')
        registra_veiculo()
        listar_veiculos()
        break