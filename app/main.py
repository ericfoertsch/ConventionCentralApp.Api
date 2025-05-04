from fastapi import FastAPI
from app.routers import vendor_router

app = FastAPI()

app.include_router(vendor_router.router)
