import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("product_dataset_30.csv")


df["features"] = df["name"] + " " + df["category"] + " " + df["description"]


vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["features"])


similarity_matrix = cosine_similarity(tfidf_matrix)


def get_all_products():
    return df.to_dict(orient="records")


def search_products(query):
    result = df[df["name"].str.lower().str.contains(query.lower())]
    return result.to_dict(orient="records")


def recommend_products(product_name):
    product_name = product_name.lower()

    matches = df[df["name"].str.lower() == product_name]

    if matches.empty:
        return {"error": "Product not found"}

    idx = matches.index[0]

    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i in scores[1:6]:
        recommendations.append({
            "name": df.iloc[i[0]]["name"],
            "category": df.iloc[i[0]]["category"]
        })

    return {"recommendations": recommendations}


def recommend_by_category(category):
    result = df[df["category"].str.lower() == category.lower()]
    return result.to_dict(orient="records")