# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloNuevo2(http.Controller):
#     @http.route('/modulo_nuevo2/modulo_nuevo2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_nuevo2/modulo_nuevo2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_nuevo2.listing', {
#             'root': '/modulo_nuevo2/modulo_nuevo2',
#             'objects': http.request.env['modulo_nuevo2.modulo_nuevo2'].search([]),
#         })

#     @http.route('/modulo_nuevo2/modulo_nuevo2/objects/<model("modulo_nuevo2.modulo_nuevo2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_nuevo2.object', {
#             'object': obj
#         })
