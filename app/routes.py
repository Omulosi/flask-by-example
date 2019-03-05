@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

