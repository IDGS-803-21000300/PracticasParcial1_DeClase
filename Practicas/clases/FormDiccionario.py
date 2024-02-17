from wtforms import Form
from wtforms import SelectField, RadioField, IntegerField, StringField
from wtforms import validators

class FormDiccionario(Form):

    palabraEspañol = StringField("PALABRA EN ESPAÑOL", [validators.DataRequired(message='El campo no puede estar vacio'),
                                                         validators.length(min=1, max=100, message="No puedes ingresar una palabra tan grande")])
    palabraIngles = StringField("PALABRA EN INGLÉS", [validators.DataRequired(message='El campo no puede estar vacio'),
                                                         validators.length(min=1, max=100, message="No puedes ingresar una palabra tan grande")])
    
    palabraBusqueda = StringField("PALABRA A BUSCAR", [validators.DataRequired(message='El campo no puede estar vacio'),
                                                         validators.length(min=1, max=100, message="No puedes ingresar una palabra tan grande")])
    
    escogerIdioma = SelectField("Selecciona el idioma", choices=["INGLES","ESPAÑOL"])
    # radiobtnEspañol = SelectField("TRADUCIR A ESPAÑOL", name="E")