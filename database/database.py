import os
import csv
import psycopg2
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decimal import Decimal

def criar_banco_postgresql():
    try:
        conn = psycopg2.connect(
            database="postgres",
            host="localhost",
            user="postgres",
            password="Ste@14725369",
            port="5432"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'pipeline_vendas';")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute("CREATE DATABASE pipeline_vendas;")
            print("Banco de dados criado com sucesso!")
        else:
            print("Banco de dados já existe.")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")

def criar_tabela_postgresql():
    try:
        conn = psycopg2.connect(
            database="pipeline_vendas",
            host="localhost",
            user="postgres",
            password="Ste@14725369",
            port="5432"
        )
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_combinados (
            id SERIAL PRIMARY KEY,
            nome_do_produto VARCHAR(255) NOT NULL,
            categoria_do_produto VARCHAR(255) NOT NULL,
            preco_do_produto DECIMAL(10, 2) NOT NULL,
            quantidade_em_estoque INT NOT NULL,
            filial VARCHAR(255) NOT NULL
        );
        """)
        
        print("Tabela criada com sucesso!")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def carregar_dados_csv_para_postgresql(path_csv):
    try:
        conn = psycopg2.connect(
            database="pipeline_vendas",
            host="localhost",
            user="postgres",
            password="Ste@14725369",
            port="5432"
        )
        cursor = conn.cursor()

        with open(path_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute("""
                INSERT INTO dados_combinados (nome_do_produto, categoria_do_produto, preco_do_produto, quantidade_em_estoque, filial)
                VALUES (%s, %s, %s, %s, %s)
                """, (
                    row['Nome do Produto'],
                    row['Categoria do Produto'],
                    row['Preço do Produto (R$)'],
                    row['Quantidade em Estoque'],
                    row['Filial']
                ))

        conn.commit()
        cursor.close()
        conn.close()
        
        print("Dados do CSV carregados com sucesso para o PostgreSQL!")
        
    except Exception as e:
        print(f"Erro ao carregar dados do CSV para o PostgreSQL: {e}")

def extrair_dados_postgresql():
    try:
        conn = psycopg2.connect(
            database="pipeline_vendas",
            host="localhost",
            user="postgres",
            password="Ste@14725369",
            port="5432"
        )
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM dados_combinados")
        rows = cursor.fetchall()

        colunas = [desc[0] for desc in cursor.description]
        
        dados = [dict(zip(colunas, row)) for row in rows]
        
        cursor.close()
        conn.close()
        
        return dados
    except Exception as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return []

def converter_decimais_para_float(dados):
    for item in dados:
        for chave, valor in item.items():
            if isinstance(valor, Decimal):
                item[chave] = float(valor)
    return dados

def salvar_no_mongodb(dados, uri, database, collection):
    if not dados:
        print("Erro ao salvar dados no MongoDB: lista de documentos vazia")
        return

    dados_convertidos = converter_decimais_para_float(dados)

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[database]
    col = db[collection]
    
    try:
        col.insert_many(dados_convertidos)
        print("Dados salvos com sucesso no MongoDB!")
    except Exception as e:
        print(f"Erro ao salvar dados no MongoDB: {e}")

path_csv = 'data_processed/dados_combinados.csv'

criar_banco_postgresql()
criar_tabela_postgresql()
carregar_dados_csv_para_postgresql(path_csv)

uri = "mongodb+srv://borzistephany18:12345@cluster0.y5v9e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
dados_postgresql = extrair_dados_postgresql()
salvar_no_mongodb(dados_postgresql, uri, 'pipeline_vendas', 'dados_combinados')
