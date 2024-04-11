from database.database import db

class User(db.Model):
  user_id = db.Column(db.Integer, primary_key = True)
  user_name = db.Column(db.String, nullable = False)
  user_email = db.Column(db.String, unique = True, nullable = False)
  user_password = db.Column(db.String, nullable = False)
  
  def is_active(self):
    return True
   
  def get_id(self):
    return str(self.user_id)
	
  def is_authenticated(self):
    return True