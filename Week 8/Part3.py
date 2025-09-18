if df is not None:
    # 1. Publications over Time
    publications_by_year = df['publish_year'].value_counts().sort_index()
    
    # 2. Top Publishing Journals
    top_journals = df['journal'].value_counts().head(10)
    
    # 3. Most Frequent Words in Titles (simplified)
    all_titles = ' '.join(df['title'].dropna()).lower()
    words = all_titles.split()
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(20)
    
    print("\n📊 Basic Analysis Results:")
    print(f"Total papers by year:\n{publications_by_year}")
    print(f"\nTop 10 journals:\n{top_journals}")
    print(f"\n20 most common words in titles:\n{most_common_words}")

    # Create visualizations
    
    # Plot 1: Publications by Year
    plt.figure(figsize=(10, 6))
    publications_by_year.plot(kind='line', marker='o')
    plt.title('Number of Publications Over Time')
    plt.xlabel('Publication Year')
    plt.ylabel('Number of Papers')
    plt.grid(True)
    plt.show()
    
    # Plot 2: Top Publishing Journals
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
    plt.title('Top 10 Journals Publishing COVID-19 Research')
    plt.xlabel('Number of Papers')
    plt.ylabel('Journal')
    plt.show()
    
    # Plot 3: Distribution of Papers by Source
    source_counts = df['source_x'].value_counts().head(5)
    plt.figure(figsize=(8, 8))
    plt.pie(source_counts, labels=source_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Papers by Source')
    plt.show()
