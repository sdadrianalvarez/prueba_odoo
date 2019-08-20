# -*- coding: utf-8 -*-
from odoo import http

# class ModuloExcel(http.Controller):
#     @http.route('/modulo_excel/modulo_excel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_excel/modulo_excel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_excel.listing', {
#             'root': '/modulo_excel/modulo_excel',
#             'objects': http.request.env['modulo_excel.modulo_excel'].search([]),
#         })

#     @http.route('/modulo_excel/modulo_excel/objects/<model("modulo_excel.modulo_excel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_excel.object', {
#             'object': obj
#         })