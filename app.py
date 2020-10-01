from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('Model.pkl')

@app.route('/')
def home():
    return render_template('Form.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        a = request.form['1']
        b = request.form['2']
        c = request.form['3']
        d = request.form['4']
        e = request.form['5']
        f = request.form['6']
        g = request.form['7']
        h = request.form['8']
        i = request.form['9']
        j = request.form['10']
        test = [a,b,c,d,e,f,g,h,i,j,0]
        Value = (model.predict([test]))
        predictedValue = (model.predict_proba([test])[:,1])
    
    return render_template('Form.html', predictedValue = predictedValue, Value = Value)

if __name__ == '__main__':
    app.run(debug = True)
    
