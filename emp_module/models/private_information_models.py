from odoo import models,fields, api

class privateInformation(models.Model):
	_inherit = 'hr.employee'

	#below 'citizenship' head 
	issue_date = fields.Date(string='Passport Issue Date')
	validUpto_date=fields.Date(string='Passport Valid Upto')
	place_of_issue = fields.Char(string='Place of Issue')
	
	uan_number=fields.Char(string='UAN Number')
	pan_number=fields.Char(string='PAN Number')
	pf_number=fields.Char(string='PF Number')

	
	#below contact information
	Personal_mobile_number= fields.Char(String='Personal Mobile Number')
	Personal_email=fields.Char(string='Personal Email')	 
	Prefered_mode_of_communication = fields.Selection([('Personal_mobile_number', 'Mobile'), ('Personal_email', 'Email')], default='Personal_email')
	parmanent_address=fields.Text(string='Permanent Address')
	current_address=fields.Text(string='Current Address')
	 
	#blow status head
	number_of_children=fields.Integer(string='No. of Children')

	#below birth head
	age=fields.Integer(string='Age')
	palce_of_birth=fields.Char(string='Place of Birth')

	#below other information head
	blood_group = fields.Char(string='Blood Group')
	family_background = fields.Char(string='Family Background')
	health_issues = fields.Char(string='Health Issues')


	gender = fields.Selection(selection_add=[('transgender', 'Transgender')])
	
	