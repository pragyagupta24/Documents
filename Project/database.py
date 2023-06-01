from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship, backref
from sqlalchemy import func
from datetime import datetime

DB_NAME = 'database.sqlite'
DB_URL = f'sqlite:///{DB_NAME}'

Base = declarative_base()

class AutomobileImage(Base):
    __tablename__ = 'automobile_images'
    id = Column(Integer, primary_key=True)
    path = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    class Meta:
        ordering = ('-created_at',)

    def __repr__(self):
        return f'<Automobile Part {self.path}>'

    def __str__(self):
        return self.path

def opendb():
    engine = create_engine(DB_URL, echo=True)
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    return Session()

if __name__ == '__main__':
    engine = create_engine(DB_URL, echo=True)
    Base.metadata.create_all(engine)