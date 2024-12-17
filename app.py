from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return "welcome home" 
    
@app.route('/about')
def about():
    return "Welcome to about us page!"

@app.route("/services")
def services():
    return "Welcome to our services page!"  
  
  

 

@app.route("/maths")
def maths ():
    a = 5
    b = 10
    c = a+b
    return render_template("maths.html", maths_result=c)

@app.route("/multiply")
def multiply ():
    a = 14
    b = 15
    c = 20
    d= a*b*c
    return render_template("mutiply.html", multiply_result=d)

@app.route("/division")
def division ():
    a = 100
    b = 15
    c= a/b
    return "Hurray!, you are correct, this is the result" + str(c) 
 
@app.route('/homepage')
def homepage():
    name="Mrs Akinfolaju"
    email="peju@yahoo.com"
    return render_template('homepage.html', name=name,email=email)


    

 
 
 
 
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004, debug=True)   