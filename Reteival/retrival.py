import firebase_admin
import firebase_admin.firestore
from firebase_admin import credentials
from firebase_admin import firestore
import csv
import collections
import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db= firestore.client()
field_names = ['name', 'gender']
dict = {}

def add_values_in_dict(sample_dict, key, list_of_values):

    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

@app.route('/')
def menubar():


    dict = collections.defaultdict(list)
    a_file = open("sample2.csv", "w")
    writer = csv.writer(a_file)
    for i in range(1, 4):
        number = str(i)
        str1 = 'hi' + number
        result = db.collection('hello').document(str1).get()
        data = result.to_dict()
        #print(data)



        for key, value in data.items():
         writer.writerow([key, value])
    a_file.close()

    # Python program to convert
    # CSV to HTML Table


    # Python program to convert
    # CSV to HTML Table


    import pandas as pd

    # to read csv file named "samplee"
    a = pd.read_csv("sample2.csv")

    # to save as html file
    # named as "Table"
    a.to_html("./templates/Table.html")

    # assign it to a
    # variable (string)
    html_file = a.to_html()







        #name = data['Name']
        #sex = data['Sex']
        #dict["Name"].append(name)
        #dict["Sex"].append(sex)
    # dict = add_values_in_dict(dict, 'Name', [name])
    # dict = add_values_in_dict(dict, 'Sex', [sex])

    #print(dict)
    #a_file = open("sample1.csv", "w")

    #writer = csv.writer(a_file)
    #for key, value in dict.items():
    #writer.writerow([key, value])

    #a_file.close()
    return render_template('/Table.html')