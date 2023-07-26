from flask import Flask, render_template, redirect, url_for, request
from forms import MessageForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '******'

messages_list = [{
    'subject': 'Order',
    'fullname': 'John Doe',
    'email': 'john@doe.com',
    'gender': 'M',
    'country': 'London',
    'message': 'Hello, I would like to be refunded for the order n°445641',
    'remote_addr': 'Some IP'
}]

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MessageForm()
    if form.validate_on_submit():
        messages_list.append({'subject': form.subject.data,
                            'fullname': form.fullname.data,
                            'email': form.email.data,
                            'gender': form.gender.data,
                            'country': form.country.data,
                            'message': form.message.data,
                            'remote_addr': request.remote_addr
                            })
        return redirect(url_for('messages'))
    return render_template('index.html', form=form)

@app.route('/messages/')
def messages():
    return render_template('messages.html', messages_list=messages_list)