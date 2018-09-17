# in-class-09-17

See <http://flask.pocoo.org/docs/1.0/quickstart/>

To run: `FLASK_APP=server.py FLASK_ENV=development flask run`

* hello world: `Flask(__name__)` and `@app.route("/")`
* logging: `app.logger.info(...)`
* static content: add image
* from template: `render_template("foo.html")`
* extracting info from request: `request.args["foo"]`
* add conditional rendering to template: `{% if`

