from django import template
from datetime import datetime
register = template.Library()

@register.filter(name='saludar')
def saludar(nombre):
    return f"<p style='background-color:#18396A; color: gray;'>Bienvenido {nombre}</p>"