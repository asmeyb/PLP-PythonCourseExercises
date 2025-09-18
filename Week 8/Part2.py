if df is not None:
    # Handle missing data
    # Drop rows where 'title' or 'journal' are missing, as they're essential for analysis
    df.dropna(subset=['title', 'journal'], inplace=True)
    print("\n✅ Rows with missing 'title' or 'journal' values have been removed.")

    # Prepare data for analysis
    try:
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        # Drop rows where the date conversion failed
        df.dropna(subset=['publish_time'], inplace=True)
        print("✅ 'publish_time' column converted to datetime format.")
        
        # Extract publication year
        df['publish_year'] = df['publish_time'].dt.year
        print("✅ 'publish_year' column created.")
        
    except Exception as e:
        print(f"❌ An error occurred during date conversion: {e}")

    # Create a new column for abstract word count
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()) if pd.notnull(x) else 0)
    print("✅ 'abstract_word_count' column created.")
