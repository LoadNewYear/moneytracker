from flask import Flask, render_template, request

app = Flask(__name__)

# Global variables
money = 0
with open("amount.txt", "r") as f:
    money = int(f.read())

# Main route
@app.route('/')
def index():
    return render_template('index.html', money=money)

# Add money
@app.route('/add', methods=['POST'])
def add():
    global money
    try:
        money += int(request.form.get('amountInput'))
    except ValueError:
        return render_template('money.html', money=money)
    with open("amount.txt", "w") as f:
        f.write(str(money))
    return render_template('money.html', money=money)
