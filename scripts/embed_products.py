import json
import pandas as pd
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer

# Load products CSV
df = pd.read_csv("data/products.csv")

# Generate TF-IDF embeddings
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df["product_name"]).toarray()

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="croco@100216",
    database="product_vector_db"
)
cursor = conn.cursor()

# Insert vectors into DB
for idx, row in df.iterrows():
    vector_json = json.dumps(vectors[idx].tolist())
    cursor.execute(
        "INSERT INTO products_vectors (product_id, product_name, vector) VALUES (%s, %s, %s)",
        (int(row["product_id"]), row["product_name"], vector_json)
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Product embeddings generated and stored in MySQL")
