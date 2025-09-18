import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

try:
    # Use a common dataset from a well-known library for robustness
    from sklearn.datasets import load_iris
    iris_data = load_iris()
    
    # Create a pandas DataFrame
    iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    iris_df['species'] = iris_data.target_names[iris_data.target]
    
    print("✅ Dataset loaded successfully!")
    print("\nFirst 5 rows of the dataset:")
    print(iris_df.head())
    
    print("\nDataset Information:")
    iris_df.info()

    # Data cleaning (if needed)
    print("\nChecking for missing values:")
    missing_values = iris_df.isnull().sum()
    if missing_values.any():
        print("⚠️ Missing values detected. Cleaning the data...")
        # Example of cleaning: Dropping rows with any missing values
        iris_df.dropna(inplace=True)
        print("✅ Missing values handled.")
    else:
        print("✅ No missing values found. Dataset is clean.")

except ImportError:
    print("❌ Error: The required libraries (pandas, scikit-learn) are not installed.")
    print("Please install them using: pip install pandas scikit-learn")
    
except Exception as e:
    print(f"❌ An unexpected error occurred during data loading: {e}")
