from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new-user/{user_id}")
def create_user(user_id: int, user: schemas.Studnet, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Student already registered")
    crud.create_user(db=db, user=user)
    return {"message":"Student added successfully"}


@app.get("/all-users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users


@app.get("/get-user-by-id/")
def read_users_bt_id(student_id: int, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, student_id)
    return users


@app.put("/update-user/{student_id}")
def read_users_bt_id(student_id: int, user: schemas.Studnet, db: Session = Depends(get_db)):
    return crud.update_user(db, student_id, user)

@app.delete("/delete-user/{student_id}")
def read_users_bt_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_user(db, student_id)
    except Exception as e:
        return {"Error":e.args}
        



