from flask import Flask
app=Flask(__name__)
@app.route('/')
def helloo():
    return("Hello World,WELCOME to India")
if __name__ == "__main__":
    app.run(debug=True)
