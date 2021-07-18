from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sign_up():
    return render_template("shopping_list.html")

@app.route('/show_items', methods=['POST', 'GET'])
def items():
    results = request.form
    return render_template('show_items.html', result=results)

if __name__ == '__main__':
    app.run(debug=True)
