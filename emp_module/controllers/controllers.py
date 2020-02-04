# -*- coding: utf-8 -*-
from odoo import http

# class EmpModule18dec2019(http.Controller):
#     @http.route('/emp_module_18dec2019/emp_module_18dec2019/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emp_module_18dec2019/emp_module_18dec2019/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emp_module_18dec2019.listing', {
#             'root': '/emp_module_18dec2019/emp_module_18dec2019',
#             'objects': http.request.env['emp_module_18dec2019.emp_module_18dec2019'].search([]),
#         })

#     @http.route('/emp_module_18dec2019/emp_module_18dec2019/objects/<model("emp_module_18dec2019.emp_module_18dec2019"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emp_module_18dec2019.object', {
#             'object': obj
#         })