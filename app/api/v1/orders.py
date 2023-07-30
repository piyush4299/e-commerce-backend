from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_dummy_response():
    return {"statusCode": 200, "message": "Welcome to out e-commerce Orders Work in progress"}