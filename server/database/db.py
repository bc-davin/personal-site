from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from config.settings import settings

client: AsyncIOMotorClient = None
database = None

async def connect_to_mongo():
    """Connect to MongoDB on application startup"""
    global client, database
    try:
        client = AsyncIOMotorClient(settings.MONGODB_URL, server_api=ServerApi('1'))
        database = client[settings.DATABASE_NAME]
        # Test the connection
        await database.command('ping')
        print(f"✅ Connected to MongoDB database: {settings.DATABASE_NAME}")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        raise e

async def close_mongo_connection():
    """Close MongoDB connection on application shutdown"""
    global client
    if client:
        client.close()
        print("✅ Closed MongoDB connection")

def get_database():
    """Get database instance"""
    return database
