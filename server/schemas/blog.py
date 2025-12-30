from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class BlogBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    excerpt: Optional[str] = Field(None, max_length=500)
    tags: List[str] = Field(default_factory=list)
    published: bool = Field(default=False)
    featured_image: Optional[str] = None
    author: str = Field(default="Admin")

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    excerpt: Optional[str] = Field(None, max_length=500)
    tags: Optional[List[str]] = None
    published: Optional[bool] = None
    featured_image: Optional[str] = None
    author: Optional[str] = None

class BlogInDB(BlogBase):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "title": "My First Blog Post",
                "content": "This is the content of my blog post...",
                "excerpt": "A short excerpt",
                "tags": ["python", "fastapi"],
                "published": True,
                "author": "John Doe"
            }
        }
