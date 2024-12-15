import json
import csv
import os

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.__leitura_dados()
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    def __leitura_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def __leitura_csv(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def __leitura_dados(self):
        if self.tipo_dados == 'csv':
            return self.__leitura_csv()
        elif self.tipo_dados == 'json':
            return self.__leitura_json()
        elif isinstance(self.path, list):  # Suporte para lista em memória
            return self.path
        else:
            raise ValueError("Tipo de dados não suportado. Use 'csv', 'json' ou uma lista.")

    def __get_columns(self):
        if self.dados and isinstance(self.dados, list) and isinstance(self.dados[0], dict):
            return list(self.dados[0].keys())
        return []

    def __size_data(self):
        return len(self.dados)

    def rename_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                new_key = key_mapping.get(old_key, old_key)
                dict_temp[new_key] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()

    @staticmethod
    def join(dadosA, dadosB):
        combined_list = dadosA.dados + dadosB.dados
        return Dados(combined_list, 'list')

    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela

    def salvando_dados(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        dados_combinados_tabela = self.__transformando_dados_tabela()
        with open(path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
