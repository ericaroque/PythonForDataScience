
# coding: utf-8

# # Exercício Mapas Choropleth  
# 
# Bem-vindo aos exercícios sobre mapas do Choropleth! Neste exercício, daremos alguns conjuntos de dados simples e pedimos que você crie o mapa a partir deles. Devido à natureza do Plotly, não podemos mostrar exemplos
# 
# [Documentação](https://plot.ly/python/reference/#choropleth)
# 
# ## Imports Plotly 

# In[1]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# ** Importe pandas e leia o arquivo csv: 2014_World_Power_Consumption **

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('2014_World_Power_Consumption')


# ** Verifique o cabeçalho do DataFrame. **

# In[5]:


df.head()


# ** Consultando as notas de aula, crie um plot de Choropleth do consumo de energia para países usando o dicionário de dados e layout. **

# In[11]:


data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        locations = df['Country'],
        locationmode = 'country names',
        z = df['Power Consumption KWH'],
        text = df['Text'],
        colorbar = {'title' : 'Consumo de Energia'},
      ) 


# In[13]:


layout = dict(
    title = 'Consumo de Energia',
    geo = dict(
        showframe = True,
        projection = {'type':'equirectangular'}
    )
)


# In[14]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# ##  Choropleth EUA
# 
# ** Importe o arquivo csv 2012_Election_Data usando pandas. **

# In[15]:


df2 = pd.read_csv('2012_Election_Data')


# ** Verifique o cabeçalho do DataFrame. **

# In[16]:


df2.head()


# ** Agora crie um gráfico que exiba a idade da população votante (Voting-Age Population, VAP) por estado. Se você quiser mais jogar com outras colunas, certifique-se de considerar seu tipo de dados. O VAP já foi transformado em float para você. **

# In[25]:


data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        locations = df2['State Abv'],
        locationmode = 'USA-states',
        z = df2['Voting-Age Population (VAP)'],
        text = df2['State'],
        colorbar = {'title' : 'Populacao'},
      ) 


# In[28]:


layout = dict(
    title = 'Consumo de Energia',
    geo = dict(
        scope='usa',
        showframe = True
    )
)


# In[29]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

