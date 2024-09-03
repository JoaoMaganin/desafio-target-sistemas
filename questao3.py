import json


def carregar_dados(caminho_arquivo):
    file = open(caminho_arquivo, 'r')
    return json.load(file)


def calcular_faturamento(dados):
    for item in dados['faturamento_diario']:
        if item['faturamento'] > 0:
            faturamento_diario[item] = item['faturamento']

    faturamento_diario = [item['faturamento'] for item in dados['faturamento_diario'] if item['faturamento'] > 0]

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    dias_acima_media = len([f for f in faturamento_diario if f > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_media


caminho_arquivo = './questao3.json'
dados = carregar_dados(caminho_arquivo)
menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(dados)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
