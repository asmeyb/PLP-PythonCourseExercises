Project Documentation
This project involved a complete data science workflow, from data acquisition and cleaning to analysis, visualization, and application development. The code is structured into four main parts to ensure clarity and logical progression.

Part 1: Focuses on data loading and initial exploration. It includes checks for data dimensions, types, and missing values to provide a foundational understanding of the dataset.

Part 2: Dedicated to data cleaning and preparation. It handles critical steps like converting the publish_time column to a proper datetime format and creating new features (e.g., publish_year) for time-series analysis.

Part 3: Conducts data analysis and creates static visualizations using matplotlib and seaborn. This section uncovers key insights, such as publication trends over time and top publishing journals.

Part 4: Builds a simple, interactive Streamlit dashboard that integrates the findings and visualizations from the previous parts, allowing users to explore the data dynamically. The app is designed for user-friendliness and clear presentation.

💡 Key Findings
Our analysis of the CORD-19 metadata revealed several significant patterns:

Publication Volume: The number of publications surged dramatically in 2020 and 2021, directly reflecting the scientific community's focused response to the COVID-19 pandemic. This highlights the rapid nature of research during a global health crisis.

Top Publishers: Journals and pre-print servers like medRxiv and bioRxiv were among the most prolific publishers. This suggests that scientists prioritized the quick dissemination of research through pre-print platforms, which bypass the traditional, lengthy peer-review process.

Data Challenges: The dataset is extremely large and contains numerous missing values, particularly in key columns. Rigorous data cleaning was essential to ensure the accuracy and reliability of the analysis.

🤔 Challenges and Learning
This assignment presented several valuable learning opportunities:

Handling Large Datasets: The sheer size of the metadata.csv file (several GB) was a significant challenge. I learned to use efficient pandas functions and to be mindful of memory usage.

Data Wrangling: The most time-consuming part of the project was data cleaning. The publish_time column had inconsistent formats, requiring the use of pd.to_datetime with errors='coerce' to handle unparseable values gracefully.

Building an Interactive App: This project provided my first experience with Streamlit. I learned how to create a basic web application to present data findings in an interactive and accessible way, going beyond static plots. The use of @st.cache_data was particularly important for optimizing app performance by caching the data loading process.

Complete Workflow: This assignment reinforced the importance of the entire data science workflow, from start to finish. It demonstrated that a complete project involves not just analysis, but also proper data preparation and a clear way to communicate the results to others.
