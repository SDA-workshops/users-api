from faker import Faker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.email})"

    @staticmethod
    def create_fake_user():
        fake = Faker()
        return User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
