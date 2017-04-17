from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import UserProfile


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit():
            # Get the username and password values from the form.
            username=form.username.data
            password=form.password.data
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.
            user=UserProfile.query.filter_by(username=username, password=password).first()
            print user
            # get user id, load into session
            login_user(user)
            flash("Login Successfull.",'success')
            # remember to flash a message to the user
            return redirect(url_for("secure_page")) # they should be redirected to a secure-page route instead
    return render_template("login.html", form=form)
    
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
    
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
