from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    print("test")


@app.route('/_get_data/', methods=['POST'])
def _get_data():
    myList = ['Element1', 'Element2', 'Element3']

    return jsonify({'data': render_template('response.html', myList=myList)})
    print("test1")

if __name__ == "__main__":
    app.run(debug=True)