from flask import Flask, session , redirect, url_for

from db_scripts import get_question_after, get_quises

def start_quis(quiz_id):
    session['quiz'] = quiz_id
    session['last_question']= 0 

def end_quiz():
    session.clear()

def quiz_form():

    html_beg = '''<html><body><h2>Выберите викторину:</h2><form method="post" action="index"><select name="quiz"'''
    html_end='''</select><p><input type="submit" value ="Выбрать"> </p></form></body></html'''

    options = ''' '''
    q_list = get_quises()

    for id, ma,e in q_list:
        option_line = ('''<option value=''' +str(id) + '''>''' + str(name) + '''</option>''')
        options += option_line
    return html_beg + options + html_end   






def index():

    if request.method == 'GET':
        start_quis(-1)
        return quiz_form()
    else:
        quest_id = request.form.get('quiz')
        start_quis(quest_id)
        return redirect(url_for('test'))