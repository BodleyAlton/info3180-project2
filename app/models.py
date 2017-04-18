from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(225))
    gender=db.Column(db.String(6))
    age=db.Column(db.Integer)
    profpic=db.Column(db.String(50))
    date_created=db.Column(db.Date)
    
    def __init__(self,firstname,lastname,email,password,gender,age,profpic,date_created):
        # self.id=id
        self.first_name=firstname
        self.last_name=lastname
        self.email=email
        self.password=password
        self.gender=gender
        self.age=age
        self.profpic=profpic
        self.date_created=date_created

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.email)

class WishList(db.Model):
    id =db.Column(db.Integer,autoincrement=True,primary_key=True)
    uid = db.Column(db.Integer,primary_key=True)
    url= db.Column(db.String(200))
    title= db.Column(db.String(20))
    desc= db.Column(db.String(200))
    webadd= db.Column(db.String(200))
    
    def __init__(self,uid,url,title,desc,webadd):
        self.uid=uid
        self.url=url
        self.title=title
        self.desc=desc
        self.webadd=webadd
        