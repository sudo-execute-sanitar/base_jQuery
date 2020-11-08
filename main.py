import flask

app = flask.Flask(__name__)


@app.route('/')
def show():
    return flask.render_template("page.html")
