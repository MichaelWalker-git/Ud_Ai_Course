
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_univ import scales_solution_1, scales_solution_2


# Once again, we make use of the Pokémon data for this exercise.

# In[2]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# **Task 1**: There are also variables in the dataset that don't have anything to do with the game mechanics, and are just there for flavor. Try plotting the distribution of Pokémon heights (given in meters). For this exercise, experiment with different axis limits as well as bin widths to see what gives the clearest view of the data.

# In[22]:



bin_edges = np.arange(0, pokemon['height'].max()+0.2, 0.2)
plt.hist(data=pokemon, x = 'height', bins=bin_edges)
plt.xlim(0, 6)


# In[17]:


# run this cell to check your work against ours
scales_solution_1()


# **Task 2**: In this task, you should plot the distribution of Pokémon weights (given in kilograms). Due to the very large range of values taken, you will probably want to perform an _axis transformation_ as part of your visualization workflow.

# In[35]:


# def sqrt_trans(x, inverse = False):
#     if not inverse:
#         return np.sqrt(x)
#     else:
#         return x ** 2

# bin_edges = np.arange(0, sqrt_trans(pokemon['weight'].max()) + 1, 1)
# plt.hist(pokemon['weight'].apply(sqrt_trans), bins=bin_edges)

# tick_locs= np.arange(0, sqrt_trans((pokemon['weight']).max())+8, 8)
# plt.xticks(tick_locs, sqrt_trans(tick_locs, inverse=True).astype(int))

bins = 10 ** np.arange(-1, 3.0+0.1, 0.1)
ticks = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
labels = ['{}'.format(val) for val in ticks]

plt.hist(data = pokemon, x = 'weight', bins = bins)
plt.xscale('log')
plt.xticks(ticks, labels)
plt.xlabel('Weight (kg)')


# In[19]:


# run this cell to check your work against ours
scales_solution_2()

