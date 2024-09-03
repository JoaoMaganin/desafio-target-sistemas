faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

percentual_representacao = {}
for estado, valor in faturamento.items():
    percentual_representacao[estado] = (valor / total_faturamento) * 100

print(f'Faturamento Total: R${total_faturamento:.2f}\n')
for estado in percentual_representacao:
    percentual = percentual_representacao[estado]
    print(f'{estado}: {percentual:.2f}%')
