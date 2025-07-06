from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    suggestion = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        
    
        if "maths" in user_input.lower():
            suggestion = "You should explore Calculus if you are begineer."

        elif "coding" in user_input.lower():
            suggestion = "Start with Python."
        elif "computer science" in user_input.lower():
            suggestion = "Start exploring Udemy or Coursera."
        else:
            suggestion = "Try Coursera or Udemy to begin your journey."

    return render_template("index.html", suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
