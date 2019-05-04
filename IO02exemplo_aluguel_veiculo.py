nome = input('Digite seu nome: ')

dia_atual  = int(input('Digite o dia atual: '))
mes_atual = int(input('Digite o mês atual: '))
ano_atual = int(input('Digite o ano atual: '))

dias_aluguel = int(input('Digite a quantidade de dias de aluguel: '))

mes_adicional = (dia_atual + dias_aluguel)//31
ano_adicional = (mes_atual//12)

dia_entrega = (dia_atual + dias_aluguel)%30
mes_entrega = (mes_adicional + mes_atual)%12
ano_entrega = ano_atual + ano_adicional


print('''
Nome: {}
Data de entrega do veículo: {}/{}/{}.
'''.format(nome, dia_entrega, mes_entrega, ano_entrega))
