from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='ThisIsSecret'


@app.route('/')
def index():

    if not 'number' in session:
        session['number']=random.randrange(0, 101)
    if not 'result' in session:
        session['result']=-1
        print session['result']
    return render_template("index.html", number=session['number'])
@app.route('/guess', methods=['POST'])
def formGuess():
    if request.form['box']=="":
        session.clear()
        return redirect('/')
    session['result']=int(request.form['box'])
    return redirect('/')


app.run(debug=True)
