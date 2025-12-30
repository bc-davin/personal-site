from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database.db import connect_to_mongo, close_mongo_connection
from api.routes import blogs, projects, experiences
from config.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()

app = FastAPI(
    title="Personal Website API",
    description="API for personal blog, projects, and experiences",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(blogs.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(experiences.router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Personal Website API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
