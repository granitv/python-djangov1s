from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='template/')

@app.route("/")
def index():
    return """
    <html><head></head> <body><h1>Coucou !</h1> </body></html>
    """

@app.route("/test_json")
def test_json():
    d = {'a': 12.0, 'b': True}
    return jsonify(d)

@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()