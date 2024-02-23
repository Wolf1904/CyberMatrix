import streamlit as st
from newsapi import NewsApiClient
import matplotlib.pyplot as plt

api_key = st.secrets["newsapi_key"]

newsapi = NewsApiClient(api_key=api_key)

st.title("News")
st.subheader("News related to Business, Science and Technology.")
st.write("---")
st.markdown("<style> body { background-color: #f5f5f5; } </style>", unsafe_allow_html=True)

search_term = st.text_input("Search news by keyword:")
category = st.selectbox("Select category:", options=["business", "science", "technology"])

top_headlines = newsapi.get_top_headlines(q=search_term, category=category, language="en")

if top_headlines["status"] != "ok":
    st.error("Error fetching news:", top_headlines["message"]) # type: ignore
else:
    with st.sidebar:
        st.subheader("Filter by Source:")
        sources = [article["source"]["name"] for article in top_headlines["articles"]]
        selected_sources = st.multiselect("Select sources:", sources, default=sources)

    filtered_articles = [article for article in top_headlines["articles"] if article["source"]["name"] in selected_sources]

    for article in filtered_articles:
        col1, col2 = st.columns(2)

        with col1:
            try:
                st.image(article["urlToImage"], width=200)
            except AttributeError:
                st.write("No image available")

        with col2:
            st.markdown(f"<h3 style='color: rgb(217, 217, 226); font-weight: bold;'>{article['title']}</h3>", unsafe_allow_html=True)
            st.write(f"{article['description']}")
            st.write(f"<a href='{article['url']}' style='color: #007bff; text-decoration: none;'>Source: {article['source']['name']}</a>", unsafe_allow_html=True)

        if "sentiment" in article:
            st.bar_chart(article["sentiment"], use_container_width=True)

        st.write("---")
