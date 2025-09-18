from flask import Flask, render_template,request,redirect,url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        
        if not name or not email:
            flash("All fields are required!", "error")
            return redirect("contact", name=name, email=email)
        
        flash("Message sent successfully!", "success")
        return redirect(url_for("home"))    
    return render_template("contact.html")

