from odoo import models,fields, api

class emergency_contact_models(models.Model):
	_inherit = 'hr.employee'

	emergency_phone = fields.Integer(string='Emergency Phone No')
	emergency_contact = fields.Char(string='Emergency Contact Name')

	emergency_relation=fields.Many2one('employee.relation',string='Relation With Employee')

class relation_dropdown(models.Model):
	_name = 'employee.relation'
	
	name = fields.Char(string='Relation Name')

