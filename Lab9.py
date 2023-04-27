from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Contact {self.name} {self.phone}>'

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    contact = Contact(name=name, phone=phone)
    db.session.add(contact)
    db.session.commit()
    return 'Contact added!'

@app.route('/clear', methods=['POST'])
def clear():
    db.session.query(Contact).delete()
    db.session.commit()
    return 'Contacts cleared!'

if __name__ == '__main__':
    app.run()
