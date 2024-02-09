from flask import Flask, render_template, request
import math
from clases import FormColors, form

app = Flask (__name__)

@app.route("/operaciones")
def formulario():
    return render_template("formulario1.html")

@app.route("/cinepolis")
def interfaz():
    return render_template("cinepolis.html")

@app.route("/Procesar", methods=["POST"])
def procesar():
    
    if request.method == "POST":

        costoBoleta = 12
        # descuento = 0
        nombre = request.form.get("txtNombre")
        cantidadCompradores = request.form.get("txtCantidadCompradores")
        rbCinecoSi = request.form.get("rbCinecoSi")
        rbCinecoNo = request.form.get("rbCinecoNo")
        cantidadBoletos = request.form.get("txtCantidadBoletos")
        cantidadPagar = request.form.get("txtCantidadPagar")

        maxBoletos = int(cantidadCompradores) * 7 

        if int(cantidadBoletos) <= int(maxBoletos):
            descuento = 0.1 if rbCinecoSi else  0
            total = 0

            if int(cantidadBoletos) > 5 :
                descuento += 0.15
            elif int(cantidadBoletos) >= 3 and int(cantidadBoletos) <= 5:
                descuento += 0.1
            else:
                descuento += 0

            total = (int(cantidadBoletos) * int(costoBoleta)) * (1 - descuento)


            if int(cantidadPagar) == int(total):
                return "<div>COMPRADOR {} , Cuenta Pagada</div>".format(nombre)
            elif int(cantidadPagar) > int(total):
                # return "<div>COMPRADOR {} , Cuenta Pagada, tu cambio es de {}</div>".format(total, (int(cantidadPagar) - int(total)))
                return "<div>COMPRADOR {} , Cuenta Pagada, tu cambio es de {}</div>".format(nombre, (int(cantidadPagar) - int(total)))
            else:
                return "<div>COMPRADOR {} , No te alcanza a pagar papito, te faltan: {}</div>".format(nombre, int(total) -  int(cantidadPagar))


        else:
            return "<div>No puedes comprar más de {} boletos!</div>".format(maxBoletos)


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
        
@app.route("/distancia", methods = ["GET", "POST"])
def distancia():
    dis = form.CalculoDistancia(request.form)

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    distancia = 0

    if request.method == "POST":
            x1 = dis.puntox1.data
            x2 = dis.puntox2.data
            y1 = dis.puntoy1.data
            y2 = dis.puntoy2.data
             
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            print(distancia)


    return render_template("distancia.html", form = dis, distancia= distancia)
        
        
@app.route("/Resistencias", methods=["GET", "POST"])
def resistencias():
    res = FormColors.FormColors(request.form)

    valoresBandaUnoDos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    colores = ["black", "burlywood", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"]
    valoresBandaTres = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 10000000]
    valoresTolerancia = [5, 10]
    coloresT = ["gold", "silver"]

    banda1 = 0
    banda2 = 0
    banda3 = 0
    tolerancia = 0
    valorUnoDos = 0
    valor = 0
    porcentaje = 0
    valorMinimo = 0
    valorMaximo = 0

    if request.method == "POST":
        banda1 = res.tira1.data
        banda2 = res.tira2.data
        banda3 = res.tira3.data
        tolerancia = res.tolerancia.data

        valorUnoDos = (str(valoresBandaUnoDos[int(banda1[0])]) + str(valoresBandaUnoDos[int(banda2[0])]))
        valor = (int(valorUnoDos) * int(valoresBandaTres[int(banda3[0])]))
        porcentaje = (int(valor) * int(valoresTolerancia[int(tolerancia[0])]) / 100)
        valorMinimo = int(valor - porcentaje)
        valorMaximo = int(valor + porcentaje)

    return render_template("resistencias.html", form=res, colores=[colores[int(banda1)], colores[int(banda2)],
                                                            colores[int(banda3)]],
                           tolerancia=coloresT[int(tolerancia)], valor=valor, minimo=valorMinimo, maximo=valorMaximo
                           )

if __name__ == "__main__":
    app.run(debug = True, port=8089)