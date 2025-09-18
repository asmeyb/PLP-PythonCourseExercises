# Barchart
# Set the style for the plots
sns.set_theme(style="whitegrid")

# Create a bar chart for average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x=species_means.index, y=species_means['petal length (cm)'], palette='viridis')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Histogram
# Create a histogram of sepal length
plt.figure(figsize=(8, 6))
sns.histplot(data=iris_df, x='sepal length (cm)', bins=10, kde=True, color='skyblue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scater Plot
# Create a scatter plot of sepal length vs. petal length, colored by species
plt.figure(figsize=(10, 8))
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Dark2')
plt.title('Sepal Length vs. Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()


# Line Chart
# Create a line chart of petal length over the data index
plt.figure(figsize=(12, 6))
sns.lineplot(data=iris_df['petal length (cm)'])
plt.title('Petal Length Trend Over Data Index')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.show()
