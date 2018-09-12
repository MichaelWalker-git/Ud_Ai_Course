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