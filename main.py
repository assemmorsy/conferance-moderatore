from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get enitiy by id


@app.get("/doctors/{doctor_id}", response_model=schemas.Doctor)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return db_doctor


@app.get("/talks/{talk_id}", response_model=schemas.Talk)
def read_talk(talk_id: int, db: Session = Depends(get_db)):
    db_talk = crud.get_talk(db, talk_id=talk_id)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk


# get all instance of an intity


@app.get("/doctors/", response_model=List[schemas.Doctor])
def read_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db, skip=skip, limit=limit)
    return doctors


@app.get("/talks/", response_model=List[schemas.Talk])
def read_talks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    talks = crud.get_talks(db, skip=skip, limit=limit)
    return talks


@app.get("/sessions/", response_model=List[schemas.Session])
def read_talks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sessions = crud.get_sessions(db, skip=skip, limit=limit)
    return sessions


# get enitiy by name


@app.get("/doctorsByName/", response_model=schemas.Doctor)
def read_doctor_name(doctor_name: str = "", db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor_by_name(db, name=doctor_name)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor


@app.get("/talksByName/", response_model=schemas.Talk)
def read_talk_name(talk_name: str = "", db: Session = Depends(get_db)):
    db_talk = crud.get_talk_by_name(db, name=talk_name)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk


# create instance of an intity


@app.post("/doctors/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor_by_name(db, name=doctor.name)
    if db_doctor:
        raise HTTPException(status_code=400, detail="Doctor already registered")
    return crud.create_doctor(db=db, doctor=doctor)


@app.post("/talks/", response_model=schemas.Talk)
def create_talk(talk: schemas.TalkCreate, db: Session = Depends(get_db)):
    return crud.create_talk(db=db, talk=talk)


@app.post("/sessions/", response_model=schemas.Session)
def create_session(session: schemas.SessionCreate, db: Session = Depends(get_db)):
    return crud.create_session(db=db, session=session)


# update created instance of an intity


@app.put("/doctors/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(
    doctor_id: int, doctor: schemas.Doctor, db: Session = Depends(get_db)
):
    db_doctor = crud.get_doctor(db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor is not founded")
    return crud.update_doctor(db=db, doctor_id=doctor_id, doctor=doctor)


@app.put("/talks/{talk_id}", response_model=schemas.Talk)
def update_doctor(talk_id: int, talk: schemas.Talk, db: Session = Depends(get_db)):
    db_talk = crud.get_talk(db, talk_id=talk_id)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk is not founded")
    return crud.update_talk(db=db, talk_id=talk_id, talk=talk)


# delete instance


@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor is not founded")
    return crud.delete_doctor(db=db, doctor_id=doctor_id)


@app.delete("/talks/{talk_id}")
def delete_talk(talk_id: int, db: Session = Depends(get_db)):
    db_talk = crud.get_talk(db, talk_id=talk_id)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk is not founded")
    return crud.delete_talk(db=db, talk_id=talk_id)
