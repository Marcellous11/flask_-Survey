from http.client import responses
from urllib import response
from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey, personality_quiz, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "marcellous"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

RESPONSES_KEY = "responses"

user_responses = []
 
@app.route('/')
def landing_page():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    return render_template('base.html',title=survey_title,instructions= survey_instructions)

@app.route('/answer', methods=['POST'])
def answer():
    choice = request.form['answer']
    user_responses.append(choice)

    if(len(user_responses) == len(satisfaction_survey.questions)): 
        return redirect('/complete')
    else:
        return redirect(f"/questions/{len(user_responses)}")

@app.route('/questions/<int:num>')
def questions(num):

    if(len(user_responses) != num):
        flash(f'Invaild question: {num}.')
        return redirect(f'/questions/{len(user_responses)}')
       

    s_question = satisfaction_survey.questions[num]


    if(len(user_responses) == len(satisfaction_survey.questions)):
        return redirect('/complete')
    
     
    return render_template('questions.html',question=s_question,question_num=num)

@app.route('/begin', methods=["POST"])
def being():
    return 



@app.route('/complete')
def thanks():
    return render_template('thanks.html')

@app.route('/questions')
def question_one():
    return redirect('/questions/0')

