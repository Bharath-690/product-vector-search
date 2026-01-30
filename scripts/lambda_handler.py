import json
import mysql.connector
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def lambda_handler(event, context=None):
    query = event.get("query")

    if not query:
        return {"error": "Query parameter is required"}

    # MySQL connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="croco@100216",
        database="product_vector_db"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT product_id, product_name FROM products_vectors")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    product_ids = [r[0] for r in rows]
    product_names = [r[1] for r in rows]

    # TF-IDF on products + query
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(product_names + [query]).toarray()

    query_vector = tfidf[-1].reshape(1, -1)
    product_vectors = tfidf[:-1]

    similarities = cosine_similarity(query_vector, product_vectors)[0]

    # Sort by similarity (desc)
    ranked = sorted(
        zip(product_ids, product_names, similarities),
        key=lambda x: x[2],
        reverse=True
    )

    # Deduplicate by product_name
    seen = set()
    results = []

    for pid, name, score in ranked:
        if name not in seen:
            seen.add(name)
            results.append({
                "product_id": pid,
                "product_name": name,
                "similarity_score": float(score)
            })
        if len(results) == 5:
            break

    return {
        "query": query,
        "top_matches": results
    }


# Local test
if __name__ == "__main__":
    test_event = {"query": "Apple iPhone 14 Pro"}
    print(json.dumps(lambda_handler(test_event), indent=2))
