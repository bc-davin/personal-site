import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "personal_website")
    
    # Collections
    BLOGS_COLLECTION: str = "blogs"
    PROJECTS_COLLECTION: str = "projects"
    EXPERIENCES_COLLECTION: str = "experiences"
    
    # CORS
    ALLOWED_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "").split(",") if os.getenv("ALLOWED_ORIGINS") else [
        "http://localhost:4200",  # Angular dev server
        "http://localhost:3000",
        "https://*.vercel.app",  # Vercel preview deployments
    ]

settings = Settings()
