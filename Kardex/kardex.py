# -*- coding: utf-8 -*-
################################################
##### Servicios Integrales de Informática. #####
#####                27/04/16              #####
#####                                      #####    
################################################

#Importaciones
import pdb   
import sys
import time
import logging

from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp.tools.translate import _

# CLASE KARDEX 
class kardex(osv.Model):
    _name = "kardex"
    _description = "Kardex Class"
    _columns = {
         'nokardex':fields.integer("No Kardex",required=True),
         'fecha':fields.date("Fecha",required=True),
         'producto':fields.char("Producto",size=127,required=True),
    }