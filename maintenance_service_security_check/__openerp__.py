{
    'name': "Security Check",
    'version': '9.0.1.0',
    'depends': [
        'maintenance_service',
        'mail',
        'sale_contract',
        'contract_timesheet_activities_on_site_management',
        'hr_analytic_timesheet_improvements',
        'account_analytic_account_improvements',
        'portal_improvements',
    ],
    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Other',
    'data': [
        'views/res_partner.xml',
        'views/connection_mode.xml',
        'views/backup_type.xml',
        'views/menu_buttons.xml',
        'views/security_check.xml',
        'views/sale_subscription.xml',

        'security/security_check_security.xml',
        'security/ir.model.access.csv',

        'report/layouts.xml',
        'report/external_access_template.xml',
        'report/backups_template.xml',
        'report/access_rights_template.xml',
        'report/gate_access_template.xml',
        'report/servers_security_template.xml',
        'report/network_security_template.xml',
        'report/workstations_security_template.xml',
        'report/todos_template.xml',
        'report/complete_report_template.xml',
        'report/reports.xml',
    ],
}
