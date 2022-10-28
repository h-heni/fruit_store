from multiprocessing.sharedctypes import Value
from unicodedata import name
from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():

    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
        print(request.form)
        heur=datetime.now()
        if request.method=='POST':
            num1=request.form.get('strawberry')
            num2=request.form.get('raspberry')
            num3=request.form.get('apple')
            
            first=request.form.get("first_name")
            second=request.form.get("last_name")
            id=request.form.get("student_id")
            tot=int(num1)+int(num2)+int(num3)
        return render_template("checkout.html",num1=num1,num2=num2,num3=num3,first=first,second=second,id=id,tot=tot,heur=heur)

@app.route('/fruits')         
def fruits():
    
    
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    