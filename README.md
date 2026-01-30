## 🔍 Vector Search Demo

This project implements a semantic product search system using vector embeddings and cosine similarity.

### Features
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

