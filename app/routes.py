from flask import render_template, flash, redirect, url_for
from app import app
from flask import request
from app.models import Credentials
from app import db

country=["USA","INDIA","UK","AUSTRALIA","GERMANY"]
Cities={}
Cities['USA']=["New-York", "Texas", "Cleveland", "washington", "Newark", "California"]
Cities['INDIA']=["New Delhi", "Hyderabad", "Mumbai", "Pune", "Benglore", "Chennai"]
Cities['UK']=["London", "Birmingham", "Glasgow", "Liverpool", "Manchester", "Sheffield"]
Cities['AUSTRALIA']=["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra-Queanbeyan", "Newcastle"]
Cities['GERMANY']=["Berlin", "Hamburg", "München", "Frankfurt"]
link={}
link['Greyhound(prefered)']="https://www.greyhound.com/en?wt_mc=acq.us-com.greyhound.sea-brand.google.5236517146.16613938020_134726614756.ad&wt_cc1=branded&wt_cc5=greyhound&utm_source=google&utm_medium=sea-brand&utm_campaign=5236517146.16613938020_134726614756.&utm_term=greyhound&utm_content=us-com.greyhound"
link['Busbud']="https://www.busbud.com/en"
link['megabus']="https://us.megabus.com/"
link['checkmybus']="https://www.checkmybus.com/"
link['gotobus']="https://www.gotobus.com/"
link['Orange(prefered)']="https://www.orangetravels.in/"
link['VRL']="https://www.vrlbus.in/"
link['tsrtc']="https://www.tsrtconline.in/oprs-web/"
link['apsrtc']="https://www.apsrtconline.in/oprs-web/"
link['SRS']="https://www.srstravels.net/"
link['Diwakar(cheapest)']="http://www.diwakarbus.com/"
link['Arriva']="http://www.arrivatravelonline.com/"
link['first group']="https://www.firstgroup-sa.co.za/travel-trade"
link['o-Ahead Group']="https://www.goaheadtours.com/tours?utm_source=google&utm_medium=cpc&utm_campaign=US_Search_General_BRM&utm_group=Company&utm_term=group%20travel%20company&utm_content=587052039580&mt=b&utm_device=c&invsrc=g.1403&gclsrc=ds&gclsrc=ds"
link['National Express UK']="https://www.nationalexpress.com/en"
link['SOxford bus company']="https://www.oxfordbus.co.uk/"
link['Getbybus']="https://getbybus.com/en/"
link['Skybus']="https://www.skybus.com.au/buy-tickets/"
link['mission link']="https://www.kimkim.com/l/australia-tours?utm_medium=cpc&utm_source=adwords&utm_campaign=australia&utm_content=australia_tours&utm_term=australia%20trips"
link['SR transport and coaches']="https://srcoaches.com.au/"
link['Murrays coaches']="https://www.murrays.com.au/"
link['Askania Travel']="https://www.askania-travel.de/willkommen/english/"
link['esta']="https://usaestaonline.com/pages/germany"
link['Enchanting Travels Inc']="https://www.enchantingtravels.com/"


Travels={}
Travels['USA']=["Greyhound(prefered)", "Busbud", "megabus", "checkmybus", "gotobus"]
Travels['INDIA']=["Orange(prefered)", "VRL", "tsrtc", "apsrtc", "SRS", "Diwakar(cheapest)"]
Travels['UK']=["Arriva", "First group", "Go-Ahead Group", "National Express UK", "Stagecoach Group", "Oxford bus company"
]
Travels['AUSTRALIA']=["Getbybus", "Skybus", "mission link", "SR transport and coaches", "Murrays coaches"]
Travels['GERMANY']=["Askania Travel", "esta", ", Enchanting Travels Inc", "Herr" ]
@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])

def login():
    return render_template('index.html')

@app.route('/',methods=['POST'])
@app.route('/index',methods=['POST'])
def post_login():
        if request.form['action']=='signup':
            return render_template('register.html')
        else:
            username1=request.form.get("username","<missing username>")
            password1=request.form.get("password","<missing password>")
            print(username1)
            u1=0
            u=Credentials.query.filter(Credentials.username==username1)
            
            for u in u:
                print(u.username)
            try:
                if u.username==username1 :
                    if u.password==password1:
                        return redirect('/login_1')
                    else:
                        return '<html><h1>Incorrect password</h1></html>'
                else:
                        return '<html><h1>login failed</h1></html>'
            except :
                return '<html<p>user not exists</p></html>'
            
            

                
@app.route("/register",methods=['GET'])
def register():
    return render_template('register.html')

@app.route("/register",methods=['POST'])
def post_register():
    username1=request.form.get("username","<missing username")
    password1=request.form.get("password","<missing password>")
    confirm_password1=request.form.get("confirm_password","<missing confirm_password>")
    print(password1)
    print(confirm_password1)
    if password1 == confirm_password1:
        u=Credentials(username=username1,password=password1)
        db.session.add(u)
        try:
            db.session.commit()
            submitted=1
        except :
            db.session.rollback()
            submitted=0
        return render_template('reg_status.html',submitted=submitted)
    else:
        return '<html><h1>password and confirm password does not match</h1> <br><br><a href="/index"> HOME</a> </html>'
@app.route('/login_1')
def login_1():    
    return render_template('login.html',country=country)

@app.route('/<countr>',methods=['GET'])
def cities(countr):
    return render_template('cities.html',country=countr,list=Cities[countr])

@app.route('/<country>/<list>',methods=['GET'])
def travels(country,list):
    print(list)
    return render_template('travels.html',country=country,list1=Travels[country],link=link)







