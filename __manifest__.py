# -*- coding: utf-8 -*-
{
    'name': "Vocational Training Practices.",

    'summary': """
        Application for managing pupil´s practices in companies.""",

    'description': """
        Allows:
            -Creation and management of pupil activities.
            -Follow up for managers.
            -Report generation and printing for practices management,
    """,

    'author': "DAM Tartanga",
    'website': "http://www.tartanga.eus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}