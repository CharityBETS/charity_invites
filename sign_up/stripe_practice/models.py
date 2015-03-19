from .extensions import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(60), nullable=False)
    token_id = db.Column(db.String(60))

    def make_dict(self):
        return {"id": self.id,
                "date": self.date,
                "token_id": self.token_id}

class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bank_token = db.Column(db.String(60))
    name = db.Column(db.String(60), nullable=False)

    def make_dict(self):
        return {"id": self.id,
                "bank_token": self.bank_token,
                "name": self.name}
