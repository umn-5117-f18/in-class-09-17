from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    foo = request.args["foo"]
    app.logger.info(foo)

    # return 'Hello, World!'
    return render_template("foo.html", arg=foo)
