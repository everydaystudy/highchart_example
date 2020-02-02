from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)


@app.route('/<cname>')
def index(cname):

    host = "http://localhost:5000"
    path = "/iris/iris.csv/%s" % cname

    url = host + path
    response = requests.get(url)
    
    data = response.json()
    data = [float(x) for x in data]

    return render_template("index.htm", c = cname, d=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)