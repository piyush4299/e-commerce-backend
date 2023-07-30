from fastapi import FastAPI
from app.main import router as app_router
from app.db import connect_to_database, close_database_connection

app = FastAPI()

app.include_router(app_router, prefix="/app")

# Executes when server starts
@app.on_event("startup")
async def startup_db_client():
    '''
        This block is reserved for setting up indexes, redis setup, etc
    '''
    app.mongodb_client = await connect_to_database()

# Executes when server stops
@app.on_event("shutdown")
async def shutdown_db_client():
    '''
        This block is reserved for actions to be performed when server stops such as closing all connections
    '''
    await close_database_connection(app.mongodb_client)