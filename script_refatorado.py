import os
import json
import csv
from processamento_dados import Dados

def get_columns(dados):
    return list(dados[0].keys()) if dados and isinstance(dados[0], dict) else []

def rename_columns(dados, key_mapping):
    new_dados_csv = []
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            new_key = key_mapping.get(old_key, old_key)
            dict_temp[new_key] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv

def size_data(dados):
    return len(dados)

def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponível'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def salvando_dados(dados, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

# Caminhos dos arquivos
path_json = 'dados_empresaA (1).json'
path_csv = 'dados_empresaB (1).csv'

# Extração de dados
dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

print("Colunas JSON:", dados_empresaA.nome_colunas)
print("Colunas CSV:", dados_empresaB.nome_colunas)

# Transformação de dados
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print("Colunas renomeadas CSV:", dados_empresaB.nome_colunas)

# Combinação de dados
dados_fusao = join(dados_empresaA.dados, dados_empresaB.dados)
nome_colunas_fusao = get_columns(dados_fusao)
print("Colunas combinadas:", nome_colunas_fusao)
print("Tamanho da fusão:", size_data(dados_fusao))

# Salvamento dos dados combinados
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)
path_dados_combinados = 'data_processed/dados_combinados.csv'
salvando_dados(dados_fusao_tabela, path_dados_combinados)
print(f"Dados combinados salvos em: {path_dados_combinados}")
