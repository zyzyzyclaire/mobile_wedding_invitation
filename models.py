from routes import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(345), unique=True, nullable=False)
  brand_name = db.Column(db.String(50), nullable=False)
  password = db.Column(db.String(255), nullable=False)
  
  menus = db.relationship('Menu')
  menu_list = db.relationship('Menu_list')
  r_menu_list = db.relationship('R_menu_list')
  
  menu_categorys = db.relationship('Menu_categorys')
