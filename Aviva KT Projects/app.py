from flask import Flask
from pymongo import MongoClient
from flask import render_template,jsonify
from flask import request,redirect,url_for
from model import collection, insert_data
app = Flask(__name__)

# .venv\Scripts\activate



insert_data()

@app.route("/")
def renderHtml():
    #print(collection)
    return render_template('chatbot.html')

results=[]





@app.route('/submit', methods=['GET', 'POST'])
def findAns():
    answer = None
    question=None
    if request.method == 'POST':
        ques= request.form.get('question')
        question= ques.lower()
        result = collection.find_one({'question': question})
        if result:
            answer = result['answer']
        else:
            answer = False
    dict={
           'question': ques,
           'answer': answer
       }
    results.append(dict)
    return render_template('chatbot.html', results=results)


@app.route('/submit-answer', methods=['POST'])
def addAns():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')
        if question and answer:
            collection.insert_one({'question': question.lower(), 'answer': answer})
    alert='Successfully added in DB!'
    return render_template('chatbot.html', results=results,alert=alert)

if __name__ == "__ main__":
    app.run(debug=True)