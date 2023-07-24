from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

messages = [{'fullname': 'Name Example',
             'email': 'email@example.com',
             'country': 'Example Country',
             'message': 'Message message message',
             'subject': 'Other',
             'gender': 'Male'}]


@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        country = request.form['country']
        message = request.form['message']
        subject = request.form['subject']
        gender = request.form['gender']

        if not fullname:
            flash('Full name is required!')
        elif not email:
            flash('Email is required!')
        elif not country:
            flash('Country is required!')
        elif not message:
            flash('Message is required!')
        elif not gender:
            flash('Gender is required!')
        else:
            messages.append({
                'fullname': fullname,
                'email': email,
                'country': country,
                'message': message,
                'subject': subject,
                'gender': gender
            })
            return redirect(url_for('index'))
    return render_template('create.html')
