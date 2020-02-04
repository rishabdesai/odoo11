from odoo import models,fields,api

class exit_interview(models.Model):
	_inherit = 'hr.employee'

	resignation_letter_date=fields.Date(string='Resignation Letter Date')
	relieving_date=fields.Date(string='Relieving Date')
	reason_for_leaving=fields.Text(string='Reason For Leaving')
	leave_encashed=fields.Char(string='Leave Encashed?')
	encashment_date=fields.Date(string='Encashment Date')
	interview_held_on=fields.Date(string='Interview Held On')
	new_workspace=fields.Char(string='New Workspace')
	exit_feedback=fields.Text(string='Feedback')