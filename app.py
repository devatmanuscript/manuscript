import firebase_admin
import firebase_admin.firestore
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, render_template, request

def add_values_in_dict(sample_dict, key, list_of_values):

    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


app = Flask(__name__)
headings = ("Name","Role")
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db= firestore.client()

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
    return render_template('menubar.html')


@app.route('/home.html')

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


