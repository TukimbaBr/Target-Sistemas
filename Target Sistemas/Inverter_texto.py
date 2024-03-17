
texto = (str(input("Digite um texto: "))).strip().upper()

letras = texto.split()
junto = ''.join(texto)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

espaco = '''
'''
print(f'O inverso de {texto} é:{espaco}{inverso}')



