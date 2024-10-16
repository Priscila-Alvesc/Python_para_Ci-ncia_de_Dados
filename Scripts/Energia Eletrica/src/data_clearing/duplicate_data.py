#Modulos py fazem operações especificaspara tratamento de dados
#São arquivos que estão dentro de um pacote pythom

import pandas as pd

#Criando uma função para contar os dados duplicados 
def count_duplicates(dataframe: pd.DataFrame):
    duplicados = dataframe.duplicated().sum()
    print(f'foram encontrdos {duplicados} ddos duplicados')

    
    