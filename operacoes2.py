from operator import itemgetter

palavras = ['amar', 'liderar','falar','abacaxi','xixi','chute']

#ordena a lista 'palavras' pela segunda letra
print(sorted(palavras, key=lambda string : string[1])) 
# ou..
print(sorted(palavras, key=itemgetter(1)))