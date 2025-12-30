from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime
from bson import ObjectId
from database.db import get_database
from schemas.experience import ExperienceCreate, ExperienceUpdate, ExperienceInDB
from config.settings import settings

router = APIRouter(prefix="/experiences", tags=["experiences"])

@router.post("/", response_model=ExperienceInDB, status_code=status.HTTP_201_CREATED)
async def create_experience(experience: ExperienceCreate):
    """Create a new experience"""
    db = get_database()
    experience_dict = experience.model_dump()
    experience_dict["created_at"] = datetime.utcnow()
    experience_dict["updated_at"] = datetime.utcnow()
    
    result = await db[settings.EXPERIENCES_COLLECTION].insert_one(experience_dict)
    created_experience = await db[settings.EXPERIENCES_COLLECTION].find_one({"_id": result.inserted_id})
    
    created_experience["_id"] = str(created_experience["_id"])
    return ExperienceInDB(**created_experience)

@router.get("/", response_model=List[ExperienceInDB])
async def get_all_experiences(current_only: bool = False, skip: int = 0, limit: int = 100):
    """Get all experiences"""
    db = get_database()
    query = {"is_current": True} if current_only else {}
    
    cursor = db[settings.EXPERIENCES_COLLECTION].find(query).skip(skip).limit(limit).sort("start_date", -1)
    experiences = await cursor.to_list(length=limit)
    
    for experience in experiences:
        experience["_id"] = str(experience["_id"])
    
    return [ExperienceInDB(**experience) for experience in experiences]

@router.get("/{experience_id}", response_model=ExperienceInDB)
async def get_experience(experience_id: str):
    """Get a specific experience by ID"""
    db = get_database()
    
    if not ObjectId.is_valid(experience_id):
        raise HTTPException(status_code=400, detail="Invalid experience ID format")
    
    experience = await db[settings.EXPERIENCES_COLLECTION].find_one({"_id": ObjectId(experience_id)})
    
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    experience["_id"] = str(experience["_id"])
    return ExperienceInDB(**experience)

@router.put("/{experience_id}", response_model=ExperienceInDB)
async def update_experience(experience_id: str, experience_update: ExperienceUpdate):
    """Update an experience"""
    db = get_database()
    
    if not ObjectId.is_valid(experience_id):
        raise HTTPException(status_code=400, detail="Invalid experience ID format")
    
    update_data = {k: v for k, v in experience_update.model_dump(exclude_unset=True).items()}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    update_data["updated_at"] = datetime.utcnow()
    
    result = await db[settings.EXPERIENCES_COLLECTION].update_one(
        {"_id": ObjectId(experience_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    updated_experience = await db[settings.EXPERIENCES_COLLECTION].find_one({"_id": ObjectId(experience_id)})
    updated_experience["_id"] = str(updated_experience["_id"])
    
    return ExperienceInDB(**updated_experience)

@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_experience(experience_id: str):
    """Delete an experience"""
    db = get_database()
    
    if not ObjectId.is_valid(experience_id):
        raise HTTPException(status_code=400, detail="Invalid experience ID format")
    
    result = await db[settings.EXPERIENCES_COLLECTION].delete_one({"_id": ObjectId(experience_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Experience not found")
    
    return None
