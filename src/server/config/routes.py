ROUTES = {
    'admin' : [
        # GUIDBOOKSKILLS
        {
            'method': ['GET'],
            'endpoint': 'views.guidebookskills',
            'function': 'get_guidebookskills'
        },
        # EXPERIMENT
        {
            'method': ['GET'],
            'endpoint': 'views.experiment',
            'function': 'get_experiment'
        }
    ],
    'v1': [
        {
            'summary': 'Admin Dashboard',
            'rule': '/guidebookskills',
            'method': ['PUT'],
            'endpoint': 'pmk_guidebookskills',
            'function': 'create_guidebookskills'
        },
        {
            'summary': 'Admin Dashboard',
            'rule': '/guidebookskills/<int:guidebookskills_id>',
            'method': ['GET'],
            'endpoint': 'pmk_guidebookskills',
            'function': 'get_guidebookskills'
        },
        {
            'summary': 'Admin Dashboard',
            'rule': '/guidebookskills',
            'method': ['GET'],
            'endpoint': 'pmk_guidebookskills',
            'function': 'get_guidebookskills_list',
            'opts': {
                'use_pagination': True
            }
        },
        {
            'summary': 'Admin Dashboard',
            'rule': '/guidebookskills/<int:guidebookskills_id>',
            'method': ['PATCH'],
            'endpoint': 'pmk_guidebookskills',
            'function': 'edit_guidebookskills',
            'opts': {
                'use_pagination': True
            }
        },
        {
            'summary': 'Admin Dashboard',
            'rule': '/guidebookskills/<int:guidebookskills_id>',
            'method': ['DELETE'],
            'endpoint': 'pmk_guidebookskills',
            'function': 'remove_guidebookskills',
            'opts': {
                'use_pagination': True
            }
        }
    ]
}