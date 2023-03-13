'''
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''
def inverte_strings(frase):
    return frase[::-1]

frase = str(input('Digite um texto, que eu inverterei as palavras: '))
print(inverte_strings(frase))