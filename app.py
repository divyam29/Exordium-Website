from datetime import datetime
from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
db = SQLAlchemy(app)

local_server = True

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/saic'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/saic'


class Form(db.Model):
    rno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    p_rno = db.Column(db.Integer, nullable=False)
    p_name = db.Column(db.String(50), nullable=False)
    p_email = db.Column(db.String(100), nullable=False)
    talent = db.Column(db.String(255), nullable=False)
    screen_name = db.Column(db.String(100), nullable=False)
    movie_line = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(20), nullable=False)


@app.route("/", methods=['GET', 'POST'])
def form():
    # abort(500)
    if(request.method == 'POST'):
        rno = request.form.get('rno')
        name = request.form.get('name')
        email = request.form.get('email')
        p_rno = request.form.get('p_rno')
        p_name = request.form.get('p_name')
        p_email = request.form.get('p_email')
        talent = request.form.get('Q1')
        screen_name = request.form.get('Q2')
        movie_line = request.form.get('Q3')

        if not rno or not name or not email or not p_rno or not p_name or not p_email or not talent or not screen_name or not movie_line:
            error_message = "All Form Fields Required"
            return render_template('index.html', error_message=error_message)

        elif "be21" not in email and "btech21" not in email:
            email_error = "Form only for BE21/BTECH21"
            return render_template('index.html', email_error=email_error)

        else:
            try:
                entry = Form(rno=rno, name=name, email=email, p_rno=p_rno, p_name=p_name, p_email=p_email,
                             talent=talent, screen_name=screen_name, movie_line=movie_line, date=datetime.now())

                db.session.add(entry)
                db.session.commit()

            except IntegrityError:
                db.session.rollback()
                return render_template('integrityError.html')

            return render_template('success.html')

    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template('404.html')


@app.errorhandler(500)
def not_found(e):
    db.session.rollback()
    print(e)
    return render_template('500.html')


app.run(debug=True)
