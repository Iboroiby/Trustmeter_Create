from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.review import ReviewCreate, ReviewOut
from app.models.review import Review
from app.models.listing import Listing
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=ReviewOut)
def create_review(review: ReviewCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    listing = db.query(Listing).filter(Listing.id == review.listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    new_review = Review(**review.dict(), user_id=user.id, listing_id=listing.id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
