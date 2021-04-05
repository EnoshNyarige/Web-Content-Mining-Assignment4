import streamlit as st
import pandas as pd
import pickle

from preprocessing_utils import *



html_temp = """
	<div style="background-color:blue;padding:10px">
	<h1 style="color:white;text-align:center;">News Article Clustering</h1>
    <h3 style="color:white;text-align:center;">Data Mining Assignment4 -  Web-Content Mining</h3>
    <h3 style="color:white;text-align:center;">Enosh Nyarige</h3>
	</div>
	"""


st.markdown(html_temp,unsafe_allow_html=True)

df = pd.read_csv('Articlesclusters.csv')

# Get user input
news_article = st.text_input("What is the content in the article you want to cluster?")
news_category = st.multiselect('Multiselect', ['Sports', 'Politics', 'Business', 'Arts/Culture/Celebrities '])
news_url = st.text_input("Link to the article: ")

if news_article and news_category and news_url:
    st.write("**Content in the News Article **: " , news_article)
    st.write("**Selected news category **:" , news_category)
    st.write("**Attached link to news rticle **:" , news_url)

    k_means = pickle.load(open('kmeans_model.pkl', 'rb'))
    tfidf_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    tfidf_pca = pickle.load(open('tfidf_pca.pkl', 'rb'))

    preprocessed_news_article = preprocess_article(news_article) 
    tfidf_article = tfidf_vectorizer.transform(np.array([preprocessed_news_article]))

    tfidf_pca_comp = tfidf_pca.transform(tfidf_article.toarray())

    st.write('The CLUSTERS')

# Create the clusters from the Dataframe
    clusterOne = df[df['clusters'] == 0][['category', 'article', 'clusters']]
    clusterTwo = df[df['clusters'] == 1][['category', 'article', 'clusters', 'url']]
    clusterThree = df[df['clusters'] == 2][['category', 'article', 'clusters', 'url']]
    clusterFour = df[df['clusters'] == 3][['category', 'article', 'clusters', 'url']]

if st.button("Cluster The Article"):
    articleCluster = k_means.predict(tfidf_pca_comp)

    if articleCluster == 0:
        st.write('This article is related to articles in cluster: ', str(1))
        st.write(clusterOne)

    elif articleCluster == 1:
        st.write('This article is related to articles in cluster: ', str(2))
        st.write(clusterTwo)

    elif articleCluster == 2:
        st.write('This article is related to articles in cluster: ', str(3))
        st.write(clusterThree)

    elif articleCluster == 3:
        st.write('This article is related to articles in cluster: ', str(4))
        st.write(clusterFour)
