
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_univ import histogram_solution_1


# We'll continue working with the Pokémon dataset in this workspace.

# In[2]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# **Task**: Pokémon have a number of different statistics that describe their combat capabilities. Here, create a _histogram_ that depicts the distribution of 'special-defense' values taken. **Hint**: Try playing around with different bin width sizes to see what best depicts the data.

# In[12]:


bin_edges = np.arange(0, pokemon['special-defense'].max()+5, 5)
plt.hist(data=pokemon, x='special-defense', bins=bin_edges)


# In[4]:


# run this cell to check your work against ours
histogram_solution_1()

