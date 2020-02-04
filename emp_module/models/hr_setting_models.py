from odoo import models,fields, api

class hr_setting_models(models.Model):
	_inherit = 'hr.employee'

	#below current contract head
	health_insurance=fields.Char(string='Health Insurance')
	medical_exam=fields.Date(string='Medical Exam')
	company_vehicle=fields.Char(fields='Company Vehicle')
	home_work_distance=fields.Integer(fields='Home-Work distance')

	#below Attendence head
	badge_id = fields.Integer(string='Badge ID')	

	#below Leaves head
	remaining_legal_leaves=fields.Integer(string='Remaining Legal Leaves')
	leave_policy = fields.Char(string='Leave Policy')
	holiday_list = fields.Date(string='Holiday List')
	default_shift = fields.Char(string='Default Shift')
	leave_approval = fields.Char(string='Leave Approval')
	
	#below Salary details head
	salary_mode=fields.Char(string='Salary Mode')	

	#below bioData head
	educational_qualification=fields.Char(string='Educational Qualification')
	personal_biodata=fields.Binary(string='Personal Bio Data')
	file_name = fields.Char("File Name")
	external_work_history=fields.Char(string='External Work History')
	internal_work_history=fields.Char(string='Internal Work History')
	upload_documents=fields.Binary(string='Upload Document')

	