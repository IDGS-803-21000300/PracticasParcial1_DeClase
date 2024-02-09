from wtforms import Form
from wtforms import SelectField, RadioField


class FormColors (Form):

    opcionesTira1 = ["negro", "cafe", "rojo", "naranja", "amarillo", "verde", "azul", "violeta", "gris", "blanco"]
    opcionesTira2 = ["negro", "cafe", "rojo", "naranja", "amarillo", "verde", "azul", "violeta", "gris", "blanco"]
    opcionesTira3 = ["negro", "cafe", "rojo", "naranja", "amarillo", "verde", "azul", "violeta", "gris", "blanco"] 
    opcionesTolerancia = ["Oro", "Plata"]

    tira1 = SelectField("tira1", choices= [(index, color) for index, color in enumerate(opcionesTira1)])
    tira2 = SelectField("tira2", choices=[(index, color) for index, color in enumerate(opcionesTira2)])
    tira3 = SelectField("tira3", choices=[(index, color) for index, color in enumerate(opcionesTira3)])
    tolerancia = RadioField("tolerancia", choices=[(index, color) for index, color in enumerate(opcionesTolerancia)], default=opcionesTolerancia[0])
