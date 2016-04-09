# -*- coding: utf-8 -*-
from osv import osv, fields
from types import *
 
""" CLASE PERSONA """
 
class persona(osv.osv):
 
    _name = "personas.persona"
    _description = "Tabla con las personas"
    _columns = {
        'nif':fields.char('NIF',size=20, required=True),
        'apellidos':fields.char('Apellidos', size=200, required=True),
        'nombre':fields.char('Nombre',size=100, required=True),
        'genero':fields.selection([('hombre','Hombre'),('mujer','Mujer')],'Género', required=True),
        'telefono':fields.char('Teléfono', size=20),
        'anotaciones':fields.text('Anotaciones'),
    }
 
    # Orden para que nos muestre primero las últimas personas
    _order = 'id desc'
 
    # Restricción única al campo NIF
    _sql_constraints = [
        ('nif_unique', 'unique(nif)', 'El NIF debe ser único'),
    ]
 
persona()