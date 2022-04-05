from db.models import Base, User
from db.session import Session


def main():
    session = Session()
    Base.metadata.create_all(session.get_bind())
    print("Preparing users...")
    fake_users = [
        User.create_fake_user() for _ in range(100)
    ]
    session.add_all(fake_users)
    session.commit()
    print("Done")


if __name__ == "__main__":
    main()
