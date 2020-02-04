from odoo import models,fields, api

class workInformation(models.Model):
	_name='hr.employee'
	_inherit = 'hr.employee'


	related_customer=fields.Char(string='Related Customer')
	related_vendor=fields.Char(string='Related Vendor')
	employee_code=fields.Integer(string='Employee Code')
	joining_date=fields.Date(string='Joining Date')
	offer_date = fields.Date(string='Offer Date')
	confirmation_date=fields.Date(string='Confirmation Date')
	Contract_end_date = fields.Date(string='Contract End Date')
	notice_in_days = fields.Integer(string='Notice Period (Days)')
	retirement_date = fields.Date(string='Retirement Date')

	


	#under 'position' head
	emp_grade = fields.Selection([
        ('gradea', 'Grade A'),
        ('gradeb', 'Grade B'), 
        ('gradec', 'Grade C')], string='Grade')

	emp_branch = fields.Selection([
        ('brancha', 'Branch 1'),
        ('branchb', 'Branch 2'),
        ('branchc', 'Branch 3')],string='Branch')

	reports_to=fields.Char(string='Reports To')


	