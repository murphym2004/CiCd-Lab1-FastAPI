import os   
import httpx

product_service_url = os.getenv("PRODUCT_SERVICE_URL", "https://127.0.0.1:8001")

def fetch_product(product_id: int) ->dict:
    response = httpx.get(f"{product_service_url}/products/{product_id}",timeout=3.0)
    response.raise_for_status()
    return response.json()

def get_product_fetcher():
    return fetch_product