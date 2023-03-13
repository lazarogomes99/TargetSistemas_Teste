'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor
total mensal da distribuidora.
'''

sao_paulo = 67_836.43
riode_janeiro = 36_678.43
minas_gerais = 29_229.88
espirito_santo = 27_165.48
outros = 19_849.53
total_faturamento = (sao_paulo + riode_janeiro + minas_gerais + espirito_santo + outros )


def calcula_porcentagem(estado):
   return ((estado/total_faturamento)*100)

print(f'Faturamento total = R${total_faturamento:.2f}')
print(f'São Paulo - {calcula_porcentagem(sao_paulo):.2f}%')
print(f'Rio de Janeiro - {calcula_porcentagem(riode_janeiro):.2f}%')
print(f'Minas Gerais - {calcula_porcentagem(minas_gerais):.2f}%')
print(f'Espírito Santo - {calcula_porcentagem(espirito_santo):.2f}%')
print(f'Outros - {calcula_porcentagem(outros):.2f}%')

