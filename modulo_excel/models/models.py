# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lista_archivos(models.Model):
     _name = 'modulo_excel.lista_archivos'

     name = fields.Char()
     archivo = fields.Char()
     columnas = fields.Integer()
     registros = fields.Integer()
     total = fields.Integer(compute="_compute_total", store=True)
     fecha_subida = fields.Datetime()

     @api.depends('columnas', 'registros')
     def _compute_total(self):
         self.total = self.columnas * self.registros