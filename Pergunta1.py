'''
Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
'''

indice = 13
soma = 0
contador = 0

while contador < indice:
     contador += 1
     soma = soma + contador
# Saída 91
print(soma)