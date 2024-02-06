from flask import Flask, render_template, request
import form
import math

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    dis = form.CalculoDistancia(request.form)

    if request.method == "POST":
            x1 = dis.puntox1.data
            x2 = dis.puntox2.data
            y1 = dis.puntoy1.data
            y2 = dis.puntoy2.data
             
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            print(distancia)


    return render_template("index.html", form = dis, distancia= distancia)

# @app.route("/distancia", methods = ["GET", "POST"])
# def distancia():
#     dis = form.CalculoDistancia(request.form)

#     if request.method == "POST":
#             x1 = dis.x1.data
#             x2 = dis.x2.data
#             y1 = dis.y1.data
#             y2 = dis.y2.data
#             print("Nombre : {}".format(y1))
#             print("Paterno : {}".format(x2))
#             print("Materno : {}".format(y2))

#     return render_template("inicio.html", form = dis)

if __name__ == "__main__":
    app.run(debug = False, port=8083)