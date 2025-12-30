from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime
from bson import ObjectId
from database.db import get_database
from schemas.blog import BlogCreate, BlogUpdate, BlogInDB
from config.settings import settings

router = APIRouter(prefix="/blogs", tags=["blogs"])

@router.post("/", response_model=BlogInDB, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogCreate):
    """Create a new blog post"""
    db = get_database()
    blog_dict = blog.model_dump()
    blog_dict["created_at"] = datetime.utcnow()
    blog_dict["updated_at"] = datetime.utcnow()
    
    result = await db[settings.BLOGS_COLLECTION].insert_one(blog_dict)
    created_blog = await db[settings.BLOGS_COLLECTION].find_one({"_id": result.inserted_id})
    
    created_blog["_id"] = str(created_blog["_id"])
    return BlogInDB(**created_blog)

@router.get("/", response_model=List[BlogInDB])
async def get_all_blogs(published_only: bool = False, skip: int = 0, limit: int = 100):
    """Get all blog posts"""
    db = get_database()
    query = {"published": True} if published_only else {}
    
    cursor = db[settings.BLOGS_COLLECTION].find(query).skip(skip).limit(limit).sort("created_at", -1)
    blogs = await cursor.to_list(length=limit)
    
    for blog in blogs:
        blog["_id"] = str(blog["_id"])
    
    return [BlogInDB(**blog) for blog in blogs]

@router.get("/{blog_id}", response_model=BlogInDB)
async def get_blog(blog_id: str):
    """Get a specific blog post by ID"""
    db = get_database()
    
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID format")
    
    blog = await db[settings.BLOGS_COLLECTION].find_one({"_id": ObjectId(blog_id)})
    
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog["_id"] = str(blog["_id"])
    return BlogInDB(**blog)

@router.put("/{blog_id}", response_model=BlogInDB)
async def update_blog(blog_id: str, blog_update: BlogUpdate):
    """Update a blog post"""
    db = get_database()
    
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID format")
    
    update_data = {k: v for k, v in blog_update.model_dump(exclude_unset=True).items()}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    update_data["updated_at"] = datetime.utcnow()
    
    result = await db[settings.BLOGS_COLLECTION].update_one(
        {"_id": ObjectId(blog_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    updated_blog = await db[settings.BLOGS_COLLECTION].find_one({"_id": ObjectId(blog_id)})
    updated_blog["_id"] = str(updated_blog["_id"])
    
    return BlogInDB(**updated_blog)

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: str):
    """Delete a blog post"""
    db = get_database()
    
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID format")
    
    result = await db[settings.BLOGS_COLLECTION].delete_one({"_id": ObjectId(blog_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return None
