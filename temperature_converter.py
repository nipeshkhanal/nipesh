from flask import Flask, request, jsonify

app = Flask(__name__)

# Conversion functions
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

# Home route
@app.route('/')
def home():
    return "Welcome to the Temperature Converter API!"

# Convert route
@app.route('/convert', methods=['GET'])
def convert():
    # Get parameters from the request
    from_unit = request.args.get('from')
    to_unit = request.args.get('to')
    temp = float(request.args.get('temp'))

    # Perform conversion based on user input
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
        return jsonify({"error": "Invalid conversion parameters."}), 400

    # Return the result as JSON
    return jsonify({
        "from": from_unit,
        "to": to_unit,
        "input": temp,
        "result": round(result, 2)
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


   
