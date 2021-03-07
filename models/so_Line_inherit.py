# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInherit1(models.Model):
    _inherit = 'sale.order.line'
    size = fields.Selection([
        ('large', 'Large'),
        ('small', 'Small'),
        ('medium', 'Medium')], default='large', required=True, store=True)


class InheritStockLine(models.Model):
    _inherit = 'stock.move'
    size = fields.Selection([
        ('large', 'Large'),
        ('small', 'Small'),
        ('medium', 'Medium')], compute="get_size_value", required=True, string="Size", readonly=False, store=True)
    sale_line_id = fields.Many2one('sale.order.line', index=True)

    @api.depends('sale_line_id.size')
    def get_size_value(self):
        for rec in self:
            rec.size = rec.sale_line_id.size
