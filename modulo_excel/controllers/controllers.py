# -*- coding: utf-8 -*-
from odoo import http

class ModuloExcel(http.Controller):
     @http.route('/modulo_excel/lista_archivos/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/modulo_excel/lista_archivos/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('modulo_excel.listing', {
             'root': '/modulo_excel/lista_archivos',
             'objects': http.request.env['modulo_excel.lista_archivos'].search([]),
         })

     @http.route('/modulo_excel/lista_archivos/objects/<model("modulo_excel.lista_archivos"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('lista_archivos.object', {
             'object': obj
         })