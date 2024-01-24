from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado", methods = ["GET", "POST"])
def suma():
    if request.method == "POST":

        num1 =  request.form.get("n1")
        num2 =  request.form.get("n2")
        suma = request.form.get("suma")
        resta = request.form.get("resta")
        multi = request.form.get("multi")
        dividir = request.form.get("dividir")

        if(dividir):
            return "<h1>El resultado es: {}</h1>".format(str(int(num1) / int(num2)))
        elif(suma):
            return "<h1>El resultado es: {}</h1>".format(str(int(num1) + int(num2)))
        elif(resta):
            return "<h1>El resultado es: {}</h1>".format(str(int(num1) - int(num2)))
        elif(multi):
            return "<h1>El resultado es: {}</h1>".format(str(int(num1) * int(num2)))

if __name__ == "__main__":
    app.run(debug = True, port=8080)