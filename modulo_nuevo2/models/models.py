# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulo_nuevo2(models.Model):
     _name = 'modulo_nuevo2.task'
     _description = 'modulo_nuevo2.modulo_nuevo2'

     name = fields.Char()
     descripcion = fields.Char()
     fecha = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
