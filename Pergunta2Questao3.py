'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

arquivo = open('dados.json')
dados = json.load(arquivo)

quantidade = 0
valores = []

for dado in dados:
  if dado["valor"] != 0.0:
    valores.append(dado["valor"])
    quantidade += 1

total = sum(valores)
valores.sort()
media = (total / quantidade)

maior_dias = 0

for dado in dados:
  if dado["valor"] > media:
    maior_dias += 1


print(f'Menor valor ocorrido dentro do mês R${valores[0]:.2f}')
print(f'Maior valor ocorrido dentro do mês R${valores[-1]:.2f}')
print(f'Média mensal de faturamento R${media:.2f}')
print(f'O número de dias no mês em que o faturamento foi maior que a média mensal foi de {maior_dias} dias.')


arquivo.close()





