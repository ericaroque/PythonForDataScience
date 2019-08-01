
# coding: utf-8

# # Execícios de Seaborn 
# 
# Hora de praticar suas novas habilidades do Seaborn! Tente recriar os gráficos abaixo (não se preocupe com esquemas de cores, apenas com o plot).

# ## Os dados
# 
# Nós estaremos trabalhando com um famoso conjunto de dados do Titanic para esses exercícios. Mais tarde, na seção de Machine Learning do curso, vamos revisar esses dados e usá-lo para prever as taxas de sobrevivência dos passageiros. Por enquanto, nos concentraremos apenas na visualização dos dados com seaborn:

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


sns.set_style('whitegrid')


# In[3]:


titanic = sns.load_dataset('titanic')


# In[4]:


titanic.head()


# # Exercícios
# 
# ** Recrie os plots abaixo usando o DataFrame Titanic. Há poucas dicas, uma vez que a maioria dos plots pode ser feito com apenas uma ou duas linhas de código e uma dica basicamente daria a solução. Mantenha atenção aos rótulos x e y para dicas. **
# 
# ** *Nota! Para não perder a imagem do plot, certifique-se de não codificar na célula que está diretamente acima do gráfico, há uma célula extra acima daquela que não substituirá esse gráfico! * **

# In[5]:


# PONHA O SEU CÓDIGO AQUI, 
# POIS SE USASSE A LINHA DEBAIXO, PODERIA ACABAR APAGANDO O PLOT QUE DESEJAMOS ENCONTRAR.


# In[7]:


sns.jointplot(x= 'fare', y='age', data = titanic)


# In[10]:


sns.distplot(titanic['fare'], kde=False,color='red', bins=30)


# In[15]:


sns.boxplot(x='class', y='age', data= titanic, palette='rainbow')


# In[18]:


sns.swarmplot(x='class', y='age', data= titanic, palette='Set2')


# In[19]:


sns.countplot(x='sex', data= titanic)


# In[24]:


corr = titanic.corr()
sns.heatmap(corr, cmap='coolwarm')
plt.title('titanic.corr()')


# In[26]:


g= sns.FacetGrid(data = titanic, col='sex')
g.map(plt.hist,'age')

