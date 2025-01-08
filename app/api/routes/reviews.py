from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.listing import ProductCreate
from app.schemas.review import ReviewCreate, ReviewResponse
from app.services.product_service import get_product_by_url, create_product
from app.services.review_service import create_review
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/reviews/", response_model=ReviewResponse)
def create_review_for_product(
    review: ReviewCreate,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    # Check or create product
    db_product = get_product_by_url(db, product.url)
    if not db_product:
        db_product = create_product(db, product)

    # Create review
    review.product_id = db_product.id
    return create_review(db, review)
