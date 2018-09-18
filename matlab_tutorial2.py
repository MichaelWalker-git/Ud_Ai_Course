# Bivariate plots
# 1.) scatterplots for quantitative variable vs quantitative variable
# 2.) Violin plots for quantitative variable vs quantitative variable
# 3.) Clustered bar charts for qualitative variable vs qualitative variable

plt.scatter(data= df, x= 'num_var1', y='num_var2')
# Relationship between two numberic variables

# x relaes to feature, y to the second

# Alternate Approach - regplot - combines scatterplot creation with regression function
sb.regplot(data=df, x= 'num_var1', y='num_var2')

# log(y) ~ x relationship, plotting the regession is not appropriate, reg_fit = False

# We can transform the data
def log_trans(x, inverse = False):
    if not inverse:
        return np.log10(x)
    else:
        return np.power(10, x)

sb.regplot(df['num_var1'], df['num_var2'].apply(log_trans))
tick_locs = [10, 20, 50, 100, 200, 500]
plt.yticks(log_trans(tick_locs), tick_locs)

# Overplotting, transparency, jitter
# If you have a very large number of points to plot or our numberic variables are discrete valued,
# it is possible that using a scatterplot straightforwardly will not be informative/ overplotted

plt.scatter(data = df, x = 'disc_var1', y = 'disc_var2')

# We may want to employ transparency and jitter to make the scatterplot more informative
plt.scatter(data = df, x = 'disc_var1', y = 'disc_var2', alpha = 1/5)

# The jitter settings will cause each point to be plotted in a uniform ±0.2 range of their true values.
# Note that transparency has been changed to be a dictionary assigned to the "scatter_kws" parameter.
# This is necessary so that transparency is specifically associated with the scatter component of the regplot function.

# Heat maps
# 2d version of the histogram can be used as a sub. for a scatterplot

plt.subplot(1,2,1)
sb.regplot(data= df, x= 'sisc_va1', y= 'sisc_var2', fit_reg= False, x_jitter = 0.2, scatter_kws = {'alpha': 1/3})

# Heat map with bin edges between values
plt.subplot(1,2,2)
bins_x = np.arrange(0.5, 10.5+1, 1)
bins_y = np.arrange(-0.5, 10.5+1, 1)

plt.hist2d(data =df, x= 'disc_var1', y = 'disc_var2', bins=[bins_x, bins_y])

plt.colorbar()
# Choosing an appropriate bin size is just as important here as it was for the univariate histogram

# To select a different color palette, you can set the "cmap" parameter
# Example:  cmap = 'viridis_r'

# hist2d returns a number of different variables, including an array of counts
bins_x = np.arange(0.5, 10.5+1, 1)
bins_y = np.arange(-0.5, 10.5+1, 1)
h2d = plt.hist2d(data=df, x='disc_var1', y='disc_var2', bins=[bins_x, bins_y], cmap='viridis_r', cmin=0.5)
counts = h2d[0]

for i in range(counts.shape[0]):
    for j in range(counts.shape[1]):
        c = counts[i,j]
        if c >= 7: # increase visibility on darkest cells
            plt.text(bins_x[i]+0.5, bins_y[j]+0.5, int(c),
                     ha = 'center', va = 'center', color = 'white')
        elif c > 0:
            plt.text(bins_x[i]+0.5, bins_y[j]+0.5, int(c),
                     ha = 'center', va = 'center', color = 'black')


# Violin plots: used to compare qualatitive data vs quantitive data
# violin plot is on the lower level of abstraction
# plotted as a kernel density estimate, smoothed histogram

sb.violotplot(data=df, x = 'cat_var', y = 'num_var')

# Two bumps = bimodality
# Long skiny = lots of variance
# Tight center can be skewed negatively and positively
# black shape with a white dot inside => miniature box plot
