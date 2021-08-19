
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
@app.route('/IITBIOTECH.html')
# def IITBIOTECH():
#     return render_template('IITBIOTECH.html')
# @app.route('/IITBIOTECH.html')
# def IITBIOTECH():
#     return render_template('IITBIOTECH.html')
# @app.route('/IITBIOTECH.html')
# def IITBIOTECH():
#     return render_template('IITBIOTECH.html')
# @app.route('/IITBIOTECH.html')
# def IITBIOTECH():
#     return render_template('IITBIOTECH.html')
# @app.route('/IITBIOTECH.html')
# def IITBIOTECH():
#     return render_template('IITBIOTECH.html')
# @app.route('/IITBIOTECH.html')
# def IITBIOTECH():
#     return render_template('IITBIOTECH.html')


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
        <script>
  function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }
  </script>
        </head>
        <body>
         <div id="mySidebar" class="sidebar">
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×</a>
    <a href="branches.html">Branches</a>
    <a href="home.html">Home</a>
    <a href="research.html">Research</a>
    <a href="aboutus.html">About Us</a>
    <a href="news.html">News</a>
  </div>
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
        </body>
        <footer class="footer">
    <link rel="stylesheet" href="/static/css/footer.css">
       <div class="footer-container">
         <div class="row">
           <div class="footer-col">
             <ul>
               <li><h4>Sitemap</h4></li>
               <li><a href="home.html">Home</a></li>
               <li><a href="branches.html">Branches</a></li>
               <li><a href="news.html">News</a></li>
             </ul>
           </div>
           <div class="footer-col">
             <ul>
               <li><h4>Contact Devs</h4></li>
               <li><a href="mailto:piyush.chandra2013@gmail.com">Piyush Chandra</a></li>
               <li><a href="mailto:adityaarchie1234@gmail.com">Aditya Saxena</a></li>
               <li><a href="mailto:nandini0842@gmail.com">Nandini Singh</a></li>
               <li><a href="mailto:devanshchauhan19990@gmail.com">Devansh Chauhan</a></li>
            <li><a href="mailto:ishankkaku@gmail.com">ishank Giri</a></li>
             </ul>
           </div>
           <div class="footer-col">
             <ul>
               <li><h4 style="font-weight: 600;">ManuScript © 2021</h4></li>
               <li>A Platform for Academia.</a></li>
             </ul>
           </div>
           <div class="footer-col">
             <h4>Team Socials</h4>
             <div class="social-links">
               <a href="https://github.com/adityasaxena-crypto/Flakp-web" target="_blank"><i style="fill: white;"><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>GitHub</title><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></i></a>
               <a href="mailto:devatmanuscript@gmail.com"><i style="fill: white;"><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Gmail</title><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg></i></a>
             </div>
           </div>
         </div>
       </div>
    </footer>

    """)
    file.close()
#NEWS ADDED
 
@app.route('/news.html')
def news():
 newsscraper()
 
 return render_template("news.html")
    
