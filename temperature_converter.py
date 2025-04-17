from flask import Flask, request, render_template_string

app = Flask(__name__)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

@app.route('/')
def home():
    return render_template_string('''
        <h1>Temperature Converter</h1>
        <form method="post" action="/convert">
            <label for="temp">Enter temperature:</label>
            <input type="number" name="temp" id="temp" required>
            <br>
            <label for="from_unit">From:</label>
            <select name="from_unit" id="from_unit" required>
                <option value="c">Celsius</option>
                <option value="f">Fahrenheit</option>
                <option value="k">Kelvin</option>
            </select>
            <br>
            <label for="to_unit">To:</label>
            <select name="to_unit" id="to_unit" required>
                <option value="c">Celsius</option>
                <option value="f">Fahrenheit</option>
                <option value="k">Kelvin</option>
            </select>
            <br><br>
            <input type="submit" value="Convert">
        </form>
        {% if result %}
            <h2>Result: {{ result }}</h2>
        {% endif %}
    ''')

@app.route('/convert', methods=['POST'])
def convert():
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    temp = request.form['temp']

    try:
        temp = float(temp)
    except ValueError:
        return render_template_string('''
            <h1>Temperature Converter</h1>
            <p>Error: Invalid input. Please enter a valid number.</p>
            <a href="/">Go back</a>
        ''')

    if from_unit == 'c' and to_unit == 'f':
        result = celsius_to_fahrenheit(temp)
    elif from_unit == 'c' and to_unit == 'k':
        result = celsius_to_kelvin(temp)
    elif from_unit == 'f' and to_unit == 'c':
        result = fahrenheit_to_celsius(temp)
    elif from_unit == 'f' and to_unit == 'k':
        result = fahrenheit_to_kelvin(temp)
    elif from_unit == 'k' and to_unit == 'c':
        result = kelvin_to_celsius(temp)
    elif from_unit == 'k' and to_unit == 'f':
        result = kelvin_to_fahrenheit(temp)
    else:
        return render_template_string('''
            <h1>Temperature Converter</h1>
            <p>Error: Invalid conversion parameters.</p>
            <a href="/">Go back</a>
        ''')

    return render_template_string('''
        <h1>Temperature Converter</h1>
        <form method="post" action="/convert">
            <label for="temp">Enter temperature:</label>
            <input type="number" name="temp" id="temp" required>
            <br>
            <label for="from_unit">From:</label>
            <select name="from_unit" id="from_unit" required>
                <option value="c" {% if from_unit == 'c' %}selected{% endif %}>Celsius</option>
                <option value="f" {% if from_unit == 'f' %}selected{% endif %}>Fahrenheit</option>
                <option value="k" {% if from_unit == 'k' %}selected{% endif %}>Kelvin</option>
            </select>
            <br>
            <label for="to_unit">To:</label>
            <select name="to_unit" id="to_unit" required>
                <option value="c" {% if to_unit == 'c' %}selected{% endif %}>Celsius</option>
                <option value="f" {% if to_unit == 'f' %}selected{% endif %}>Fahrenheit</option>
                <option value="k" {% if to_unit == 'k' %}selected{% endif %}>Kelvin</option>
            </select>
            <br><br>
            <input type="submit" value="Convert">
        </form>
        <h2>Result: {{ result }} {{ to_unit|capitalize }}</h2>
    ''', result=round(result, 2), from_unit=from_unit, to_unit=to_unit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
