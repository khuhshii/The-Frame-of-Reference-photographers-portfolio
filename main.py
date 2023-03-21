from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__,template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/FSM'
db = SQLAlchemy(app)

class Feedback(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    occasion = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    message = db.Column(db.String(250), nullable=False)

class Booking_list(db.Model):
    sno = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    occasion = db.Column(db.String(50), nullable=False)
    phone =  db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(12), nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(50), nullable=False)
    date_of_req = db.Column(db.String(12), nullable=True)

class Active(db.Model):
    sno = db.Column(db.Integer, nullable=False, primary_key=True)
    book_code =  db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    occasion = db.Column(db.String(50), nullable=False)
    phone =  db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(12), nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(50), nullable=False)
    date_of_req = db.Column(db.String(12), nullable=True)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(20), nullable=False)

class Services(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        occasion=request.form.get('occasion')
        message=request.form.get('message')
        entry=Feedback(name=name,email=email,occasion=occasion,date=datetime.now(),message=message)
        db.session.add(entry)
        db.session.commit()
        return render_template('msg.html')
    return render_template('contact.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/food")
def food():
    return render_template('food.html')

@app.route("/wedding")
def wedding():
    return render_template('wedding.html')

@app.route("/nature")
def nature():
    return render_template('nature.html')

@app.route("/book", methods=['GET','POST'])
def book():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        occasion=request.form.get('occasion')
        phone=request.form.get('phone')
        date=request.form.get('date')
        no_of_days=request.form.get('no_of_days')
        address=request.form.get('address')
        message=request.form.get('message')
        entry=Booking_list(name=name,email=email,occasion=occasion,phone=phone,date=date,no_of_days=no_of_days,address=address,message=message,date_of_req=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return render_template('bmsg.html')
    return render_template('book.html')

@app.route("/admin", methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=Users.query.filter_by(email=email).first()
        userpass=Users.query.filter_by(password=password).first()
        if user and userpass:
            return render_template('mysec.html')
        else:
            return "Invalid username or password"
    return render_template('admin.html')

@app.route("/gallery-single")
def gallerysingle():
    return render_template('gallery-single.html')

@app.route("/sample-inner-page")
def sampleinnerpage():
    return render_template('sample-inner-page.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/msg")
def msg():
    return render_template('msg.html')

@app.route("/mysec")
def mysec():
    return render_template('mysec.html')

@app.route("/myfeeds")
def myfeeds():
    feedback=Feedback.query.all()
    return render_template('myfeeds.html',feedback=feedback)

@app.route("/mybooks")
def mybooks():
    active=Active.query.all()
    return render_template('mybooks.html',active=active)

@app.route("/logoutadmin") 
def logoutadmin(): 
    return 0

@app.route("/bmsg")
def bmsg():
    return render_template('bmsg.html')

"""@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    feedback=Feedback.query.filter_by(sno=sno).first() 
    db.session.delete(feedback)
    db.session.commit()
    return  "Successfully Deleted"""

@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    active=Active.query.filter_by(sno=sno).first() 
    db.session.delete(active)
    db.session.commit()
    return  "Successfully Deleted"

@app.route("/more")
def more():
    services=Services.query.all()
    return render_template('more.html',services=services)

if __name__=="__main__":
    app.run(debug=True)