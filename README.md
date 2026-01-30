## 🔍 Vector Search Demo

This project implements a semantic product search system using vector embeddings and cosine similarity.

## Features
- Finds semantically similar products, not just exact text matches
- Handles closely related product names (e.g., *Apple iPhone 14 Pro* vs *Apple iPhone 14*)
- Supports typo tolerance (e.g., *Samzung Galaxy S21*)
- Returns **top-5 unique products** ranked by similarity score
- Filters out duplicate or repetitive results for cleaner output

### Example Output
```json
{
  "query": "Apple iPhone 14 Pro",
  "top_matches": [
    {
      "product_id": 33,
      "product_name": "Apple iPhone 14 Pro",
      "similarity_score": 1.0
    },
    {
      "product_id": 39,
      "product_name": "Apple iPhone 14",
      "similarity_score": 0.83
    }
  ]
}
```

## 💻 Tech Stack

- Python 3.x  
- TF-IDF vectorization (scikit-learn)  
- MySQL (for storing products and vectors)  
- Cosine similarity (for vector search)

## 🚀 How to Run Locally

### 1.Clone the repository:
```json

git clone https://github.com/Bharath-690/product-vector-search.git
cd product-vector-search
```
### 2.Set up Python environment:
```json

pip install -r requirements.txt
```

### 3.Create MySQL database and table:
```json

CREATE DATABASE product_vector_db;
USE product_vector_db;
SOURCE sql/create_table.sql;
```

### 4.Generate product data with edge cases:
```json

python scripts/generate_products.py
```
This generates data/products.csv with 500 products.

### 5.Generate TF-IDF embeddings and store in MySQL:
```json

python scripts/embed_products.py
```
(Make sure to update your MySQL credentials in embed_products.py)

### 6.Run the similarity search (simulate AWS Lambda):
```json

python scripts/lambda_handler.py
```
Example query is hardcoded in the script, or you can modify the test_event dictionary.

## 🧠 Vector Similarity Logic Explained

Product names are converted into numerical vectors using TF-IDF, which reflects the importance of each word relative to all product names.

Cosine similarity measures the angle between the query vector and product vectors, indicating how similar they are.

The system ranks all products based on similarity scores and returns the top 5 unique matches.

This approach allows handling of near duplicates, spelling errors, and similar phrases effectively without needing heavy machine learning models.

## ☁️ AWS Lambda Notes

*lambda_handler.py mimics an AWS Lambda function handler

*Accepts a query string and generates embeddings using the same TF-IDF logic

*Queries MySQL and returns the most similar products

*AWS account is not required for local testing

*Can be deployed to AWS Lambda with proper configuration

*Terraform scripts are optional and can be added separately

## 📝 Assumptions and Limitations

*TF-IDF embeddings do not capture deep semantic meaning like transformer models

*MySQL stores vectors as JSON strings (not ideal for very large datasets)

*Duplicate product names exist by design and are handled via deduplication logic

*No real-time indexing or incremental updates

*Typo tolerance is limited by token matching in TF-IDF

## 📂 Repository Structure
```json
product-vector-search/
├── data/                  # Generated CSV product data
├── scripts/               # Python scripts for generation, embedding, and Lambda handler
├── sql/                   # SQL scripts for database creation
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── .gitignore             # Git ignore rules
```

## 📧 Contact

Created by Nesai Bharath
Feel free to reach out on

GitHub: https://github.com/Bharath-690

LinkedIn: https://www.linkedin.com/in/nesai-bharath-741349293


