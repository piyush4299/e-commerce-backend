from faker import Faker

# Function to generate dummy product data
def generate_dummy_product():
    fake = Faker()
    product_data = {
        "name": fake.catch_phrase(max_nb_chars=90),
        "description": fake.text(max_nb_chars=230),
        "price": round(fake.random.uniform(10, 100), 2),
        "stockAvailable": fake.random_int(0, 100),
        "category": "Electronics",
        "isAvailableForSale": fake.boolean(),
        "images": [fake.image_url() for _ in range(fake.random_int(1, 5))],
        "specification": {
            "brand": fake.company(),
            "model": fake.word(),
            "color": fake.color_name(),
        },
    }
    return product_data