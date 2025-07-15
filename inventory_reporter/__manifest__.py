{
    "name": "Inventory Report",
    "version": "1.0.1",
    "depends": ["stock"],
    "author": "Mosiw, Erfan",
    "category": "Inventory",
    "summary": "go to the hell",
    "description": "inventory reporter / pdf",
    "data": [
        "report/report_inventory_request_template.xml",
        "views/report_action.xml",
    ],
    'assets': {
        'web.report_assets_common': [
            'inventory_reporter/static/src/css/report_styles.css',
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
