from bottle import *

@route("/")
def index():
    name = request.query.n
    data = request.query.d
    print("[{}] {}".format(name, data))
    return "done"

run(host="localhost", port="80", quiet=True)
