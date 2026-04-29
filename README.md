
Product Recommendation API

Project Description
This project is built using FastAPI and Machine Learning.
It recommends products based on product similarity using TF-IDF and Cosine Similarity.

Features
- Product Listing API
- Product Recommendation API
- Search API
- User Preference Recommendation
- Swagger UI Docs

Installation

pip install -r requirements.txt

Run Project

uvicorn main:app --reload

Open Browser

http://127.0.0.1:8000

Swagger Docs

http://127.0.0.1:8000/docs

API Endpoints

GET /
GET /products
GET /recommend/iPhone 14
GET /search?query=iphone
POST /recommend/user

Body:
{
  "category": "Laptop"
}


HOW TO RUN

1. Create Folder:
Product_Recommendation_API

2. Save all files inside folder

3. Open terminal

cd Product_Recommendation_API

4. Install libraries

pip install -r requirements.txt

5. Run FastAPI server

uvicorn main:app --reload

6. Open:
http://127.0.0.1:8000/docs
