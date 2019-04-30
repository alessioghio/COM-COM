from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


list = {
    "Wong": {
        "queso": 8.990,
        "jamon": 18.0,
        "leche": 4.50,
        "huevos": 6.650,
        "arroz": 17.50
    },
    "PlazaVea": {
        "queso": 8.10,
        "jamon": 14.0,
        "leche": 4.30,
        "huevos": 6.60,
        "arroz": 16.990
    },
    "Tottus": {
        "queso": 8.10,
        "jamon": 10.460,
        "leche": 4.30,
        "huevos": 8.450,
        "arroz": 17.890
    }
}

total = []
temp = 0

# Sum prices per supermarket
# Store it in array "total"
for counter in list.values():
    for x in counter.values():
        temp = temp+x
    total.append(round(temp, 2))
    temp = 0


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/result')
def result():
    return render_template('/result.html', total=total)


if __name__ == '__main__':
    app.run(debug=True)
