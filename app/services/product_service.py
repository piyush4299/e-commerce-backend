from fastapi import Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.product import Product, ProductCreate, ProductUpdate
from app.db import connect_to_database

class ProductService:
    def __init__(self, db: AsyncIOMotorClient = Depends(connect_to_database)):
        self.db = db
        self.collection = self.db["products"]
    
    async def get_all_products(self):
        try:
            cursor = self.collection.find()
            all_products = await cursor.to_list(None)
            print("All product records from DB", all_products)
            return {'status': 200, 'message': 'success', 'products': str(all_products)}
        except Exception as e:
            print("Something went wrong with getting all products record: ", e)
            return {'status': 500, 'message': 'Something went wrong'}
       
    async def get_product_by_id(self, product_id: str):
        try:
            product = await self.collection.find_one({"_id": product_id})
            if product:
                print("product found with passed in id successfully from DB", product)
                return {'status': 200, 'message': 'success', "product": str(product)}
            else:
                return {'status': 404, 'message': 'product not found'}
        except Exception as e:
            print("Something went wrong with getting product: ", e)
            return {'status': 500, 'message': 'Something went wrong'}
    
    async def create_product(self, product: ProductCreate):
        try:
            await self.collection.insert_one(product)
            return {"statusCode": 200, "message": "Added product successfully", "added_product": str(product)}
        except Exception as e:
            print("Something went wrong with adding product: ", e)
            return {'status': 500, 'message': 'Something went wrong'}

    async def update_product(self, product_id: str, product_data: ProductUpdate):
        try:
            product = await self.collection.update_one({"_id": product_id}, {"$set": product_data})
            if product.modified_count:
                print("product found and record updated in DB", product)
                return {'status': 200, 'message': 'success', "updated_product": str(product)}
            else:
                return {'status': 404, 'message': 'product not found to update'}
        except Exception as e:
            print("Something went wrong with updating product: ", e)
            return {'status': 500, 'message': 'Something went wrong'}
    
    async def delete_product(self, product_id: str):
        try:
            product = await self.collection.delete_one({"_id": product_id})
            print("Student record deleted successfully from DB", product)
            return {'status': 200, 'message': 'success'}
        except Exception as e:
            print("Something went wrong with deleting product: ", e)
            return {'status': 500, 'message': 'Something went wrong'}