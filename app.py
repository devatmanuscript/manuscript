
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

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


@app.route('/branches.html')
def branches():
    return render_template('branches.html')

@app.route('/conversion.html')
def conversion():
    return render_template('conversion.html')

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

    
@app.route('/')
def menubar():
    return render_template('home.html')
#template
@app.route('/template.html')
def journaltemplate():
    return render_template('template.html')
    
@app.route('/csestatic.html')
def csestatic():
    return render_template('csestatic.html')

@app.route('/nitcse.html')
def nitcse():
    return render_template('nitcse.html')

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
#underdev
@app.route('/underdev.html')
def under():
    return render_template('underdev.html')
#IITchemical
@app.route('/iitchemical.html')
def IITchemical():
    return render_template('iitchemical.html')
#IITbiotechnology
@app.route('/IITBIOTECH.html')
def IITBIOTECH():
    return render_template('IITBIOTECH.html')



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

def newsscraper():

    url = 'https://www.sciencenews.org/'

    source = requests.get('https://www.sciencenews.org/').text
    file = open("./templates/news.html","w", errors='ignore' , encoding="utf8" )
    file.write("""    <head>
        <style>

    .topics-river__wrapper___2CozB
        
        {    
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        display: block;
        margin-left: auto;
        margin-right: auto;
        position: relative;
        width: calc(100vw - 3.7496rem);
        max-width: 86.2504rem;
        margin-bottom: 3rem;
        grid-column-start: 1;
    grid-column-end: 3;
        }

        .topics-river__heading___JcY1k{
            --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        font-family: charter,georgia,serif;
        font-weight: 700;
        color: #31313b;
        font-size: 2.875rem;
        line-height: 1.08696;
        margin-bottom: 1.75rem;
        }

        
        .term-river-grid__container___3M6IO{
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        margin-left: auto;
        margin-right: auto;
        position: relative;
        width: calc(100vw - 3.7496rem);
        max-width: 86.2504rem;
        display: flex;
        flex-wrap: wrap;
        margin-bottom: 3rem;
        }

        .term-river-grid__group___2d4hS
        
        {
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        padding-bottom: 5rem;
        margin-right: 1.25rem;
        width: calc(25vw - 1.8749rem);
        max-width: 20.6251rem;

        }

        .term-river-grid__header___3oiZP
        
        {
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        display: block;
        border-bottom: 1px solid;
        border-color: #31313b;
        margin-bottom: .625rem;
        padding-bottom: .375rem;

        }
        
        
        .term-river-grid__term-name___3ZtsG
        
        {
            --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        font-family: museo-sans,helvetica,arial,sans-serif;
        font-weight: 700;
        letter-spacing: .075em;
        text-transform: uppercase;
        color: #176cab;
        margin-bottom: .375rem;
        font-size: 1rem;
        line-height: 1.1875;
        
        }

        .list
        
        {    
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        list-style: none;


        }


        .term-river-grid__wrapper___fTw9V with-image
        
        {    
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        }

        
        .term-river-grid__figure___11iky
        
        {    
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        display: block;
        height: auto;
        margin: 0;
        max-width: 100%;
        margin-bottom: 1.25rem;
        }

        
        
        .term-river-grid__thumbnail___k0oqa
        
        {    
            --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        color: inherit;
        text-decoration: none;
        display: block;
        overflow: hidden;
        position: relative;    --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        color: inherit;
        text-decoration: none;
        display: block;
        overflow: hidden;
        position: relative;
        }

    .term-river-grid__title___2Gm-_{
        --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        font-family: charter,georgia,serif;
        font-weight: 700;
        color: #31313b;
        font-size: 1.25rem;
        line-height: 1.2;
        margin-bottom: .3125rem;
        }

        
    .term-river-grid__meta___BARqt{
        --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        color: #31313b;
        font-size: .8125rem;
        line-height: 1.15385;
        }

        .term-river-grid__byline___2xYH5 author vcard{
            --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        color: #31313b;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;}

        .byline-link url fn n{
            --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        color: inherit;
        text-decoration: none;}

        .term-river-grid__date___1mM6f entry-date published
        {
            --adminbar-height: 0rem;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        color: #31313b;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
    }





    
        .term-river-grid__wrapper___fTw9V no-image
        
        {    
            --adminbar-height: 0rem;
        color: #31313b;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeSpeed;
        text-size-adjust: 100%;
        word-break: keep-all;
        list-style: none;
        margin: 0;
        padding: 0;
        border: 0;
        box-sizing: border-box;
        font-size: 100%;
        font-style: normal;
        font: inherit;
        vertical-align: baseline;
        display: none;

        } 
        </style>
        </head>
        
            <section class="topics-river__wrapper___2CozB">
            <h2 class="topics-river__heading___JcY1k">
                More Stories	</h2>
        
            <div class="term-river-grid__container___3M6IO">
            
            """)

    soup = BeautifulSoup(source,'lxml')
    for article in soup.find_all('div',class_='term-river-grid__group___2d4hS'):
        file.write(str(article))
        
        
    file.write("""

        </section>

    """)
    file.close()
#NEWS ADDED
 
@app.route('/news.html')
def news():
 newsscraper()
 
 return render_template("news.html")
    
