# -*- coding: utf-8 -*-
{
    'name': "Material Listing",

    'description': """
        This module will be able to list the materials that will be sold.
    """,

    'author': "Muhardiansyah",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/material_listing_views.xml',
    ],
    
    'installable': True,
    'application': True,

}
