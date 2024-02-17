import streamlit as st
from newsapi import NewsApiClient
import matplotlib.pyplot as plt  # For charts (optional)

# Retrieve API key from secrets
api_key = st.secrets["newsapi_key"]

# Create NewsAPI client
newsapi = NewsApiClient(api_key=api_key)

# Set page title and background color
st.title("News")
st.subheader("News related to Business, Science and Technology.")
st.write("---")
st.markdown("<style> body { background-color: #f5f5f5; } </style>", unsafe_allow_html=True)

# Create layout with search, columns, and sidebar
search_term = st.text_input("Search news by keyword:")
category = st.selectbox("Select category:", options=["business", "science", "technology"])

# Fetch top headlines
top_headlines = newsapi.get_top_headlines(q=search_term, category=category, language="en")

# Check for API errors
if top_headlines["status"] != "ok":
    st.error("Error fetching news:", top_headlines["message"]) # type: ignore
else:
    # Sidebar for filtering and options (optional)
    with st.sidebar:
        st.subheader("Filter by Source:")
        sources = [article["source"]["name"] for article in top_headlines["articles"]]
        selected_sources = st.multiselect("Select sources:", sources, default=sources)

    # Filter articles based on selected sources (optional)
    filtered_articles = [article for article in top_headlines["articles"] if article["source"]["name"] in selected_sources]

    # Process and display articles
    for article in filtered_articles:
        col1, col2 = st.columns(2)  # Adjust column sizes as needed

        with col1:
            try:
                st.image(article["urlToImage"], width=200)
            except AttributeError:
                st.write("No image available")

        with col2:
            st.markdown(f"<h3 style='color: rgb(217, 217, 226); font-weight: bold;'>{article['title']}</h3>", unsafe_allow_html=True)
            st.write(f"{article['description']}")
            st.write(f"<a href='{article['url']}' style='color: #007bff; text-decoration: none;'>Source: {article['source']['name']}</a>", unsafe_allow_html=True)

        # Add a chart (optional)
        if "sentiment" in article:  # Assuming sentiment analysis is done
            st.bar_chart(article["sentiment"], use_container_width=True)

        st.write("---")

# Optional additions:
# - Dark mode using st.beta_set_page_config(theme="dark")
# - Custom CSS for more granular styling
# - Interactive filters using st.slider, st.date_picker, etc.

