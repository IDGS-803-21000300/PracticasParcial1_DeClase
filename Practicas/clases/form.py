from wtforms import Form
from wtforms import StringField, EmailField, IntegerField 

class CalculoDistancia (Form):

    puntox1 = IntegerField("puntox1")
    puntoy1 = IntegerField("puntoy1")

    puntox2 = IntegerField("puntox2")
    puntoy2 = IntegerField("puntoy2")