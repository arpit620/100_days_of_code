# Importing necessary modules from the Flask library
from flask import Flask, request, render_template

# Creating an instance of the Flask class
app = Flask(__name__)

# Creating the home route
@app.route('/')
def home():
    # Rendering the home page template
    return render_template('index.html')

# Creating the temperature route
@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    # Initializing variables
    result = None
    temp = None
    unit = 'C'

    # Checking if the request method is POST
    if request.method == 'POST':
        # Getting the temperature and unit from the form
        temp = request.form['temp']
        unit = request.form['unit']

        # Converting the temperature based on the unit
        if unit == 'C':
            result = (float(temp) * 9/5) + 32
        else:
            result = (float(temp) - 32) * 5/9

    # Rendering the temperature page template with the result, temperature, and unit
    return render_template('temperature.html', result=result, temp=temp, unit=unit)

# Creating the length route
@app.route('/length', methods=['GET', 'POST'])
def length():
    # Initializing variables
    result = None
    length = None
    unit = 'cm'

    # Checking if the request method is POST
    if request.method == 'POST':
        # Getting the length and unit from the form
        length = request.form['length']
        unit = request.form['unit']

        # Converting the length based on the unit
        if unit == 'cm':
            result = float(length) / 2.54
        else:
            result = float(length) * 2.54

    # Rendering the length page template with the result, length, and unit
    return render_template('length.html', result=result, length=length, unit=unit)

# Creating the results route
@app.route('/results')
def results():
    # Rendering the results page template
    return render_template('results.html')

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/results')
def results():

