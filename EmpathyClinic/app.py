# Import necessary libraries
from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your Heroku PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://lypaavvxlpqorj:d38910e864e282745e8df5b63bb06c0c294adefac71101523140f9e80679ac35@ec2-52-5-167-89.compute-1.amazonaws.com:5432/ddln2snf1v0c97')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    people = db.Column(db.Integer)
    date = db.Column(db.String(255))
    message = db.Column(db.String(255))

# Define the route for rendering the form and the admin dashboard
@app.route('/')
def index():
    return render_template('index.html')  # Change to your HTML file name

@app.route('/admin')
def admin_dashboard():
    try:
        # Retrieve appointments data from Heroku PostgreSQL
        appointments = Appointment.query.all()

        return render_template('admin.html', appointments=appointments)
    except Exception as e:
        # Handle exceptions (e.g., database errors)
        return f"Error: {e}"

# Define the route for handling form submissions
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['Name']
        people = request.form['People']
        date = request.form['date']
        message = request.form['Message']

        try:
            # Insert data into Heroku PostgreSQL
            new_appointment = Appointment(name=name, people=people, date=date, message=message)
            db.session.add(new_appointment)
            db.session.commit()

            return f"Form submitted successfully! Data: {name}, {people}, {date}, {message}"
        except Exception as e:
            # Handle exceptions (e.g., database errors)
            return f"Error: {e}"
    else:
        # If it's a GET request, you might want to redirect or render a different page
        return render_template('some_other_page.html')

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)))
