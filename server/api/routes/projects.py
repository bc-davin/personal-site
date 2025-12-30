from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime
from bson import ObjectId
from database.db import get_database
from schemas.project import ProjectCreate, ProjectUpdate, ProjectInDB
from config.settings import settings

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=ProjectInDB, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate):
    """Create a new project"""
    db = get_database()
    project_dict = project.model_dump()
    project_dict["created_at"] = datetime.utcnow()
    project_dict["updated_at"] = datetime.utcnow()
    
    result = await db[settings.PROJECTS_COLLECTION].insert_one(project_dict)
    created_project = await db[settings.PROJECTS_COLLECTION].find_one({"_id": result.inserted_id})
    
    created_project["_id"] = str(created_project["_id"])
    return ProjectInDB(**created_project)

@router.get("/", response_model=List[ProjectInDB])
async def get_all_projects(featured_only: bool = False, skip: int = 0, limit: int = 100):
    """Get all projects"""
    db = get_database()
    query = {"featured": True} if featured_only else {}
    
    cursor = db[settings.PROJECTS_COLLECTION].find(query).skip(skip).limit(limit).sort("created_at", -1)
    projects = await cursor.to_list(length=limit)
    
    for project in projects:
        project["_id"] = str(project["_id"])
    
    return [ProjectInDB(**project) for project in projects]

@router.get("/{project_id}", response_model=ProjectInDB)
async def get_project(project_id: str):
    """Get a specific project by ID"""
    db = get_database()
    
    if not ObjectId.is_valid(project_id):
        raise HTTPException(status_code=400, detail="Invalid project ID format")
    
    project = await db[settings.PROJECTS_COLLECTION].find_one({"_id": ObjectId(project_id)})
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project["_id"] = str(project["_id"])
    return ProjectInDB(**project)

@router.put("/{project_id}", response_model=ProjectInDB)
async def update_project(project_id: str, project_update: ProjectUpdate):
    """Update a project"""
    db = get_database()
    
    if not ObjectId.is_valid(project_id):
        raise HTTPException(status_code=400, detail="Invalid project ID format")
    
    update_data = {k: v for k, v in project_update.model_dump(exclude_unset=True).items()}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    update_data["updated_at"] = datetime.utcnow()
    
    result = await db[settings.PROJECTS_COLLECTION].update_one(
        {"_id": ObjectId(project_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    
    updated_project = await db[settings.PROJECTS_COLLECTION].find_one({"_id": ObjectId(project_id)})
    updated_project["_id"] = str(updated_project["_id"])
    
    return ProjectInDB(**updated_project)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: str):
    """Delete a project"""
    db = get_database()
    
    if not ObjectId.is_valid(project_id):
        raise HTTPException(status_code=400, detail="Invalid project ID format")
    
    result = await db[settings.PROJECTS_COLLECTION].delete_one({"_id": ObjectId(project_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return None
