import csv

def verificar_colunas_csv(path_csv):
    with open(path_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        colunas_csv = reader.fieldnames
        print("Nomes das colunas no CSV:", colunas_csv)

# Caminho do arquivo CSV
path_csv = 'data_processed/dados_combinados.csv'
verificar_colunas_csv(path_csv)
