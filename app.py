from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        ops = request.form['operation']
        num1 = eval(request.form['num1'])
        num2 = eval(request.form['num2'])
        result = 0
        if ops=='add':
            result = num1+num2
        elif ops =='subtract':
            result = num1-num2
        elif ops =='multiply':
            result = num1*num2
        else:
            result = num1/num2
        return render_template('results.html', result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0")