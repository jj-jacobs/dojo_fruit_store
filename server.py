from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print(request.form["strawberry"])
    print(int(request.form["strawberry"]))
    return render_template("checkout.html", num_straw=request.form["strawberry"], num_rasp=request.form["raspberry"], num_apple=request.form["apple"],  first_name=request.form["first_name"], last_name=request.form["last_name"], stud_id=request.form["student_id"],total_fruit=int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"]))

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
