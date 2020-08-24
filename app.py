from flask import Flask,render_template,request
from tensorflow.keras.models import load_model,model_from_json
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
tokenizer = Tokenizer(num_words=10000,oov_token='OOV')
max_length = 100
pad_type = 'post'
truc_type = 'post'
app = Flask(__name__)

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        sentence = [message]
        sentence = tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(sentence,maxlen=max_length,padding=pad_type,truncating=truc_type)
        my_predict = np.argmax(loaded_model.predict(padded))
        return render_template('result.html',prediction=my_predict)
if __name__ == '__main__':
    app.run(debug=True)