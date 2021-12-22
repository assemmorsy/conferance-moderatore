from sqlalchemy.orm import Session

from . import models, schemas

# get enitiy by id
def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


def get_talk(db: Session, talk_id: int):
    return db.query(models.Talk).filter(models.Talk.id == talk_id).first()


def get_session(db: Session, session_id: int):
    return db.query(models.Session).filter(models.Session.id == session_id).first()


# get enitiy by name


def get_doctor_by_name(db: Session, name: str):
    return db.query(models.Doctor).filter(models.Doctor.name == name).first()


def get_talk_by_name(db: Session, name: str):
    return db.query(models.Talk).filter(models.Talk.name == name).first()


def get_session_by_name(db: Session, name: str):
    return db.query(models.Session).filter(models.Session.name == name).first()


# get all instance of an intity


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()


def get_talks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Talk).offset(skip).limit(limit).all()


def get_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Session).offset(skip).limit(limit).all()


# create instance of an intity


def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(
        name=doctor.name, file_path=doctor.file_path, talk_id=doctor.talk_id
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def create_talk(db: Session, talk: schemas.TalkCreate):
    db_talk = models.Talk(
        name=talk.name, start_time=talk.start_time, session_id=talk.session_id
    )
    db.add(db_talk)
    db.commit()
    db.refresh(db_talk)
    return db_talk


def create_session(db: Session, session: schemas.SessionCreate):
    db_session = models.Session(name=session.name, date=session.date)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


# update created instance of an intity


def update_doctor(db: Session, doctor_id: int, doctor: schemas.Doctor):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if db_doctor:
        db_doctor.name = doctor.name
        db_doctor.file_path = doctor.file_path
        db.commit()
        db.refresh(db_doctor)
    return db_doctor


def update_talk(db: Session, talk_id: int, talk: schemas.Talk):
    db_talk = db.query(models.Talk).filter(models.Talk.id == talk_id).first()
    if db_talk:
        db_talk.name = talk.name
        db_talk.start_time = talk.start_time
        db.commit()
        db.refresh(db_talk)
    return db_talk


def update_session(db: Session, session_id: int, session: schemas.Session):
    db_session = (
        db.query(models.Session).filter(models.Session.id == session_id).first()
    )
    if db_session:
        db_session.name = session.name
        db_session.date = session.date
        db.commit()
        db.refresh(db_session)
    return db_session


# delete instance


def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return None


def delete_talk(db: Session, talk_id: int):
    db_talk = db.query(models.Talk).filter(models.Talk.id == talk_id).first()
    if db_talk:
        db.delete(db_talk)
        db.commit()
    return None


def delete_talk(db: Session, session_id: int):
    db_session = (
        db.query(models.Session).filter(models.Session.id == session_id).first()
    )
    if db_session:
        db.delete(db_session)
        db.commit()
    return None
