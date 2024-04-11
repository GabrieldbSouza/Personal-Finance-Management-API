from database.database import db
from datetime import datetime

class Transaction(db.Model):
  trans_id = db.Column(db.Integer, primary_key = True)
  trans_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
  trans_date = db.Column(db.Date, nullable = False)
  trans_amount = db.Column(db.Float, nullable = False)

  def __repr__(self):
    return f"Transaction('{self.trans_id}','{self.trans_user_id}','{self.trans_date}','{self.trans_amount}')"