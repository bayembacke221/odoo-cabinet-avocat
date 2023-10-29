# -*- coding: utf-8 -*-
{
    'name':'Gestion Cabinet Avocat',
    'summary': "Gestion d’une agence de cabinet d'avocat",
    'description': 
    """Gestion d’une agence de cabinet d'avocat""",
    'author': "Mbacke Mbaye & Mage Seye",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base',],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/associe.xml',
    ],
    'demo': ['demo.xml'],
    'application': True ,
    'installable': True ,
    'auto_install': False,
    'sequence': 1,
}