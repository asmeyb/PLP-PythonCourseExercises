import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from scikit-learn
from sklearn.datasets import load_iris
iris_data = load_iris()

# Create a DataFrame from the dataset
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df['species'] = iris_data.target_names[iris_data.target]

print("First few rows of the dataset:")
print(iris_df.head())
