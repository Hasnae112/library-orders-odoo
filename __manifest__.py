{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Summery',
    'description': 'Library ',
    'category': 'Library',
    'author': 'Author',
    'website': 'Website',
    'depends': ['base', 'mail', 'calendar', 'web'],
    'data': [

        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/menu.xml',  # ✅ TOUJOURS EN PREMIER

        'data/sequence_member_data.xml',
        'data/sequence_invoice_data.xml',
        'data/mail_template_data.xml',

        'report/library_invoice_templates.xml',
        'report/report.xml',

        'views/authors_views.xml',
        'views/books_views.xml',
        'views/categories_views.xml',
        'views/employees_views.xml',
        'views/invoice_views.xml',
        'views/member_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
