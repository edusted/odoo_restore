{
    'name': 'odoo_logistics',
    'version': '1.0',
    'summary': 'Module for managing transport requests within the Logistics module.',
    'description': """
        This module allows for the creation and management of transport requests within the Logistics module.
    """,
    'author': 'Eduard Stsiablou',
    'category': 'Logistics',
    'depends': ['base', 'sale', 'hr', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/transport_request_views.xml',
        'views/request_type_views.xml',
        'views/packaging_type_views.xml',
        'views/expense_category_views.xml',
        'views/priority_type_views.xml',
        'views/menu_views.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
