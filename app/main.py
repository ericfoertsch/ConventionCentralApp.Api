from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import vendor_router, convention_router, event_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allows the frontend running on port 5173
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(vendor_router.router)
app.include_router(convention_router.router)
app.include_router(event_router.router)
