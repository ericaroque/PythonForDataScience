
# coding: utf-8

# # Exercícios Matplotlib 
# 
# 
# Bem-vindo aos exercícios de matplotlib! Tome seu tempo com estes, Matplotlib pode ser complicado de entender no início. Estes plots são relativamente simples, mas podem ser difíceis se esta é a sua primeira vez com matplotlib, sinta-se à vontade para dar uma olhada nas soluções à medida que avança.
# 
# Além disso, não se preocupe se você achar frustrante a sintaxe matplotlib, nós realmente não estaremos usando isso o tempo todo, dado que muitas vezes durante todo o curso, já que pretendemos usar as funções incorporadas no seaborn e no pandas. Mas, esses são construídos com matplotlib, e é por isso que ainda é importante estudar ele!
# 
# ** * NOTA: TODOS OS COMANDOS PARA PLOTAR UMA FIGURA TODOS VÃO NA MESMA CÉLULA. * **
# 
# # Exercícios
# Siga as instruções para recriar os gráficos usando esses dados:
# 
# ## Data

# In[10]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# ** Importe matplotlib.pyplot como plt e defina% matplotlib inline se você estiver usando o notebook jupyter. Qual comando você usa se você não estiver usando o notebook jupyter? **

# In[21]:


import matplotlib.pyplot as plt


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Exercício 1
# 
# ** Acompanhe estes passos: **
# * ** Crie um objeto de figura chamado fig usando plt.figure () **
# * ** Use add_axes para adicionar um eixo à tela de figura em [0,0,1,1]. Chame esse novo eixo de "ax". **
# * ** Plote (x, y) nesses eixos e defina os rótulos e títulos para corresponder ao gráfico abaixo: **

# In[22]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('title')


# ## Exercício 2
# ** Crie um objeto de figura e coloque dois eixos sobre ele, ax1 e ax2. Localizado em [0,0,1,1] e [0,2,0,5, .2, .2], respectivamente. **

# In[24]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])


# ** Agora plote (x, y) em ambos os eixos. E chame seu objeto de figura para mostrá-lo. **

# In[29]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,y,'r-')
ax2.plot(x,y,'r-')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')


# ## Exercício 3
# 
# ** Crie o gráfico abaixo, adicionando dois eixos a um objeto de figura em [0,0,1,1] e [0,2,0,5, .4, .4] **

# In[27]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])


# ** Agora use x, y e z arrays para recriar o gráfico abaixo. Observe os limites xlimits e y no gráfico inserido: **

# In[35]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax1.plot(x,z,'b-')
ax2.plot(x,y,'b-')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax2.set_title('zoom')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)


# ## Exercício 4
# 
# ** Use plt.subplots (nrows = 1, ncols = 2) para criar o gráfico abaixo. **

# In[37]:


plt.subplots(ncols=2,nrows=1)


# ** Agora trace (x, y) e (x, z) nos eixos. Note a largura de linha e o estilo objetivos. **

# In[39]:


plt.subplot(1,2,1)
plt.plot(x,y,'b--')
plt.subplot(1,2,2)
plt.plot(x,z,'r-')


# ** Veja se você pode redimensionar o gráfico adicionando o argumento figsize () em plt.subplots () apenas copiando e colando seu código anterior. **

# In[46]:


fig, axes = plt.subplots(nrows =1, ncols= 2, figsize=(10,3))
axes[0].plot(x,y,'b-', ls= '-', lw =3)
axes[1].plot(x,z,'r--',ls= '--', lw =3)

