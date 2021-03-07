# -*- coding: utf-8 -*-
# from odoo import http


# class Testingmodule(http.Controller):
#     @http.route('/testingmodule/testingmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testingmodule/testingmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testingmodule.listing', {
#             'root': '/testingmodule/testingmodule',
#             'objects': http.request.env['testingmodule.testingmodule'].search([]),
#         })

#     @http.route('/testingmodule/testingmodule/objects/<model("testingmodule.testingmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testingmodule.object', {
#             'object': obj
#         })
