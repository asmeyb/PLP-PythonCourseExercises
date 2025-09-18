import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import streamlit as st
import os

# Function to safely load data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, low_memory=False)
        print("✅ Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found.")
        return None

file_path = 'metadata.csv'
df = load_data(file_path)

if df is not None:
    print("\n📦 DataFrame Dimensions:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n📝 First 5 rows of the dataset:")
    print(df.head())
    
    print("\n📊 Data Types and Non-Null Counts:")
    df.info()
    
    print("\n🔍 Missing values in key columns:")
    key_columns = ['title', 'authors', 'journal', 'publish_time', 'abstract']
    print(df[key_columns].isnull().sum())
    
    print("\n📈 Basic statistics for numerical columns:")
    print(df.describe())
