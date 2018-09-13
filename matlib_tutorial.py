# Bar charts - depict the distribution of a categorical variable
# - Height of data points that tkae on that level

sb.countplot(data = df, x = 'cat_var')


# color_palette returns a list of RGB tuples, each tuple specifying a color.
# No parameters returns the current / default palette, and we take the first one to be the color for all bars.

sb.countplot(data = pokemon, x='generation_id', color=base_color, order=gen_order)

base_color = sb.color_palette()[0]
gen_order = pokemon['generation_id'].value_counts().index

# Overlap on x axis labels
# Two solutions:
# 1.) labels = vertical: plt.xticks(rotation=90);
# 2.) Switch axis values:  y = 'type_1'

# Sort order by pokemon type

# Absolute vs Relative Frequency
# By default countplot function will summarize and plot the data in terms of absolute frequency (pure counts)

# Relative frequency : height indicates the proportion of data taking each level

# Method one of relative frequency - Relabel the counts axis in terms of proportions
# get proportion taken by most common group for derivation
# of tick marks
n_points = df.shape[0]
max_count = df['cat_var'].value_counts().max()
max_prop = max_count / n_points

# generate tick mark locations and names
tick_props = np.arange(0, max_prop, 0.05)
tick_names = ['{:0.2f}'.format(v) for v in tick_props]

# create the plot
base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color)
plt.yticks(tick_props * n_points, tick_names)
# The first argument takes the tick locations: in this case, the tick proportions multiplied back to be on the scale of counts.
# The second argument takes the tick names: in this case, the tick proportions formatted as strings to two decimal places.
plt.ylabel('proportion')

# Additional variation

# create the plot
base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color)

# add annotations
n_points = df.shape[0]
cat_counts = df['cat_var'].value_counts()
locs, labels = plt.xticks() # get the current tick locations and labels

# loop through each pair of locations and labels
for loc, label in zip(locs, labels):

    # get the text property for the label to get the correct count
    count = cat_counts[label.get_text()]
    # I use the .get_text() method to obtain the category name, so I can get the count of each category level.

    pct_string = '{:0.1f}%'.format(100*count/n_points)

    # print the annotation just below the top of the bar
    plt.text(loc, count-8, pct_string, ha = 'center', color = 'w')
    # I use the text function to print each percentage, with the x-position, y-position, and string as the three main parameters to the function.

##################################################
# Change tick location and labels
plt.xticks(tick_props * n_pokemon, tick_names)

plt.xlabel('proportion')

# axis instead of count
for i in range(type_counts.shape[0]):
    count = type_counts[i]
    plt.text[count+1, i, pct_string, va="center"]


# Counting Missing Data
#  We can use pandas functions to create a table with the number of missing values in each column.
#     df.isna().sum()
#  Seaborn's barplot function is built to depict a summary of one quantitative variable against levels of a second, qualitative variable, but can be used here.

na_counts = df.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)


# The first argument to the function contains the x values (column names)
# The second is the y values (our counts)

# If your data is not yet summarized, however, just use the countplot function so that you don't need to do extra summarization work


################################################## PIE CHARTS ##################################################
# Fairly limited plot type; Guidelines:
#     Relative frequencies, areas should represent parts of a whole, rather than measurements on a second variable
#     Limit the number of slices plotted, pie charts usually works best with 2 or 3 slices
#     Plot data systematically, plotting a pie chart from 12 clockwise from most to least
# Bar charts are safer and helps the user better understand

sorted_counts = df['cat_var'].value_counts()
plt.pie(sorted_counts, labels= sorted_counts.index, startangle=90, counterclock=False);
plt.axis('square')
#  Axis makes it so that the scaling of the plot is equal on both the x and y axis

# Donut plot
sorted_counts = df['cat_var'].value_counts()
plt.pie(sorted_counts, labels=sorted_counts.index, startangle=90, counterclock=False, wedgeProps ={'width': 0.4});
plt.axis('square')
# setting the wedges' width property to less than 1 removes coloring from the center of the circle.

# Histogram - used to plot the distribution of a numberic variable
# Counts on value ranges, bin size (range)

plt.hist(data = df, x = 'num_var')

# When a data value is on a bin edge, it is counted in the bin to its right.
# The exception is the rightmost bin edge, which places data values equal to the uppermost limit into the right-most bin (to the upper limit's left).

# By default, the hist function divides the data into 10 bins,

# df['num_var'].describe()) to gauge what minimum and maximum bin limits
bin_edges = np.arange(0, df['num_var'].max() + 1, 1)
plt.hist(data=df, x='num_var', bins=bin_edges)
# arrange - leftmost bin edge
# second argument is the upper limit
# third - bin width

# Playing around with bin sizes and find median
# larger figure size for subplots
plt.figure(figsize=[10, 5])

# histogram on left, example of too large bin size
plt.subplit(1,2,1)
bin_edges = np.arange(0, df['num_var'].max() + 4, 4)
plt.hist(data=df, x='num_var', bins=bin_edges)

# too small of bin size
plt.subplot(1,2,2)
bin_edges = np.arange(0, df['num_var'].max() + 1/4, 1/4)
plt.hist(data=df, x='num_var', bins=bin_edges)

# The seaborn function distplot
sb.distplot(df['num_var'])  # first argument must be the Series or array with the points to be plotted

# Pros:
    # has built-in rules for specifying histogram bins, and by default plots a kernel density estimate (KDE) on top of the data.
    # The vertical axis is based on the KDE,

bin_edges = np.arange(0, df['num_var'].max() + 1, 1)
sb.distplot(df['num_var'], bins=bin_edges, kde=False, hist_kws={'alpha': 1})


################################################## Figure, axes, subplots ##################################################

# figure() creates a new Figure object, a reference to which has been stored in the variable fig.
# One of the Figure methods is .add_axes(), which creates a new Axes object in the Figure.


# To use Axes objects with seaborn, seaborn functions usually have an "ax" parameter to specify upon which Axes a plot will be drawn.

fig = plt.figure()
ax = fig.add_axes([.125, .125, .775, .755])
base_color = sb.color_palette()[0]
sb.countplot(data = df, x = 'cat_var', color = base_color, ax = ax)


# If you don't assign Axes objects as they're created, you can retrieve the current Axes using ax = plt.gca(),
# or you can get a list of all Axes in a Figure fig by using axes = fig.get_axes().

# fig, axes = plt.subplots(3, 4) # grid of 3x4 subplots
    # axes = axes.flatten() # reshape from 3x4 array into 12-element vector
    # for i in range(12):
    #     plt.sca(axes[i]) # set the current Axes
    #     plt.text(0.5, 0.5, i+1) # print conventional subplot index number to middle of Axes