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
# you'd like to remove the box plot, you can set the inner = None

base_color = sb.color_pallett()[0]
sb.violotplot(data=df, x='cat_var', y='num_var', color=base_color, inner=None)

# Box Plot - showing the relationship between a numeric variable and a categorical variable, summarization of the data
# Center line = Median
# whiskers = Max and min of data
# Dots => outliers (defined outside of standard deviation)

plt.figure(figsize = [10, 5])
base_color = sb.color_palette()[0]

# left plot: violin plot
plt.subplot(1, 2, 1)
ax1 = sb.violinplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)

# right plot: box plot
plt.subplot(1,2,2)
sb.boxplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot

# Clustered Bar Charts
# bars are organized into clusters based on levels of the first variable,
# and then bars are ordered consistently across the second variable within each cluster

sb.countplot(data = df, x = 'cat_var1', hue = 'cat_var2')

ax = sb.countplot(data = df, x = 'cat_var1', hue = 'cat_var2')
ax.legend(loc = 8, ncol = 3, framealpha = 1, title = 'cat_var2')

# Alternative Approach (Heat Map)
# The seaborn function heatmap is at home with this type of heat map implementation
# Instead of providing the original dataframe, we need to summarize the counts into a matrix that will then be plotted.

ct_counts = df.groupby(['cat_var1', 'cat_var2']).size()
ct_counts = ct_counts.reset_index(name = 'count')
ct_counts = ct_counts.pivot(index = 'cat_var2', columns = 'cat_var1', values = 'count')
sb.heatmap(ct_counts)

sb.heatmap(ct_counts, annot = True, fmt = 'd')
# annot = True makes it so annotations show up in each cell,

# Faceting
# the data is divided into disjoint subsets, most often by different levels of a categorical variable
# comparing distributions or relationships across levels of additional variables, especially when there are three or more variables of interest overall
# Two steps involved in creating a faceted plot
# First, we need to create an instance of the FacetGrid object and specify the feature we want to facet by ("cat_var" in our example).
# we use the map method on the FacetGrid object to specify the plot type and variable(s) that will be plotted in each subset (in this case, histogram on "num_var").

g = sb.FacetGrid(data = df, col = 'cat_var')
g.map(plt.hist, "num_var")

# data is being plotted independently. Each uses the default of ten bins from hist to bin together the data, and each plot has a different bin size

bin_edges = np.arange(-3, df['num_var'].max()+1/3, 1/3)
g = sb.FacetGrid(data = df, col = 'cat_var')
g.map(plt.hist, "num_var", bins = bin_edges)

# col_wrap = 5 means that the plots will be organized into rows of five facets each, rather than a single long row of fifteen plots

group_means = df.groupby(['many_cat_var']).mean()
group_order = group_means.sort_values(['num_var'], ascending = False).index

g = sb.FacetGrid(data = df, col = 'many_cat_var', col_wrap = 5, size = 2,
                 col_order = group_order)
g.map(plt.hist, 'num_var', bins = np.arange(5, 15+1, 1))
g.set_titles('{col_name}')

# Bar plot
# plot a numeric variable against a categorical variable by adapting a bar chart so that its bar
# heights indicate the mean of the numeric variable

base_color = sb.color_palette()[0]
sb.barplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
# error bars plotted to show the uncertainty in the mean based on variance and sample size

# Pointplot function can be used to plot the averages as points rather than bars.

sb.pointplot(data = df, x = 'cat_var', y = 'num_var', linestyles = "")
plt.ylabel('Avg. value of num_var')

# pointplotwill connect values by a line
# remove the line via linestyles = "" for nominal data.

plt.figure(figsize = [12, 5])
base_color = sb.color_palette()[0]

# left plot: violin plot
plt.subplot(1, 3, 1)
sb.violinplot(data = df, x = 'condition', y = 'binary_out', inner = None,
              color = base_color)
plt.xticks(rotation = 10) # include label rotation due to small subplot size

# center plot: box plot
plt.subplot(1, 3, 2)
sb.boxplot(data = df, x = 'condition', y = 'binary_out', color = base_color)
plt.xticks(rotation = 10)

# right plot: adapted bar chart
plt.subplot(1, 3, 3)
sb.barplot(data = df, x = 'condition', y = 'binary_out', color = base_color)
plt.xticks(rotation = 10)

# Adapted Histograms
# Matplotlib's hist function can also be adapted so that bar heights indicate value other than a count of points through the use of the "weights" parameter.
# If we change the weights to be a representative function of each point's value on a second variable, then the sum will end up representing something other than a count.

# bin_edges = np.arange(0, df['num_var'].max()+1/3, 1/3)

# count number of points in each bin
bin_idxs = pd.cut(df['num_var'], bin_edges, right = False, include_lowest = True,
                  labels = False).astype(int)
pts_per_bin = df.groupby(bin_idxs).size()

num_var_wts = df['binary_out'] / pts_per_bin[bin_idxs].values

# plot the data using the calculated weights
plt.hist(data = df, x = 'num_var', bins = bin_edges, weights = num_var_wts)

# To get the mean of the y-variable ("binary_out") in each bin,
# the weight of each point should be equal to the y-variable value,
# divided by the number of points in its x-bin (num_var_wts).

# .values at the end of the num_var_wts expression is what allows for the elementwise division operation to be
# successful. bin_idxs allows for more convenient numeric referencing of bin membership.

# Line Plots
# line plot is a fairly common plot type that is used to plot the trend of one numeric variable against values of a second variable
# all data points are plotted, in a line plot, only one point is plotted for every unique x-value or bin of x-values (like a histogram)
#  x-variable represents time,
# seaborn function tsplot that is intended to be used with time series data

#  Matplotlib's errorbar function, performing some processing on the data in order to get it into its necessary form.

# plt.errorbar(data = df, x = 'num_var1', y = 'num_var2')


# set bin edges, compute centers
xbin_edges = np.arange(0.5, df['num_var1'].max()+0.25, 0.25)
xbin_centers = (xbin_edges + 0.25/2)[:-1]

# compute statistics in each bin
data_xbins = pd.cut(df['num_var1'], xbin_edges, right = False, include_lowest = True)
y_means = df['num_var2'].groupby(data_xbins).mean()
y_sems = df['num_var2'].groupby(data_xbins).sem()

# plot the summarized data
plt.errorbar(x = xbin_centers, y = y_means, yerr = y_sems)

# Alternate
#  pandas' rolling method
# rolling window will make computations on sequential rows of the dataframe, we should use sort_values to put the x-values in ascending order first.

# compute statistics in a rolling window
df_window = df.sort_values('num_var1').rolling(15)
x_winmean = df_window.mean()['num_var1']
y_median = df_window.median()['num_var2']
y_q1 = df_window.quantile(.25)['num_var2']
y_q3 = df_window.quantile(.75)['num_var2']

# plot the summarized data
base_color = sb.color_palette()[0]
line_color = sb.color_palette('dark')[0]
plt.scatter(data = df, x = 'num_var1', y = 'num_var2')
plt.errorbar(x = x_winmean, y = y_median, c = line_color)
plt.errorbar(x = x_winmean, y = y_q1, c = line_color, linestyle = '--')
plt.errorbar(x = x_winmean, y = y_q3, c = line_color, linestyle = '--')
plt.savefig('L4_C13_Lineplot3.png')

bin_edges = np.arange(-3, df['num_var'].max()+1/3, 1/3)
g = sb.FacetGrid(data = df, hue = 'cat_var', size = 5)
g.map(plt.hist, "num_var", bins = bin_edges, histtype = 'step')
g.add_legend()

# Functions you provide to the map method of FacetGrid objects do not need to be built-ins.
# Below, I've written a function to perform the summarization operations seen above to plot an errorbar
# line for each level of the categorical variable, then fed that function (freq_poly) to map.

def freq_poly(x, bins = 10, **kwargs):
    """ Custom frequency polygon / line plot code. """
    # set bin edges if none or int specified
    if type(bins) == int:
        bins = np.linspace(x.min(), x.max(), bins+1)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2

    # compute counts
    data_bins = pd.cut(x, bins, right = False,
                       include_lowest = True)
    counts = x.groupby(data_bins).count()

    # create plot
    plt.errorbar(x = bin_centers, y = counts, **kwargs)

bin_edges = np.arange(-3, df['num_var'].max()+1/3, 1/3)
g = sb.FacetGrid(data = df, hue = 'cat_var', size = 5)
g.map(freq_poly, "num_var", bins = bin_edges)
g.add_legend()


# Adding a third variable
# Using Color for Third Variables
# One of the most common ways of adding a third variable to a plot in matplotlib and seaborn is through the use of color.
# The violinplot, boxplot, and barplot functions can all be made with third-variable clusters by adding a "hue" parameter.

# Heat maps can be adapted to depict third variables - hanging the "weights" parameter for hist2d

plt.scatter(data = df, x = 'num_var1', y = 'num_var2', c = 'num_var3')
plt.colorbar()

#  qualitative variable, you can set different colors for different levels of a categorical variable
# through the "hue" parameter on seaborn's FacetGrid class.
g = sb.FacetGrid(data = df, hue = 'cat_var1', size = 5)
g.map(plt.scatter, 'num_var1', 'num_var2')
g.add_legend()

# Qualitative palettes are built for nominal-type data.
# palette should also try and avoid drastic changes in brightness and saturation
#  that would cause a reader to interpret one category as being more important than the others
sb.palplot(sb.color_palette(n_colors=9))

# sequential palette, consecutive color values should follow each other systematically.
# Typically, this follows a light-to-dark trend across a single or small range of hues,
# where light colors indicate low values and dark colors indicate high values
sb.palplot(sb.color_palette('viridis', 9))

# diverging palette, two sequential palettes with different hues are put back to back,
# with a common color (usually white or gray) connecting them. One hue indicates values greater than the center point,
# while the other indicates values smaller than the center.
sb.palplot(sb.color_palette('vlag', 9))

#  Seaborn also adds in a number of its own palettes:
#
# Qualitative (all up to 6 colors): 'deep', 'pastel', 'dark', 'muted', 'bright', 'colorblind'
# Sequential: 'rocket' (white-orange-red-purple-black), 'mako' (mint-green-blue-purple-black)
# Diverging: 'vlag' (blue-white-red), 'icefire' (blue-black-orange)

# FacetGrid through the "palette" parameter,
# in scatter through the "cmap" parameter.

#  To be safe here, avoid or minimize transparency in plots with color.
# You may need to plot only a sample of your points in order to make sure that the effect of the third variable is clearly visible.

plt.figure(figsize = [5,5])

# left: qualitative points
plt.scatter(0,0.5,s = 1e4, c = sb.color_palette()[0], alpha = 0.5)
plt.scatter(0,-0.5,s = 1e4, c = sb.color_palette()[1], alpha = 0.5)

# right: quantitative points
plt.scatter(1,0.5,s = 1e4, c = sb.color_palette('Blues')[2], alpha = 0.5)
plt.scatter(1,-0.5,s = 1e4, c = sb.color_palette('Blues')[4], alpha = 0.5)

# set axes for point overlap
plt.xlim(-0.5,1.5)
plt.ylim(-3.5,3.5)
plt.xticks([])
plt.yticks([])

#  FacetGrid could be used to subset your dataset across levels of a categorical variable, and then create one plot for each subset.
g = sb.FacetGrid(data = df, col = 'cat_var2', row = 'cat_var1', size = 2.5,
                margin_titles = True)
g.map(plt.scatter, 'num_var1', 'num_var2')

# Swarm Plots
# Similar to a scatterplot, each data point is plotted with position according to its value on the two variables being plotted.
# Instead of randomly jittering points as in a normal scatterplot,
#  points are placed as close to their actual value as possible without allowing any overlap.
# A swarm plot can be created in seaborn using the swarmplot function, similar to how you would a call violinplot or boxplot


plt.figure(figsize = [12, 5])
base_color = sb.color_palette()[0]

# left plot: violin plot
plt.subplot(1, 3, 1)
ax1 = sb.violinplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)

# center plot: box plot
plt.subplot(1, 3, 2)
sb.boxplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot

# right plot: swarm plot
plt.subplot(1, 3, 3)
sb.swarmplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot
# IMPORTANT:  it is only reasonable to use a swarm plot if we have a small or moderate amount of data.

# Rug and Strip Plots
#  In a rug plot, all of the data points are plotted on a single axis, one tick mark or line for each one
g = sb.JointGrid(data = df, x = 'num_var1', y = 'num_var2')
g.plot_joint(plt.scatter)
g.plot_marginals(sb.rugplot, height = 0.25)

# Seaborn's JointGrid class enables this plotting of bivariate relationship with marginal univariate plots for numeric data.
# The plot_joint method specifies a plotting function for the main, joint plot for the two variables,
# while the plot_marginals method specifies the plotting function for the two marginal plots.

# inner = "stick" and inner = "point"
# to include a swarm plot inside of the violin areas, instead of a box plot.

plt.figure(figsize = [10, 5])
base_color = sb.color_palette()[0]
#
# # left plot: strip plot
plt.subplot(1, 2, 1)
ax1 = sb.stripplot(data = df, x = 'num_var', y = 'cat_var', color = base_color)
#
# # right plot: violin plot with inner strip plot as lines
plt.subplot(1, 2, 2)
sb.violinplot(data = df, x = 'num_var', y = 'cat_var', color = base_color, inner = 'stick')