from fastapi import FastAPI, HTTPException
app = FastAPI(title = "product service")

products={
    1: {"id": 1, "name": "laptop", "price": 10.0},
    2: {"id": 2, "name": "mouse", "price": 20.0},
}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product