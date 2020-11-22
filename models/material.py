# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'uposports.material'
     _description = 'uposports Material'

     name = fields.Char(string="Nombre", required=True, size=30, help="Nombre del material")
     descripcion = fields.Text(size=300)
     unidades = fields.Integer(required=True)

     instalacion_id = fields.Many2one("uposports.instalacion",string="Instalacion")

     @api.onchange('unidades')
     def onchange_unidades(self):
          resultadoUnidades = {}
          if self.unidades < 0:
               resultadoUnidades = {'value': {'unidades': 0},
               'warning': {'title': 'Unidades de material incorrecta',
                              'message': 'El número de unidades no puede ser negativo'}}
          return resultadoUnidades