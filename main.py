from  flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    escuela = "UTL!!"
    alumnos = ["mario", "Pedro", "Luis", "Dario"]
    return render_template("index.html", escuela = escuela, alumnos = alumnos)

@app.route("/alumnos")
def alum():
    return render_template("alumnos.html")

@app.route("/maestros")
def maes():
    return render_template("maestros.html")


@app.route("/hola")
def hola():
    return "<p> <h1> hola desde hola  <br> Mundo </h1> </p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola " + name

@app.route("/numero/<int:n>")
def numero(n):
    return "<h1>El número es: {} ".format(n) 

@app.route("/numero/<int:id>/<string:name>")
def func(id, name):
    return "ID: {} Nombre: {}".format(id, name) 

@app.route("/suma/<float:n1>/<float:n2>")
def func1(n1, n2):
    return "El valor de {} + {} = {}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def func2(ab = "UTL"):
    return "el valor es" + ab

if __name__== "__main__":
    app.run(debug=True)