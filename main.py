from  flask import Flask, render_template, request

import forms

app = Flask(__name__)


@app.route("/")
def index():
    escuela = "UTL!!"
    alumnos = ["mario", "Pedro", "Luis", "Dario"]
    return render_template("index.html", escuela = escuela, alumnos = alumnos)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alum_form = forms.UserForm(request.form)

    if request.method == 'POST':
        nom = alum_form.nombre.data
        apa = alum_form.aPaterno.data
        ama = alum_form.aMaterno.data
        edad = alum_form.edad.data
        correo = alum_form.correo.data

        print(f'Nombre: {nom}, aPaterno: {apa}, aMaterno: {ama}, Edad: {edad}, Correo: {correo}')

    return render_template("alumnos.html", form=alum_form, nom=nom, apa=apa, ama=ama, edad=edad, correo=correo)

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


#formulario
@app.route("/multiplicar", methods = ["GET","POST"])
def mult():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1> La multiplicación es: {} </h1>".format(str(int(num1)*int(num2)))
    else:

        return '''
            <form action = "/multiplicar" method = "POST">
                <label> N1: </label>
                <input type="text" name="n1"/><br>
                <label> N2: </label>
                <input type="text" name="n2"/><br>
                <input type="submit"/>
            </form>

            '''
#decorador para formulario1
@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")


@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")

@app.route("/resultado", methods = ["GET","POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1> La multiplicación es: {} </h1>".format(str(int(num1)*int(num2)))
    

if __name__== "__main__":
    app.run(debug=True)