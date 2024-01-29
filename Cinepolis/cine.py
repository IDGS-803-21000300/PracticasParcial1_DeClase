from flask import Flask, render_template, request

app =  Flask (__name__)

@app.route("/")
def interfaz():
    return render_template("index.html")

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
        




if __name__ == "__main__":
    app.run(debug = False, port=8081)