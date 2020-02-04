from odoo import fields,models, api

class ShiftTime(models.Model):
	_name='shift.time'
	_description='stores information of shift_name, shift_start_time and shift_end_time'
	_rec_name='shift_name'

	shift_name=fields.Char(string="Shift Name", required=True)
	shift_start_time=fields.Float(string="Start Time")
	shift_end_time=fields.Float(string="End Time")
	
class ShiftDate(models.Model):
	_name='shift.date'
	_description='store information of employee name, shift start date and shift end date'
	_rec_name='emp_names_id'

	emp_names_id=fields.Many2one('hr.employee', string="Employee Name")
	shift_start_date=fields.Date(string="Start Date")
	shift_end_date=fields.Date(string="End Date")
	shift_name_id=fields.Many2one('shift.time', string='Shift Name')

	@api.onchange('shift_name_id')
	def fetch_Shift_time_Details(self):
		for rec in self:
			
			if rec.shift_name_id:
				obj1=self.env['shift.time'].search([('shift_name','=',rec.shift_name_id.shift_name)])	
				emp_object=self.env['hr.employee'].search([('id','=',rec.emp_names_id.id)])	
				emp_object.write({'shift_start_time_inherited':obj1.shift_start_time,
									'shift_end_time_inherited':obj1.shift_end_time,
									'shift_name_inherited':obj1.shift_name })

class ShiftTimeInherited(models.Model):
	_inherit='hr.employee'

	shift_name_inherited= fields.Char(string="Shift Name",readonly=True,store=True)
	shift_start_time_inherited= fields.Float(string="Start Time",readonly=True,store=True)
	shift_end_time_inherited= fields.Float(string="End Time",readonly=True,store=True)

	@api.multi
	def shift_smart_button(self):
		res = self.env['ir.actions.act_window'].for_xml_id('emp_module_18dec2019','action_shift_date')
		res['context'] = {'default_emp_names_id':self.id}
		res['domain'] = [('emp_names_id','=',self.id)]
		return res