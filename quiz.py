from random import randint
from flask import Flask, session, redicrect, url_for
from db_scripts import get_question_after
quiz = 0 
last_question = 0
def index():
    global quiz, last_question
    quiz = 1
    last_question = 0
    return '<a href="/test">Тест</a>'
def rest():
    global last_question
    result = get_question_after(last_question, quiz)
    if result is None or len(result) == 0:
        return redirect(url_for('result'))

    else:
        last_question = 0
        return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'
def result(): 
    return "that a all folks!"

app = Flask(__name__)
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
if __name__ == '__main__':       
