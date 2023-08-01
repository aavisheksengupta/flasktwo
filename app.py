from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/cal', methods=["GET"])
def math_operator():
    operation=request.json("operation")
    numbers1=request.json("number1")
    numbers2=request.json("number2")

    if operation=="add":
        result=numbers1+numbers2
    if operation =="multiply":
        result=numbers1*numbers2
    if operation =="division":
        result=numbers1/numbers2
    else
         result = number1=number2
    return result

app.run(debug=True)