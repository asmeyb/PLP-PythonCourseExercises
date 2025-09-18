print("\nBasic statistics of numerical columns:")
print(iris_df.describe())

print("\nMean of numerical features grouped by species:")
species_means = iris_df.groupby('species').mean()
print(species_means)
