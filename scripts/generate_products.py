import csv
import random

# Base product lists
electronics = [
    "Apple iPhone 14",
    "Apple iPhone 14 Pro",
    "Apple iPhone 13",
    "Samsung Galaxy S21",
    "Samzung Galaxy S21",   # typo
    "OnePlus 11",
    "Redmi Note 12",
    "Sony WH-1000XM5 Headphones",
    "Boat Rockerz 450 Headphones"
]

fashion = [
    "Nike Air Max Shoes",
    "Nike AirMax Shoes",   # similar name
    "Adidas Running T-Shirt",
    "Puma Sports Shorts",
    "Levi's Blue Jeans",
    "Allen Solly Formal Shirt",
    "US Polo Casual Shirt"
]

groceries = [
    "Aashirvaad Wheat Flour",
    "Ashirwad Wheat Flower",   # typo
    "Tata Salt",
    "Fortune Sunflower Oil",
    "Maggi Noodles",
    "Maggie Noodles",          # typo
    "Dabur Honey",
    "Amul Butter"
]

all_products = electronics + fashion + groceries

# Generate 500 products
rows = []
for product_id in range(1, 501):
    product_name = random.choice(all_products)
    rows.append([product_id, product_name])

# Write to CSV
output_path = "data/products.csv"
with open(output_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product_id", "product_name"])
    writer.writerows(rows)

print(f"✅ Generated {len(rows)} products and saved to {output_path}")
