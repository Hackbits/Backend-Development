from flask import Flask, render_template,request

app = Flask(__name__)

@app.before_request
def log_request():
    print(f"Incoming request: {request.method} {request.url}")
    
@app.after_request
def log_response(response):
    print(f"Outgoing response: {response.status_code}")
    return response

@app.route("/")
def hello():
    return render_template("home.html", person = "SRI")

@app.route("/user/<name>",methods=["POST","GET"])
def get_user(name=None):
    if(request.method == "GET"):
        return render_template("user.html", person = name)
    else:
        data = request.get_json()
        arguments = request.args.to_dict();
       
        return {"name":name,"age":data['age'],"search":arguments["search"],"name":arguments["name"]},404

@app.route("/about")
def about():
    return "This is about page. we haven't templated yet."

