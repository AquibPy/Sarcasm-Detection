from flask import Flask,render_template,request

import numpy as np
import pickle
app = Flask(__name__)
cv = pickle.load(open('cv.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        sentence = [message]
        vect = cv.transform(sentence).toarray()
        my_predict = (model.predict(vect))
        # if my_predict == 1:    
        #     prediction = True
        # else:
        #     prediction = False
        return render_template('result.html',prediction=my_predict)
if __name__ == '__main__':
    app.run(debug=True)