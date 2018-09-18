
# coding: utf-8

# In[2]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_biv import scatterplot_solution_1, scatterplot_solution_2


# In this workspace, you'll make use of this data set describing various car attributes, such as fuel efficiency. The cars in this dataset represent about 3900 sedans tested by the EPA from 2013 to 2018. This dataset is a trimmed-down version of the data found [here](https://catalog.data.gov/dataset/fuel-economy-data).

# In[3]:


fuel_econ = pd.read_csv('./data/fuel_econ.csv')
fuel_econ.head()


# **Task 1**: Let's look at the relationship between fuel mileage ratings for city vs. highway driving, as stored in the 'city' and 'highway' variables (in miles per gallon, or mpg). Use a _scatter plot_ to depict the data. What is the general relationship between these variables? Are there any points that appear unusual against these trends?

# In[7]:


plt.scatter(data= fuel_econ, x= 'city', y='highway', alpha = 1/5)
plt.xlabel('City efficiency')
plt.ylabel('Highway efficiency')


# In[5]:


# run this cell to check your work against ours
scatterplot_solution_1()


# **Task 2**: Let's look at the relationship between two other numeric variables. How does the engine size relate to a car's CO2 footprint? The 'displ' variable has the former (in liters), while the 'co2' variable has the latter (in grams per mile). Use a heat map to depict the data. How strong is this trend?

# In[15]:


# bins_x = np.arange(0.5, 10.5+1, 1)
# bins_y = np.arange(-0.5, 10.5+1, 1)

bins_x = np.arange(0.6, fuel_econ['displ'].max()+0.4, 0.4)
bins_y = np.arange(0, fuel_econ['co2'].max()+50, 50)
plt.hist2d(data = fuel_econ, x = 'displ', y = 'co2', bins = [bins_x, bins_y], 
           cmap = 'viridis_r', cmin = 0.5)
plt.colorbar()


# In[6]:


# run this cell to check your work against ours
scatterplot_solution_2()

