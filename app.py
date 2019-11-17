from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)

class InputForm(FlaskForm):
    wage = StringField('Wage', validator = [DataRequired()])
    city1 = StringField('City 1', validator = [DataRequired()])
    city2 = StringField('City 2', validator = [DataRequired()])
    submit = SubmitField('Find')


@app.route('/')
@app.route('/index')
def index():
    data = {'wage': '10000', 'city1': 'New York', 'city2': 'Boston'}     
    return render_template('index.html', data = data)

@app.route('/input', methods = ['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        #flash('Wage requested: {}, City 1: {}, City 2: {}'.format(
            #form.wage.data, form.city1.data, form.city2.data))
        return redirect(url_for('result'))
    return render_template(input.html, form = form)

@app.route('/result')
def result():
    pass

if __name__ == '__main__':
    app.run(debug=True)