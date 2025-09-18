try:
    print("\n📊 Basic Statistics of Numerical Columns:")
    numerical_stats = iris_df.describe()
    print(numerical_stats)
    
    # Perform grouping
    print("\nGrouped Analysis: Average of numerical features per species")
    
    # Ensure the species column is a valid category
    if 'species' not in iris_df.columns:
        raise ValueError("The 'species' column is not in the dataset.")
    
    grouped_data = iris_df.groupby('species').mean(numeric_only=True)
    print(grouped_data)

    print("✅ Data analysis completed successfully!")

except ValueError as ve:
    print(f"❌ Data analysis error: {ve}")
    print("Please check the column names and data types.")

except Exception as e:
    print(f"❌ An unexpected error occurred during data analysis: {e}")
