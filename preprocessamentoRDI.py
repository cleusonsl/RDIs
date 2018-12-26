# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 19:54:58 2018

@author: cleus
"""

import pandas as pd
incidentes = pd.read_csv('todos.csv')#lendo o arquivo
from datetime import date
incidentes.describe()#criando o dataframe
incidentes['Hora de Abertura'] = pd.to_datetime(incidentes['Hora de Abertura'])
incidentes['Hora de Resolução'] = pd.to_datetime(incidentes['Hora de Resolução'])

#recebe os incidentes em que o campo 'Ferramenta de Monitoração' recebeu valor nulo
reclamacao = incidentes.loc[pd.isnull(incidentes['Ferramenta de Monitoração'])]

#Recebe os incidentes em que foi localizado o padrão de string 'eploy' no campo 'Título'
deploys = incidentes.loc[incidentes['Título'].str.contains ('eploy')]
deploys_resolvidos = deploys.loc[pd.notnull(deploys['Hora de Resolução'] )]
pd.value_counts (deploys['Ambiente Incidente'])
deploys.to_html('deploys.htm')
import matplotlib.pyplot as plt

labels = 'DESENV', 'HOMOLO', 'PROD'
plt.pie(pd.value_counts (deploys['Ambiente Incidente']),labels=labels,autopct='%1.1f%%')

plt.scatter(incidentes['Hora de Abertura'].datetime., incidentes['Hora de Abertura'].hours)

plt.show()