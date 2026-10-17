# CICD-2 Two FastAPI Microservices
with HTTPX

---

##Lab 5 Two FastAPI Microservices
with HTTPX


Two FastAPI Microservices
with HTTPX

This project runs two FastAPI services. The User API uses HTTPX to request product information from the Product Service.

## Running the services

Run these commands in two separate Codespaces terminals.

Terminal 1 – Product Service (port 8001):
python -m uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload

Terminal 2 – User API (port 8000):
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Use the Codespaces Ports tab to open port 8000, then add /docs to the URL to test the User API.

## Product endpoint
GET /api/products/{product_id} retrieves a product through the User API.
For example, /api/products/1 returns:

{"id": 1, "name": "Laptop", "price": 899.0}

A missing product returns 404. If the Product Service is unavailable, the User API returns 503.
Configuration
PRODUCT_SERVICE_URL sets the address the User API uses to contact the Product Service. It defaults to http://127.0.0.1:8001 in Codespaces.
For separate Docker containers in a future lab, it can be set to http://product-service:8001 without changing the application code.

## Testing
Run:
python -m pytest

## Lab5 structure

app/   # Existing User API
├── __init__.py
├── main.py   
├── database.py   
├── models.py  
├── schemas.py   
└── product_client.py  

product_service/  
├── __init__.py
└── main.py

tests/
├── conftest.py  
├── test_users.py   
└── test_remote_products.py  

---

project-name/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── services.py
│   └── models.py
│   
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── requirements.txt
├── README.md
└── .gitignore

---
```
