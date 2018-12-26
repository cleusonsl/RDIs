# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:59:31 2018

@author: cleus
"""

import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()
base.loc[base['age'] < 0]

#apaga toda a coluna 'age' 
#base.drop('age', 1, inplace= True)

#apaga os registros com idade menor do que 0
#base.drop(base[base.age < 0].index, inplace = True)

#preencher usando a média
#base.mean()
#base['age'].mean()
#base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92 #49.92 é media das idades

#localiza valores nulos (NaN)para o campo "age"
base.loc[pd.isnull(base['age'])]

#divide colunas de previsores e classes em variáveis diferentes
previsores = base.iloc[:,1:4].values
classe = base.iloc[:, 4].values

#Transforma os valores 'NaN' em valor médio para o campo age
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN',strategy='mean',axis=0) 
imputer = imputer.fit(previsores[:,0:3])
previsores = imputer.transform(previsores[:, 0:3])


#deixando os valores na mesma escala
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

