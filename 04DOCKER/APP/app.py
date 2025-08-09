from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if operation == 'add':
            r = num1 + num2
            result = f"The sum of {num1} and {num2} is {r}"
        elif operation == 'subtract':
            r = num1 - num2
            result = f"The subtract of {num1} and {num2} is {r}"
        elif operation == 'multiply':
            r = num1 * num2
            result = f"The multiply of {num1} and {num2} is {r}"
        elif operation == 'divide':
            r = num1 / num2
            result = f"The Division of {num1} and {num2} is {r}"

        return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
