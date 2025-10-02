from flask import Flask, render_template,request,url_for,redirect, session, flash

app = Flask(__name__)
app.secret_key = "sectret123"

USERS_FILE = "users.txt"


# Function to save user in file
def save_user(username, email, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{email},{password}\n")


# Function to check login credentials
def validate_user(username, password):
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    return True
    except FileNotFoundError:
        return False
    return False

@app.route("/")
def home():
    return redirect(url_for('login'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get["username"]
        email = request.form.get["email"]
        password = request.form.get["password"]

        save_user(username, email, password)
        flash("Signup successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("signup2.html")
    
    
    
      

@app.route("/login", methods = ["POST","GET"] )
def login():
        if request.method == "POST":
         username = request.form.get("username")
         password = request.form.get("password")

         user = validate_user(username, password)
         if user:
            session["user"] = user
            return redirect(url_for("dashboard"))
         else:
            flash("Invalid username or Password!", "danger")
        # valid_users = {
        # 'admin':123,
        # 'sks':'bjp',
        # 'mk':'raj'
        # }
        # if usernamee in valid_users and password == valid_users[usernamee]:
        #  return render_template("dashboard2.html")
        # else:
        #   return "Invalid Login!"
        
        return render_template("login2.html")
       
    

     
@app.route("/dashboardd", methods=["GET","POST"])
def dashboardd():
    # if "user" not in session:
        # return redirect(url_for("login"))
        return render_template("dashboard2.html")#, user=session["user"])



@app.route("/forget")
def forget():
     return render_template("forget2.html")

@app.route("/dashboardd")
def dashboard():
     return render_template("dashboard2.html")

@app.route("/feedback", methods = ['GET', 'POST'])
def feedback():
      if request.method == 'POST':
        name = request.form.get("username")
        email = request.form.get("email")
        massage = request.form.get("massage")

        return render_template("thankyou2.html", name=name, massage=massage, email=email)
    
      return render_template("feedback2.html")
     

@app.route("/analytics")
def analytics():
     return render_template("analytics2.html")
@app.route("/task")
def tasks():
     return render_template("task2.html")
@app.route("/notification")
def notification():
     return render_template("notification2.html")
@app.route("/settings")
def settings():
     return render_template("settings2.html")

     
if __name__ == "__main__":
  app.run(debug = True)