import time
import numpy as np

portfolio = {1:{'Fiat Uno 1.0 ': {'preco': 50, 'Ano': 2015, 'lugares': 5}},
             2:{'Palio 1.0 ': {'preco': 80, 'Ano': 2016, 'lugares': 5}},
             3:{'Onix 1.0 ': {'preco': 100, 'Ano': 2020, 'lugares': 5}},
             4:{'Prisma Sedan ': {'preco': 200, 'Ano': 2022, 'lugares': 5}},
             5:{'Cruze 2.0 ': {'preco': 350, 'Ano': 2021, 'lugares': 5}},
             6:{'Corolla XEI 2.0 ': {'preco': 450, 'Ano': 2022, 'lugares': 5}},
             7:{'Hilux 3.0 SW4': {'preco': 800, 'Ano': 2023, 'lugares': 8}},
             8:{'Fiat Strada 1.4': {'preco': 370, 'Ano': 2012, 'lugares': 5}},}
carros_info = {1:{'Fiat Uno 1.0 ': {'preco': 50, 'Ano': 2015, 'lugares': 5}},
             2:{'Palio 1.0 ': {'preco': 80, 'Ano': 2016, 'lugares': 5}},
             3:{'Onix 1.0 ': {'preco': 100, 'Ano': 2020, 'lugares': 5}},
             4:{'Prisma Sedan ': {'preco': 200, 'Ano': 2022, 'lugares': 5}},
             5:{'Cruze 2.0 ': {'preco': 350, 'Ano': 2021, 'lugares': 5}},
             6:{'Corolla XEI 2.0 ': {'preco': 450, 'Ano': 2022, 'lugares': 5}},
             7:{'Hilux 3.0 SW4': {'preco': 800, 'Ano': 2023, 'lugares': 8}},
             8:{'Fiat Strada 1.4': {'preco': 370, 'Ano': 2012, 'lugares': 5}},}

alugados= {}

lucro = []

def mostrar():
    print('','='*32, f'\n Seja bem vindo a minha locadora!\n', '='*32,'\n\n','='*43 ,f'\n Estes são os carros disponíveis no momento.\n', '='*43)
    for idx, marca in portfolio.items():
        print('[{}] - {} - R$ {},00 / dia'.format(idx, list(marca.keys())[0], list(marca.values())[0]['preco']))
        
        
def mostrar_dev():
    print('','='*32,'\n Seja bem vindo a minha locadora!\n','='*32,'\n\n')
    for idx, marca in alugados.items():
        print('[{}] - {} - R$ {},00 / dia'.format(idx, list(marca.keys())[0], list(marca.values())[0]['preco']))
        
    

def alug():  
    print('\nQual carro deseja alugar?\n\nDigite o número que corresponda ao carro... ')
    alug_esc = int(input())
    time.sleep(0.3)
    valor_carro = list(list(portfolio[alug_esc].values())[0].values())[0] 
    print('Você escolheu o {a}, ele está custando R$ {b},00 / dia.\n\nPor quantos dias deseja alugar o {a}\n\n'.format(a = list(list(portfolio[alug_esc].keys()))[0], b=valor_carro))
    dias_alug = int(input())
    time.sleep(0.3)
    global lucro_oper
    lucro_oper = dias_alug * int(valor_carro)
    time.sleep(0.3)
    lucro.append(lucro_oper)
    if alug_esc in portfolio:
        alteração = portfolio.pop(alug_esc)
        alugados[alug_esc] = alteração
    print(f'Obrigado, você alugou o {list(alteração)[0]} por R${lucro_oper},00\n\n\n')
        

def devolucao():
    mostrar_dev()
    print('\nQual carro deseja Devolver?\n\nDigite o número que corresponda ao carro... ')
    dev_esc = int(input())
    if dev_esc in alugados:
        alteracaodev = alugados.pop(dev_esc)
        portfolio[dev_esc] = alteracaodev
        print('Obrigado, você devolveu o {}\n\n\n'.format(list(alteracaodev)[0]))
        

def erro():
    print('','='*60,'\n O valor digitado está inválido, reentre com valores aceitos.\n','='*60)

list_range = [x for x in range(0,8)]
def info():
    print('Sobre qual carro deseja informações?\n\nEscolha o número do carro desejado entre as opções abaixo...\n\n')
    time.sleep(1)
    print('','='*44 ,f'\n Estes são todos os nossos carros disponíveis.\n', '='*44,'\n')
    for idx, marca in carros_info.items():
        print('[{}] - {} - R$ {},00 / dia'.format(idx, list(marca.keys())[0], list(marca.values())[0]['preco']))
    esc_info = int(input()) - 1
    while esc_info in list_range:
            set_carros = list(carros_info.values())
            nome_carro = []
            ano_do_carro = []
            assentos = []
            nome_carro.append(list(list(carros_info.values())[esc_info])[0])
            ano_do_carro.append(set_carros[esc_info][nome_carro[0]]['Ano'])
            assentos.append(set_carros[esc_info][nome_carro[0]]['lugares'])
            time.sleep(0.5)
            print('\n','='*75,f'\n Voce escolheu o {nome_carro[0]} fabricado em {ano_do_carro[0]}, ele possui {assentos[0]} lugares.\n','='*75,'\n')
            time.sleep(2)
            print('\n','='*75,f'\n Você pode continuar buscando informações escolhendo outro número de carro...\n','='*75,'\n')
            print(' 0 - Sair')
            esc_info = int(input()) - 1
            time.sleep(0.5)
            continue

    


alpha = 0
while alpha == 0:
    try:
        mostrar()
        print('\n\n\nDigite a ação desejada.\n')
        print('0 - Sair | 1 - Alugar | 2 - Devolver | 3 - Informações | 4 - Custos')
        esc_prin = int(input())
        if esc_prin == 0:
            print('','='*48,'\n Obrigado por usar nossos serviços, volte sempre!\n','='*48)
            alpha +=1
            continue
        elif esc_prin == 1:
            alug()
            time.sleep(1)
            continue
        elif esc_prin == 2:
            devolucao()
            time.sleep(1)
            continue
        elif esc_prin ==3:
            info()
            time.sleep(1)
            continue
        elif esc_prin == 4:
            print(f'\n\n\n\n==========================================\nVocê gastou um valor total de R${sum(lucro)},00\n==========================================\n\n\n\n\n')
            time.sleep(1)
        else:
            erro()
            time.sleep(1)
            continue
        
        continue
        
        
        
        
        
    
    except Exception as e:
        erro()
        time.sleep(1)
        continue
