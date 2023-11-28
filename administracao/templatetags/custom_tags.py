from django import template
import struct

register = template.Library()

# PEGA O VALOR DA LINHA PELO INDICE VINDO DA COLUNA COMO SE TIVESSE UM COMPORTAMENTO DE LISTA.
@register.filter
def get_value(dictionary, key):
    return dictionary.get(key, '')

# PEGA VALOR DO BIT QUE VEM EM UMA STRING E CONVERTE PARA BOOLEAN
@register.filter
def bytes_to_bool(value):
    return struct.unpack('<?', value)[0]

@register.filter
def starts_with(value, prefix):
    return value.startswith(prefix)

@register.filter
def multiply(value, factor):
    return value * factor