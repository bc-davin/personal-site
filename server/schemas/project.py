from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import datetime
from bson import ObjectId

class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    technologies: List[str] = Field(default_factory=list)
    github_url: Optional[HttpUrl] = None
    live_url: Optional[HttpUrl] = None
    image_url: Optional[str] = None
    featured: bool = Field(default=False)
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, min_length=1)
    technologies: Optional[List[str]] = None
    github_url: Optional[HttpUrl] = None
    live_url: Optional[HttpUrl] = None
    image_url: Optional[str] = None
    featured: Optional[bool] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class ProjectInDB(ProjectBase):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "title": "Personal Website",
                "description": "A full-stack personal website built with Angular and FastAPI",
                "technologies": ["Angular", "FastAPI", "MongoDB"],
                "github_url": "https://github.com/username/project",
                "featured": True
            }
        }
