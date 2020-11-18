# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
     _name = 'uposports.cliente'
     _description = 'uposports Cliente'

     name = fields.Char(string="DNI", required=True, size=9, help="Documento identificativo")
     nombre = fields.Char(string="Nombre", required=True, size=30, help="Nombre del cliente")
     apellidos = fields.Char(string="Apellidos",required=True, size=50, help="Apellidos del cliente")
     telefono = fields.Integer(string="Telefono", required=True, size=9, help="Número de teléfono móvil")
     codigoPostal = fields.Integer(string="Codigo Postal",required=True, size=5, help="Codigo Postal")

     abono_id=fields.Many2one('uposports.abono',string="Abono actual del cliente",required=True)
     reserva_id=fields.One2many('uposports.reserva',"cliente_id","Reservas del cliente")
     pago_id=fields.One2many("uposports.pago","cliente_id","Pagos del cliente")
    	

