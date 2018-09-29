
# coding: utf-8

# In[20]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_biv import additionalplot_solution_1, additionalplot_solution_2


# We'll continue to make use of the fuel economy dataset in this workspace.

# In[21]:


fuel_econ = pd.read_csv('./data/fuel_econ.csv')
fuel_econ.head()


# **Task 1**: Plot the distribution of combined fuel mileage (column 'comb', in miles per gallon) by manufacturer (column 'make'), for all manufacturers with at least eighty cars in the dataset. Consider which manufacturer order will convey the most information when constructing your final plot. **Hint**: Completing this exercise will take multiple steps! Add additional code cells as needed in order to achieve the goal.

# In[25]:


# handle the different car makes
most_makes = fuel_econ['make'].value_counts().index[:18]
filtered_makes_in_most_makes = fuel_econ['make'].isin(most_makes)
fuel_econ_sub = fuel_econ.loc[filtered_makes_in_most_makes]

make_means = fuel_econ_sub.groupby('make').mean()
combo_mpg_order = make_means.sort_values('comb', ascending = False).index

# Plotting
graph = sb.FacetGrid(data = fuel_econ_sub, col = 'make', col_wrap = 6, size = 2, col_order = combo_mpg_order)
graph.map(plt.hist, 'comb', bins = np.arange(12, fuel_econ_sub['comb'].max()+2, 2))
graph.set_titles('{col_name}')



# In[23]:


# run this cell to check your work against ours
additionalplot_solution_1()


# **Task 2**: Continuing on from the previous task, plot the mean fuel efficiency for each manufacturer with at least 80 cars in the dataset.

# In[29]:


base_color = sb.color_palette()[0]
sb.barplot(data= fuel_econ_sub, x='comb', y='make', color=base_color, order=combo_mpg_order, ci='sd')
plt.xlabel('Avg. Combined Fuel Eff.(mpg)')


# In[26]:


# run this cell to check your work against ours
additionalplot_solution_2()

