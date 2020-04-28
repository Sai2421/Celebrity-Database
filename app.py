from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class actor(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    image=db.Column(db.String(200),nullable=False)
    name=db.Column(db.String(200),nullable=False)
    zoidiac=db.Column(db.String(200),nullable=False)
    height=db.Column(db.String(200),nullable=False)
    age=db.Column(db.Integer(),nullable=False)
    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        image=request.form['image']
        name=request.form['name']
        zodiac=request.form['zodiac']
        height=request.form['height']
        age=request.form['age']
        new_task=actor(image=image,name=name,zoidiac=zodiac,height=height,age=age)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Exception"
    else:
        data=actor.query.all()
        return render_template("index.html",data=data)

if __name__=='main':
    app.run()