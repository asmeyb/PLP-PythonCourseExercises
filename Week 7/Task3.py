try:
    sns.set_theme(style="whitegrid")
    
    # 1. Bar Chart: Average Petal Length by Species
    plt.figure(figsize=(8, 6))
    sns.barplot(x=grouped_data.index, y=grouped_data['petal length (cm)'], palette='viridis')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.show()

    # 2. Histogram: Distribution of Sepal Length
    plt.figure(figsize=(8, 6))
    sns.histplot(data=iris_df, x='sepal length (cm)', kde=True, color='skyblue')
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # 3. Scatter Plot: Sepal Length vs. Petal Length
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Dark2')
    plt.title('Sepal Length vs. Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.show()

    # 4. Line Chart: Petal Length Trend (simulated time-series)
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=iris_df, x=iris_df.index, y='petal length (cm)')
    plt.title('Petal Length Over Data Index')
    plt.xlabel('Data Index')
    plt.ylabel('Petal Length (cm)')
    plt.show()

    print("✅ All plots generated successfully!")

except KeyError as ke:
    print(f"❌ Plotting error: Missing column '{ke}'. Please check your column names.")

except Exception as e:
    print(f"❌ An unexpected error occurred during plotting: {e}")
