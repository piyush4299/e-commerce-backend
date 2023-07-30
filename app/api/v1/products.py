import time
from fastapi import APIRouter, HTTPException, Depends
from app.models.product import ProductCreate, ProductUpdate
from app.services.product_service import ProductService
from app.api.v1.utils.generate_dummy_product import generate_dummy_product
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_all_products(productService: ProductService= Depends()):
    return await productService.get_all_products()

@router.post("/create-product")
async def create_product(product_data: ProductCreate, productService: ProductService = Depends()):
    product_dict = product_data.dict()
    product_dict["createdAt"] = int(time.time())
    return await productService.create_product(product_dict)

@router.post("/populate-dummy-products")
async def populateData(product_data: ProductCreate, productService: ProductService = Depends()):
    print('populate data')
    num_products_to_create = 5
    products_created = []
    
    for _ in range(num_products_to_create):
        product_data = generate_dummy_product()
        try:
            '''
                ProductCreate(**product_data) => is a way to unpack the data in dictionary format
                similar to creating an object of this ProductCreate class
            '''
            created_product = await productService.create_product(ProductCreate(**product_data))
            products_created.append(created_product)
        except Exception as e:
            print("Error: ",e)
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": f"{num_products_to_create} products created successfully.", "products": products_created}

@router.get("/getProduct/{product_id}")
async def get_product_by_id(product_id: str, productService: ProductService= Depends()):
    product = await productService.get_product_by_id(ObjectId(product_id))
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found!")
    return product

@router.put("/update/{product_id}")
async def update_product(product_id: str, product_data: ProductUpdate, productService: ProductService= Depends()):
    product_dict = product_data.dict(exclude_unset=True)
    product_dict['udpatedAt'] = int(time.time())
    product = await productService.get_product_by_id(ObjectId(product_id))
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found!")
    
    return await productService.update_product(ObjectId(product_id), product_dict)

@router.delete("/delete/{product_id}")
async def delete_product(product_id: str, productService: ProductService= Depends()):
    product = await productService.get_product_by_id(ObjectId(product_id))
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found!")
    return await productService.delete_product(ObjectId(product_id))

