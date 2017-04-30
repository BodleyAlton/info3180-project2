import os, time,jsonify,requests, urlparse
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import *
from models import *
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
from thumbs import *
from flask_jwt import JWT
from . import app

jwt = JWT(app, authenticate, identity)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route("/api/users/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit():
            # Get the username and password values from the form.
            email=form.email.data
            password=form.password.data
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.
            user=UserProfile.query.filter_by(email=email, password=password).first()
            print user
            # get user id, load into session
            login_user(user)
            userid= current_user.id
            print userid
            flash("Login Successfull.",'success')
            # remember to flash a message to the user
            return redirect(url_for("viewprof",userid=userid)) # they should be redirected to a secure-page route instead
    return render_template("login.html", form=form)

@app.route('/profile/<userid>',methods=["GET","POST"])
def viewprof(userid):
    form=ScrapeUrl()
    userr={}
    i=0
    # if request.method=='POST':
    #     users= db.session.query(UserProfile).filter_by(id=userid)
    #     for user in users:
    #         p={'userid':str(user.id),'email':user.email, 'image':user.profpic,'gender':user.gender,'age':str(user.age),'profile_created_on':user.date_created}
    #         # userr.insert(i,p)
    #         i+=1
    #     return jsonify(p)
    users= db.session.query(UserProfile).filter_by(id=userid)
    # userr={'users':users,'form':form}
    return render_template('viewprof.html',users=users)
    
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))
    
@app.route('/api/users/register',methods=['POST','GET'])
def createprof():
    pform=ProfileForm()
    file_folder = app.config['UPLOAD_FOLDER']
    if request.method=='POST':
        firstname=pform.firstname.data
        lastname=pform.lastname.data
        email=pform.email.data
        password=pform.password.data
        age=pform.age.data
        gender=pform.gender.data
        profpic=request.files['profpic']
        if profpic and allowed_file(profpic.filename):
            picname= secure_filename(profpic.filename)
            path="/static/uploads/"+ picname
            profpic.save("./app"+path)
            profpic=path
            prof= UserProfile(firstname,lastname,email,password,gender,age,profpic,date())
            db.session.add(prof)
            db.session.commit()
            return redirect (url_for('home'))
    return render_template('createProf.html',form=pform)

@app.route('/api/users/<userid>/wishlist', methods=["POST","GET"])
def get_wishlist(userid):
    if request.method=="GET":
        urls=[]
        #Return wishlist
        # print current_user.id;
        wishlist= db.session.query(WishList).filter_by(uid=userid).all()
        print "RESULT"
        for wish in wishlist:
            print wish.desc
            url=wish.desc
            title=wish.title
            p={"title":title, "url":url}
            urls.append(p)
        message="success"
        wishlist={"message":message, "urls":urls}
        wishes= json.dumps(wishlist)
        return render_template("wishlist.html",wish=wishes)
    if request.method=="POST":
        #Add item to wishlist
        url=request.form['url']
        uid= userid
        desc=request.form['desc']
        title=request.form['title']
        webadd=request.form['webadd']
        item=WishList(uid,url,title,desc,webadd)
        db.add(item)
        db.commit()
        return render_template("wishlist.html",wish=wishlist)

@app.route('/api/users/<userid>/wishlist/<itemid>',methods=["DELETE"])
def delete(userid,itemid):
    if request.method=="DELETE":
        #Remove item from table
        item=db.session.query(WishList).filter_by(id=itemid).all()
        db.session.delete(item)
        return render_template('wishlist.html')
    return render_template('wishlist.html')
    
@app.route('/emails',methods=["POST","GET"])
def emails():
    """Render the website Email page"""
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        #send_email(name,email,subject,message)
    return render_template('emails.html')
        
def send_email(from_name, from_email, subject, msg):
    from_addr= ''
    to_addr = ''

    message= """
    From: {} <{}>
    To: {}<{}>
    subject: {}
    {}
    """
    to_name="rick"
    
    message_to_send = message.format(from_name, from_addr,to_name, to_addr, subject,msg)

    username=''
    password=''

    server= smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(from_addr,to_addr,message_to_send)
    server.quit()
    
@app.route('/url',methods=["GET"])
def get_urls():
    url=request.form['urls']
    imag=get_thumbs(url)
    image={"urls":imag}
    print jsonify(image)
    print "AFTER JSON"
    return jsonify(image)
  
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
    
    
def date():
    return time.strftime("%m %d %Y")
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
