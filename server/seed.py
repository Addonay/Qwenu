import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomprj.settings')

django.setup()

# from products.models import Product
from category.models import Category
# from reviews.models import Rating

def seed_categories():
    categories = [
        'Electronics', 'Clothing', 'Home & Kitchen', 'Beauty & Personal Care', 'Toys & Games', 'Grocery & Gourmet Food',
        'Pet Supplies', 'Office Products', 'Software', 'Musical Instruments',
        'Sports & Outdoors', 'Books', 'Gaming Accessories', 'Cell Phones & Accessories', 'Computers & Accessories',
        'Camera & Photo', 'Home Audio & Theater', 'Wearable Technology',  'Furniture', 'Home Décor', 'Outdoor Recreation', 'Exercise & Fitness',
        'Cycling', 'Hunting & Fishing', 
        'Virtual Reality', 'Drones', 'Fitness Trackers', 'Health Monitors'
    ]

    for category_name in categories:
        Category.objects.create(name=category_name)

def seed_products():
    pass

def seed_data():
    seed_categories()

if __name__ == "__main__":
    seed_data()