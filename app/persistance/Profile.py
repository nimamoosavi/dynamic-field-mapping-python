from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profile'
    customer_id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    status = Column(String)
    address_line = Column(String)
    city = Column(String)
    province = Column(String)
    postal_code = Column(String)

# Database setup
engine = create_engine('sqlite:///profiles.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example of inserting a profile
profile = Profile(customer_id="123", firstname="John", lastname="Doe")
session.add(profile)
session.commit()
