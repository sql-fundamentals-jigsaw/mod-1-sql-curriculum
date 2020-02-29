from flask import Flask
app = Flask()

@app.route('/')
def hello():
    return 'hello world'

app.run(debug = True)

