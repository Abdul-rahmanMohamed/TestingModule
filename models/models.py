# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class testingmodule(models.Model):
    _name = 'testingmodule.testingmodule'
    _description = 'testingmodule.testingmodule'

    def _new_return_note(self):
        return {"This module is seperated as you ordered me if you go to SO_Line " \
               "you will see new field called size " \
               "if you select any size value and Confirm your order " \
               "Go to delivery you will get the same value of size " \
               "you can edit and no change in size value of its SO line "}

    name = fields.Char("Name", required=True)
    note = fields.Text("Note", default=_new_return_note)

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
