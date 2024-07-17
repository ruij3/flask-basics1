from flask import Flask, render_template  # imports flask module from Flask class
import random

app = Flask(__name__)  # instance of flask         flask <- module, Flask <- class

@app.route("/")    # / <- endpoint/route
def home():
    return "<h1>Hello World!</h1>"

@app.route("/computing")
@app.route("/h2comp")
@app.route("/best_subject")  # all three routes will lead to what is computing?
def computing():
    return "<h1>What is computing?</h1>"

my_college = "ASRJC"
rival_college = "ACJC"
secret_text = "yesssssss"
secret_nums = [1111, 1234, 2, 3, 444]
secret_info = {"name": "ruijia", "description": "wow", "gender": "female", "type": "me"}

@app.route("/about")
def about():
    return render_template("about.html", my_college=my_college, rival_college=rival_college)


@app.route("/secret")
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template("secret.html", secret_text=secret_text, lucky_num=lucky_num, secret_info=secret_info)

if __name__ == "__main__":
    app.run(debug=True, port=1234)


