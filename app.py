from flask import Flask, request, render_template

from sentiment_analyzer.model import Model



model = Model()

app = Flask(__name__)


@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

    

@app.route('/pred',methods=['POST', 'GET'])
def pred():
    sentiment, confidence = model.predict(request.form['Sentence'])

    if sentiment == 'Bad':
        sentiment = 'Bad Review'
        return render_template('bad.html',
                            sentiment= sentiment,
                            confidence = f'Confidence = {confidence} %')
        
    elif sentiment == 'Wonderfull':
        sentiment = 'Wonderfull Review'
        return render_template('good.html',
                            sentiment= sentiment,
                            confidence = f'Confidence = {confidence} %')
        
    else:
        sentiment = 'Normal Review'
        return render_template('neutral.html',
                            sentiment= sentiment,
                            confidence = f'Confidence = {confidence} %')
    
    


    
    
if __name__ == "__main__":
    app.run(port=8000)
   