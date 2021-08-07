
from flask import Flask, render_template, request

def add_values_in_dict(sample_dict, key, list_of_values):

    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


app = Flask(__name__)
headings = ("Name","Role")

@app.route('/research.html')
def research():
    return render_template('research.html')


@app.route('/professor.html')
def professor():
    return render_template('professor.html')

@app.route('/conversion.html')
def conversion():
    return render_template('conversion.html')

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

    
@app.route('/')
def menubar():
    return render_template('home.html')

    
@app.route('/csestatic.html')
def csestatic():
    return render_template('csestatic.html')

@app.route('/eeestatic.html')
def eeestatic():
    return render_template('eeestatic.html')

@app.route('/civilstatic.html')
def civilstatic():
    return render_template('civilstatic.html')

@app.route('/mechanicalstatic.html')
def mechanicalstatic():
    return render_template('mechanicalstatic.html')
#hehe
@app.route('/home.html')
def home():
    return render_template('home.html')

def homepage():
   dict={}
  
   for i in range(1,4):
    number=str(i)
    str1='hi'+ number
    result = db.collection('hello').document(str1).get()
    data=result.to_dict()

    name=data['Name']
    sex=data['Sex']
    dict = add_values_in_dict(dict, 'Name', [name])
    dict = add_values_in_dict(dict, 'Sex', [sex])

    
   return render_template('home.html', headings=headings, data=dict)


