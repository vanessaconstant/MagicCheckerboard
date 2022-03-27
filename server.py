from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def createBoard_1():
    return render_template('index.html', color_one="black", color_two='red', col=8, row=8)


@app.route('/<int:row>')
def createBoard_2(row):
    return render_template('index.html', color_one="black", color_two='red', col=8, row=row)


@app.route('/<int:col>/<int:row>')
def createBoard_3(col, row):
    return render_template('index.html', color_one="black", color_two='red', col=col, row=row)


@app.route('/<int:col>/<int:row>/<string:color_one>')
def createBoard_4(col, row, color_one):
    return render_template('index.html', color_one=color_one, color_two='red', col=col, row=row)


@app.route('/<int:col>/<int:row>/<string:color_one>/<string:color_two>')
def createBoard_5(col, row, color_one, color_two):
    return render_template('index.html', color_one=color_one, color_two=color_two, col=col, row=row)


if __name__ == "__main__":
    app.run(debug=True)
