from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Post, User
from fake_data import generate_fake_data
from datetime import datetime

app = FastAPI(title="Blog API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize fake data
posts, users = generate_fake_data()

@app.get("/")
async def root():
    return {"message": "Welcome to the Blog API"}

@app.get("/posts")
async def get_posts():
    import json
    with open("jsonfiles/blog.json") as f:
        data = json.load(f)
    return {"posts": data["featuredProducts"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)