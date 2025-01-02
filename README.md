# Projeto de Pipeline de Engenharia de Dados: Fusão de Empresas

## Visão Geral do Projeto

Este projeto simula a fusão de duas grandes empresas, cada uma com bases de dados separadas e estruturas diferentes. O objetivo principal é construir um pipeline de dados que extrai, transforma e carrega os dados dessas duas fontes, permitindo a geração de relatórios para análise do impacto da fusão. O foco da análise será avaliar o comportamento das vendas, respondendo perguntas como:

- **As vendas aumentaram, diminuíram ou estão concentradas em uma das empresas?**

Além disso, será criado um dashboard interativo no **Power BI** para visualizar esses dados.

O pipeline de dados será desenvolvido de forma reutilizável, permitindo que seja facilmente adaptado e utilizado nos meses seguintes para atualizar e gerar relatórios sobre a evolução da fusão e do desempenho das vendas.

## Detalhes do Projeto

### Contexto

- **Cenário da fusão:** Duas empresas com bases de dados diferentes se fundiram e agora precisam gerar um relatório para entender os resultados dessa fusão.
- **Dados das empresas:** Cada empresa possui uma estrutura de dados distinta, o que exigirá transformações antes da análise.
- **Objetivo:** A equipe de Business Intelligence (BI) e Analytics precisa desses dados transformados e integrados para responder perguntas cruciais, como:
  - **As vendas aumentaram ou diminuíram?**
  - **As vendas estão concentradas na Empresa A ou na Empresa B?**

### Funções da Equipe de Desenvolvedores de Dados

A equipe de desenvolvedores de dados será responsável por:

1. **Integrar os dados:**
   - Extrair dados das duas bases de dados diferentes (MongoDB Atlas e PostgreSQL).
   - Transformar os dados para um formato consistente e carregá-los em uma estrutura unificada.

2. **Desenvolver o pipeline:**
   - Construir o pipeline de **ETL (Extração, Transformação e Carga)** para garantir que o processo de integração de dados seja feito de maneira automatizada e reutilizável.
   - O pipeline será desenhado para ser reaplicado em novos períodos, garantindo a atualização e geração de relatórios mensais sobre o desempenho das vendas.

3. **Gerar Relatórios:**
   - Transformar os dados integrados em insights que podem ser utilizados pelas equipes de BI e Analytics para tomar decisões informadas sobre o impacto da fusão nas vendas.

4. **Reusabilidade:**
   - Criar um pipeline que possa ser facilmente reaplicado para novos períodos, permitindo a atualização dos dados mensalmente, sem necessidade de reconfiguração significativa.

### Armazenamento de Dados

Os dados serão armazenados em duas plataformas diferentes, dependendo da estrutura de dados de cada empresa:

- **MongoDB Atlas:** Utilizado para armazenar dados em formato não relacional (NoSQL), oferecendo alta escalabilidade e flexibilidade.
- **PostgreSQL:** Usado para armazenar dados estruturados (SQL), garantindo integridade e confiabilidade para consultas analíticas.

## Tecnologias Utilizadas

- **MongoDB Atlas:** Armazenamento de dados NoSQL
- **PostgreSQL:** Armazenamento de dados SQL
- **Python:** Desenvolvimento do pipeline ETL

## Como Usar

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/seu_usuario/fusao-empresas.git

