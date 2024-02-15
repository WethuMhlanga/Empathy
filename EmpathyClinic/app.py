# Import necessary libraries
from flask import Flask, render_template, request
import mysql.connector
import os
import pandas as pd

app = Flask(__name__)

# Configure your MySQL database
db_config = {
   'host': 'localhost',
   'user': 'root',
   'password': 'Ndumiso@19',
   'database': 'clinic_db',  # Change to your database name
}

# Define a function to establish a database connection
def connect_to_database():
   return mysql.connector.connect(**db_config)

# Define the route for rendering the form and the admin dashboard
@app.route('/')
def index():
    return render_template('index.html')  # HTML file name

@app.route('/admin')
def admin_dashboard():
    try:
        # Connect to MySQL
        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)

        # Retrieve appointments data from MySQL
        select_query = "SELECT * FROM appointment"
        cursor.execute(select_query)
        appointments = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

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
           # Connect to MySQL
           conn = connect_to_database()
           cursor = conn.cursor()

           # Insert data into MySQL
           insert_query = "INSERT INTO appointment (name, people, date, message) VALUES (%s, %s, %s, %s)"
           data = (name, people, date, message)
           cursor.execute(insert_query, data)

           # Commit the changes and close the connection
           conn.commit()
           cursor.close()
           conn.close()

           # Save data to a CSV file
           csv_filename = 'form_data.csv'
           df = pd.DataFrame([data], columns=['Name', 'People', 'Date', 'Message'])
           df.to_csv(csv_filename, mode='a', header=not os.path.exists(csv_filename), index=False)

           return f"Form submitted successfully! Data: {name}, {people}, {date}, {message}"
       except Exception as e:
           # Handle exceptions (e.g., database errors)
           return f"Error: {e}"
   else:
       # If it's a GET request, you might want to redirect or render a different page
       return render_template('some_other_page.html')

if __name__ == '__main__':
   app.run(debug=True)
