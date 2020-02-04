# -*- coding: utf-8 -*-
{
    'name': "emp_module_18dec2019",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
            'base','hr',
            'hr_timesheet',
            'hr_holidays',
            'hr_payroll',
            'hr_attendance',
            'hr_recruitment',
            'hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/work_information_views.xml',
        'views/private_information_views.xml',
        'views/hr_setting_views.xml',
        'views/emergency_contact_views.xml',
        'views/exit_interview_views.xml',
        'views/shift_management_views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True, 
    'application': True,
    'auto_install': False,
}