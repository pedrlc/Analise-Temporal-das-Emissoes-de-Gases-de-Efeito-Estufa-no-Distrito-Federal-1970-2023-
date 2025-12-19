import pandas as pd

df = pd.read_csv('TabelaSalarial.csv',sep=',',encoding='utf-8-sig')


print("Colunas do DataFrame:")

print(df.columns.tolist()) # imprime os nomes das colunas

#['N,Estado Civil,Grau de Instrução,N de Filhos,Salario (x Sal Min),Idade (em anos),Região de Procedência']

print(df[["Idade (em anos)", "Salario (x Sal Min)", "N de Filhos"]].describe()) # imprime as colunas Idade, Salario e N de Filhos

#               Idade (em anos)  Salario (x Sal Min)  N de Filhos
#   count        36.000000            36.000000    20.000000
#   mean         34.583333            11.122222     1.650000
#   std           6.737422             4.587458     1.268028
#   min          20.000000             4.000000     0.000000
#   25%          30.000000             7.552500     1.000000
#   50%          34.500000            10.165000     2.000000
#   75%          40.000000            14.060000     2.000000
#   max          48.000000            23.300000     5.000000

print("\n\n")

print(df["Grau de Instrução"].describe()) # imprime a contagem dos valores únicos na coluna Grau de Instrução

# Graud de Instrução e Região de Procedência são colunas categóricas, por isso o describe() não mostra as estatísticas descritivas como média, desvio padrão, etc.
# para incluir colunas categóricas no describe(), podemos usar o parâmetro include='object'

print(df[["Grau de Instrução", "Região de Procedência"]].describe(include='object')) 
print("\n\n")

print(df.describe(include='all')) # imprime as estatísticas descritivas de todas as colunas, incluindo categóricas

               # N Estado Civil Grau de Instrução  N de Filhos  Salario (x Sal Min)  Idade (em anos) Região de Procedência
#   count   36.000000           36                36    20.000000            36.000000        36.000000                    36
#   unique        NaN            2                 3          NaN                  NaN              NaN                     3
#   top           NaN       casado      ensino médio          NaN                  NaN              NaN                 outra
#   freq          NaN           20                18          NaN                  NaN              NaN                    13
#   mean    18.500000          NaN               NaN     1.650000            11.122222        34.583333                   NaN
#   std     10.535654          NaN               NaN     1.268028             4.587458         6.737422                   NaN
#   min      1.000000          NaN               NaN     0.000000             4.000000        20.000000                   NaN
#   25%      9.750000          NaN               NaN     1.000000             7.552500        30.000000                   NaN
#   50%     18.500000          NaN               NaN     2.000000            10.165000        34.500000                   NaN
#   75%     27.250000          NaN               NaN     2.000000            14.060000        40.000000                   NaN
#   max     36.000000          NaN               NaN     5.000000            23.300000        48.000000                   NaN

 # lista com os nomes das colunas
# cols faz uma lista com os nomes das colunas

print(df.dtypes)
#   N                          int64
#   Estado Civil              object
#   Grau de Instrução         object
#   N de Filhos              float64
#   Salario (x Sal Min)      float64
#   Idade (em anos)            int64
#   Região de Procedência     object
#   dtype: object


cols = df.columns.tolist() # lista com os nomes das colunas
cols_num = df.select_dtypes(include=['int64', 'float64']).columns.tolist() # lista com os nomes das colunas numéricas
cols_all = df.select_dtypes(include=['object', 'int64', 'float64']).columns.tolist() # lista com os nomes de todas as colunas (numéricas e categóricas)

print("\n\n")
print("Moda das colunas:")
print(df[cols_all].mode().iloc[0]) # moda de todas as colunas inlcuvisive categóricas

#   iloc mostra a primeira linha do resultado do mode(), que é a moda

print("\n\n")
print("Mediana das colunas:")
print(df[cols_num].median()) # mediana das colunas numéricas
print("\n\n")
# Não tem como ter valor "object" na mediana, por isso só usamos cols_num, apenas colunas numéricas

print("Média de todos os valores númericos:")
print(df[cols_num].mean())