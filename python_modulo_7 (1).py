# -*- coding: utf-8 -*-
"""Python_modulo_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cBWcMvOyrdHcdUwg-dU-fqSamknlO0sA

<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo 07** | Python: Programação Orientada a Objetos
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>from / import / as;</li>
  <li>Módulo;</li>
  <li>Pacote;</li>
  <li>Baixando pacotes.</li>
</ol>

---

# **Exercícios**

## 0\. Preparação do ambiente

Neste exercício vamos utilizar a base de dados de ações da bolsa de valores dos EUA, a Dow Jones. Os dados estão disponíveis para *download* neste [link](https://archive.ics.uci.edu/ml/datasets/Dow+Jones+Index). Vamos utilizar o pacote `wget` para fazer o *download* dos dados.

- Instalando o pacote `wget` na versão 3.2.
"""

!pip install wget==3.2

""" - Fazendo o download dos dados no arquivo compactado `dados.zip`."""

import wget

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')

""" - Descompactando os `dados` na pasta dados com o pacote nativo `zipfile`."""

import zipfile

with zipfile.ZipFile('./dados.zip', 'r') as fp:
  fp.extractall('./dados')

"""Verifique a pasta dados criada, ela deve conter dois arquivos:

 - **dow_jones_index.data**: um arquivo com os dados;
 - **dow_jones_index.names**: um arquivo com a descrição completa dos dados.

É possível observar que o arquivo de dados é um arquivo separado por virgulas, o famoso `csv`. Vamos renomear o arquivo de dados para que ele tenha a extensão `csv` com o pacote nativo `os`.

- Renomeando o arquivo com o pacote nativo `os`.
"""

import os

os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')

"""Pronto! Abra o arquivo e o Google Colab irá apresentar uma visualização bem legal dos dados.

---

## 1\. Pandas

Para processar os dados, vamos utilizar o pacote `pandas` na versão `1.1.5`. A documentação completa por ser encontrada neste [link](https://pandas.pydata.org/docs/)
"""

!pip install pandas==1.1.5

"""Vamos importar o pacote com o apelido (alias) `pd`."""

import pandas as pd

"""Estamos prontos para ler o arquivo."""

df = pd.read_csv('./dados/dow_jones_index.csv')

"""O pandas trabalha com o conceito de dataframe, uma estrutura de dados com muitos métodos e atributos que aceleram o processamento de dados. Alguns exemplos:

- Visualizando as `n` primeiras linhas:
"""

df.head(n=10)

""" - Visualizando o nome das colunas:"""

df.columns.to_list()

""" - Verificando o número de linhas e colunas."""

linhas, colunas = df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')

"""Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações do McDonalds, listado na Dow Jones como MCD:

- Selecionando as linha do dataframe original `df` em que a coluna `stock` é igual a `MCD`.
"""

df_mcd = df[df['stock'] == 'MCD']

""" - Selecionando apenas as colunas de data e valores de ações."""

df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]

"""Excelente, o problema é que as colunas com os valores possuem o carater `$` e são do tipo texto (`object` no `pandas`)."""

df_mcd.head(n=10)

df_mcd.dtypes

"""Vamos limpar as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` remove o caracter **$** e faz a conversão do tipo de `str` para `float`."""

for col in ['open', 'high', 'low', 'close']:
  df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))

"""Verifique novamente os dados e seus tipos."""

df_mcd.head(n=10)

df_mcd.dtypes

"""Excelente, agora podemos explorar os dados visualmente.

**Agora é a sua vez!** Conduza o mesmo processo para extrair e tratar os dados da empresa Coca-Cola (`stock` column igual a `KO`).
"""

# extração e tratamento dos dados da empresa Coca-Cola.
df_ko = df[df['stock'] == 'KO']
df_ko = df_ko[['date', 'open', 'high', 'low', 'close']]
for col in ['open', 'high', 'low', 'close']:
  df_ko[col] = df_ko[col].apply(lambda value: float(value.split(sep='$')[-1]))
df_ko.head(n=10)

"""---

## 2\. Seaborn

Para visualizar os dados, vamos utilizar o pacote `seaborn` na versão `0.11.1`. A documentação completa por ser encontrada neste [link](https://seaborn.pydata.org/)
"""

!pip install seaborn==0.11.1

"""Vamos importar o pacote com o apelido (alias) `sns`."""

import seaborn as sns

"""Vamos visualizar o os valores de abertura das ações ao longo do tempo."""

plot = sns.lineplot(x="date", y="open", data=df_mcd)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)

"""Vamos também visualizar o os valores de fechamento das ações ao longo do tempo."""

plot = sns.lineplot(x="date", y="close", data=df_mcd)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)

"""Para facilitar a comparação, vamos visualizar os quatro valores no mesmo gráfico."""

plot = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_mcd, ['date']))
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)

"""Para finalizar, vamos salvar o gráfico numa figura."""

plot.figure.savefig("./mcd.png")

"""**Agora é a sua vez,** faça o gráfico acima para a empresa Coca-Cola e salve a imagem com o nome `ko.png`."""

#Grafico de abertura Coca-Cola


plot_ko = sns.lineplot(x="date", y="open", data=df_ko)
_ = plot_ko.set_xticklabels(labels=df_ko['date'], rotation=90)

#Gráfico de fechamento da Coca-cola:

plot_ko = sns.lineplot(x="date", y="close", data=df_ko)
_ = plot_ko.set_xticklabels(labels=df_ko['date'], rotation=90)

# visualização dos dados da Coca-Cola.

plot_ko = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_ko, ['date']))
_ = plot_ko.set_xticklabels(labels=df_ko['date'], rotation=90)
plot_ko.figure.savefig("./ko.png")

"""Analise as duas imagens e escreva pelo menos um *insight* que você consegue extrair dos dados. Fique a vontade para escrever quantos *insights* você quiser."""

menor_fechamento_mcd = df_mcd.close.min()
menor_fechamento_ko = df_ko.close.min()
maior_fechamento_mcd = df_mcd.close.max()
maior_fechamento_ko = df_ko.close.max()

print(f'Menor fechamento da McDonalds foi de {menor_fechamento_mcd} e maior fechamento foi de {maior_fechamento_mcd}')
print(f'Menor fechamento da Coca-Cola foi de {menor_fechamento_ko} e maior fechamento foi de {maior_fechamento_ko}')

"""**Insight's McDonalds**:


*   Observando o primeiro semestre das acoes da McDonalds, podemos analisar um crescimento de aproximadamente 10%.
*   Seu maior fechamento foi no dia 17/06 no valor de 82,52.
*   Seu fechamento com menor baixa ocorreu em 18/03, fechando a 72,99.

**Insight's Coca-Cola**:


*   Observando o primeiro semestre das acoes da Coca-Cola, podemos analisar um crescimento de aproximadamente 3%.
*   Seu maior fechamento foi no dia 20/05 no valor de 68,30.
*   Seu fechamento com menor baixa ocorreu em 28/01, fechando a 62,21.


Ambas as empresas tiveram crescimento no primeiro semestre de 2011.

---
"""