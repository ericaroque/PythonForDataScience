
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


from plotly import __version__


# In[7]:


print (__version__)


# In[12]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[13]:


import cufflinks as cf


# In[14]:


init_notebook_mode(connected= True)


# In[15]:


cf.go_offline()


# In[17]:


df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())


# In[18]:


df.head()


# In[19]:


df2 = pd.DataFrame({'Categoria': ['A','B','C'], 'Valores': [32,43,50]})


# In[20]:


df2.head()


# In[23]:


df.iplot(kind = 'scatter', x= 'A', y='B', mode = 'markers')


# In[24]:


df2.iplot(kind = 'bar', x=  'Categoria', y = 'Valores')


# In[28]:


df.count().iplot(kind = 'bar')


# In[30]:


df.iplot(kind = 'box')


# In[31]:


df3 = pd.DataFrame({'x': [1,2,3,4,5], 'y':[10,20,30,40,50], 'z':[5,4,3,2,1]})


# In[32]:


df3.head()


# In[34]:


df3.iplot(kind = 'surface', colorscale='rdylbu')


# In[35]:


df[['A', 'B']].iplot(kind= 'spread')


# In[36]:


df['A'].iplot(kind = 'hist', bins = 50)


# In[37]:


df.iplot(kind = 'bubble', x= 'A', y = 'B', size = 'C')


# In[39]:


df.scatter_matrix()

