from flask import *

app = Flask(__name__)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("table.html")

if __name__ == '__main__':
    app.run(debug=True)
