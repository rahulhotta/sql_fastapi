from sqlalchemy.orm import Session

import models
import schemas


def get_user_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_user(db: Session, user):
    db_user = models.Student(id=user.id, name=user.name,
                             roll=user.roll, branch=user.branch)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, student_id, user):
    db_user = db.query(models.Student).get(student_id)
    if db_user:
        db_user.id = user.id
        db_user.name = user.name
        db_user.roll = user.roll
        db_user.branch = user.branch
        db.commit()
        db.refresh(db_user)
        return [db_user]
    return {"message": "User not found"}


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.Student).get(user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "Deleted Successfully"}
    return {"Error": "Student not found"}
