from db.models import User


class UsersIterator:
    def __init__(self, session):
        self.session = session
        self.cursor = None

    def __iter__(self):
        engine = self.session.get_bind()
        self.cursor = engine.execute("SELECT * FROM users")
        return self

    def __next__(self):
        return next(self.cursor)


def users(session):
    for user in session.query(User):
        yield user
