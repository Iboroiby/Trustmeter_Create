from fastapi import FastAPI
from app.api.routes import auth, users, listings, reviews, admin

app = FastAPI(
    title="TrustMeter",
    description="A web app for reviews and ratings.",
    version="1.0.0"
)

# Include all routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(listings.router, prefix="/listings", tags=["Listings"])
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)