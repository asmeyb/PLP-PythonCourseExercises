# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

st.set_page_config(layout="wide")

@st.cache_data
def load_data_st(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    df.dropna(subset=['title', 'journal', 'publish_time'], inplace=True)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df.dropna(subset=['publish_time'], inplace=True)
    df['publish_year'] = df['publish_time'].dt.year
    return df

file_path = 'metadata.csv'
df = load_data_st(file_path)

if df is not None:
    st.title("CORD-19 Data Explorer 📄🔍")
    st.markdown("A simple exploration of COVID-19 research papers using the **CORD-19** metadata dataset.")
    
    st.sidebar.header("Filter Options")
    
    # Interactive widget: Slider for year range
    min_year, max_year = int(df['publish_year'].min()), int(df['publish_year'].max())
    selected_year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    
    # Filter DataFrame based on selected year range
    filtered_df = df[(df['publish_year'] >= selected_year_range[0]) & (df['publish_year'] <= selected_year_range[1])]

    # --- Display Visualizations ---
    st.header("Key Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Publications Over Time")
        publications_by_year = filtered_df['publish_year'].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        publications_by_year.plot(kind='line', marker='o', ax=ax)
        ax.set_title('Number of Publications Over Time')
        ax.set_xlabel('Publication Year')
        ax.set_ylabel('Number of Papers')
        ax.grid(True)
        st.pyplot(fig)
        
    with col2:
        st.subheader("Top Publishing Journals")
        top_journals = filtered_df['journal'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax)
        ax.set_title('Top 10 Journals Publishing COVID-19 Research')
        ax.set_xlabel('Number of Papers')
        ax.set_ylabel('Journal')
        st.pyplot(fig)
        
    # Word Cloud (Requires the wordcloud library)
    try:
        from wordcloud import WordCloud
        st.subheader("Word Cloud of Paper Titles")
        all_titles = ' '.join(filtered_df['title'].dropna()).lower()
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    except ImportError:
        st.warning("⚠️ The 'wordcloud' library is not installed. Run `pip install wordcloud` to see this chart.")

    st.markdown("---")
    
    # Display a sample of the data
    st.header("Data Sample")
    st.dataframe(filtered_df[['title', 'authors', 'journal', 'publish_year']].head(10))

else:
    st.error("Could not load the data. Please ensure 'metadata.csv' is in the same directory.")
