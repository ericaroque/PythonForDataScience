
# coding: utf-8

# In[96]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


tips =  sns.load_dataset('tips')


# In[16]:


tips.head()


# In[10]:


sns.distplot(tips['total_bill'], kde = False, bins=50)


# In[18]:


sns.jointplot(x ='total_bill', y='tip', data=tips, kind='reg')


# In[21]:


sns.pairplot(tips, hue='sex', palette='coolwarm')


# In[22]:


sns.rugplot(tips['total_bill'])


# In[24]:


sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])


# In[25]:


import numpy as np


# In[26]:


tips.head()


# In[29]:


sns.barplot(x='sex', y='total_bill', data = tips)


# In[30]:


sns.barplot(x='sex', y='total_bill', data = tips, estimator=np.std)


# In[31]:


sns.countplot(x= 'sex', data = tips)


# In[35]:


sns.boxplot(x='day', y='total_bill', data= tips,  palette='rainbow', hue = 'sex')


# In[37]:


sns.boxplot(data =tips, palette='rainbow', orient='h')


# In[40]:


sns.violinplot(x='day', y= 'tip', data = tips, hue='sex', split=True)


# In[45]:


sns.stripplot(x= 'day', y='total_bill', data = tips, jitter=True, hue='sex', dodge= True)


# In[48]:


sns.swarmplot(x= 'day', y='total_bill', data = tips, hue='sex', split= True)


# In[51]:


sns.swarmplot(x= 'day', y='total_bill', data = tips,  color='black')
sns.violinplot(x='day', y= 'total_bill', data = tips)


# In[52]:


sns.factorplot(x='sex', y='total_bill', data= tips, kind = 'bar')


# In[53]:


flights = sns.load_dataset('flights')


# In[54]:


tips = sns.load_dataset('tips')


# In[55]:


flights.head()


# In[56]:


tips.head()


# In[58]:


crr =tips.corr()


# In[60]:


sns.heatmap(crr, cmap = 'coolwarm', annot=True)


# In[67]:


pf = flights.pivot_table(values= 'passengers', index='month', columns='year' )


# In[68]:


pf


# In[71]:


sns.heatmap(pf, cmap='magma', linecolor='white', linewidths=1)


# In[73]:


sns.clustermap(pf, standard_scale=1)


# Plots de Regressão do Seaborn

# In[74]:


tips.head()


# In[75]:


tips.info()


# In[89]:


sns.lmplot(x='total_bill', y = 'tip', data=tips, hue= 'sex', col='day', aspect=0.6, height=8)


# In[90]:


iris = sns.load_dataset('iris')


# In[91]:


iris.head()


# In[92]:


iris['species'].value_counts()


# In[99]:


g= sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map(plt.scatter)


# In[101]:


g= sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[102]:


sns.pairplot(iris, hue='species')


# In[103]:


tips = sns.load_dataset('tips')


# In[104]:


tips.head()


# In[107]:


g = sns.FacetGrid(tips, col= 'time', row= 'smoker')
g.map(plt.hist, 'total_bill')


# In[110]:


tips.head()


# In[116]:


sns.set_style('whitegrid')
sns.countplot(data=tips, x= 'sex')
sns.despine()


# In[117]:


sns.set_style('whitegrid')
plt.figure(figsize=(12,8))
sns.countplot(data=tips, x= 'sex')
sns.despine()


# In[124]:


sns.lmplot(x='total_bill',y='tip',data = tips, height =2, aspect =2)


# In[131]:


sns.set_context('poster', font_scale=1)
sns.lmplot(x='total_bill',y='tip',data = tips, hue='sex', palette='PRGn')

