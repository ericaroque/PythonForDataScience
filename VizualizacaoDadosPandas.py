
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[25]:


import matplotlib as plt
plt.style.use('dark_background')


# In[17]:


import seaborn as sns


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_csv("df1", index_col=0)


# In[6]:


df.head()


# In[7]:


df2 = pd.read_csv("df2", index_col=0)


# In[8]:


df2.head()


# In[26]:


df['A'].hist()


# In[27]:


df2.head()


# In[28]:


df2.info()


# In[30]:


df2.plot.area(alpha =0.4)


# In[32]:


df2.plot.bar(stacked = True)


# In[44]:


df['A'].plot.hist(bins = 50)


# In[45]:


df.head()


# In[49]:


df.plot.scatter(x = 'A', y='B',c='C', cmap = 'inferno' )


# In[50]:


df2.plot.box()


# In[52]:


df3 = pd.DataFrame(np.random.rand(1000,2), columns=['A','B'])


# In[57]:


df3.plot.hexbin(x= 'A', y= 'B', gridsize=30)


# In[59]:


df2.plot.kde()

