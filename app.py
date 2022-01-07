from flask import Flask, request, render_template, Markup

from sentiment_analyzer.model import Model



model = Model()

app = Flask(__name__)


@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('model.html')

@app.route('/predict',methods=['POST', 'GET'])
def pred():
    sentiment, confidence = model.predict(request.form['Sentence'])

    if sentiment == 'Bad':
        sentiment = 'Bad Review 😒😒'
    elif sentiment == 'Wonderfull':
        sentiment = 'Wonderfull Review 😊😊'
    else:
        sentiment = 'Normal Review 😐😐'


    return render_template('model.html',
                            sentiment= sentiment,
                            confidence = f'Confidence = {confidence} %')
    
if __name__ == "__main__":
    app.run()
   