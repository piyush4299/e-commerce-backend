from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "e-commerce_db"

async def connect_to_database() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(MONGO_URI)
    await ping_connected_database(client)
    database = client[DATABASE_NAME]
    print(client[DATABASE_NAME])
    return database

async def close_database_connection(client: AsyncIOMotorClient):
    client.close()
    
async def ping_connected_database(client: AsyncIOMotorClient):
    # Send a ping to confirm a successful connection
    try:
        await client.admin.command('ping')
        print("Pinged your client connection. Connection with Mongodb seems to be good!!")
    except Exception as e:
        print(e)