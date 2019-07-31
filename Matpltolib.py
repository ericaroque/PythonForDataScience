
# coding: utf-8

# In[1]:


import matplotlib.pyplot as pl


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np


# In[5]:


x = np.linspace(0,5,11)


# In[6]:


x


# In[7]:


y = x * x


# In[8]:


y


# In[19]:


pl.plot(x,y, 'r--')
pl.ylabel('Eixo Y')
pl.xlabel('Eixo X')
pl.title('Titulo')


# In[27]:


pl.subplot(1,2,1)
pl.plot(x,y, 'r--')
pl.subplot(1,2,2)
pl.plot(y,x,'g*-')


# In[28]:


fig = pl.figure()


# In[38]:


fig = pl.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
axes1.plot(x,y)
axes.set_xlabel('Eixo X')
axes.set_title('Titulo')
axes2.plot(y,x)


# In[42]:


fig, ax = pl.subplots()
ax.plot(x,x**3, 'b--')
ax.plot(x,x**4, 'g--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Grafico')


# In[47]:


fig, ax= pl.subplots (nrows=1, ncols=2)


# In[49]:


for axe in ax:
    axe.plot(x,y,'b')
    axe.set_title('Titulo')
fig    


# In[51]:


ax[0].plot(x,y,'b')
ax[0].set_title('Titulo 1')

ax[1].plot(x,y,'b')
ax[1].set_title('Titulo 1')
fig


# In[57]:


fig, ax = pl.subplots(nrows=5, ncols=5)
pl.tight_layout()


# In[58]:


fig = pl.figure(figsize=(8,4), dpi = 100)


# In[69]:


fig, axes = pl.subplots(figsize=(10,3))

axes.plot(x,y, 'r-', label = 'x ^2')
axes.plot(y,x, 'g--', label = 'x ^3')
axes.set_title('Titulos')
axes.legend(loc =0)


# In[70]:


x


# In[83]:


fig, ax = pl.subplots(figsize=(8,10))
ax.plot(x, x**2, 'b--', linewidth=10, alpha =0.5, linestyle = '-', marker = 'o')
ax.plot(x, x**3, 'g-')

ax.set_xlim(0,2)
ax.set_ylim(0,10)


# In[84]:


pl.scatter(x,y)


# In[ ]:


fig.savefig('imagem.jpg')

