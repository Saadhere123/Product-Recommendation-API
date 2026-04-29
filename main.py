from fastapi import FastAPI
from pydantic import BaseModel
from recommender import (
    get_all_products,
    recommend_products,
    search_products,
    recommend_by_category
)

app = FastAPI(
    title="Product Recommendation API",
    description="AI Backend Internship Task 12",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Product Recommendation API is running"}


@app.get("/products")
def products():
    return {"products": get_all_products()}


@app.get("/recommend/{product_name}")
def recommend(product_name: str):
    return recommend_products(product_name)


@app.get("/search")
def search(query: str):
    return {"results": search_products(query)}


class UserPreference(BaseModel):
    category: str


@app.post("/recommend/user")
def recommend_user(user: UserPreference):
    return {"recommendations": recommend_by_category(user.category)}