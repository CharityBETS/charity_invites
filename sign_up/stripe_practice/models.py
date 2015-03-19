from .extensions import db


class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    charity_name = db.Column(db.String(60))
    date = db.Column(db.String(60), nullable=False)

    def make_dict(self):
        return {"id": self.id,
                "bank_token": self.bank_token,
                "name": self.name}
