{
    "name": "Inventory Report",
    "version": "2.0",
    "depends": ["stock"],
    "author": "mosiw",
    "category": "Inventory",
    "summary": "go the hell",
    "description": "inventory reporter / pdf",
    "data": [
        "report/report_inventory_request_template.xml",
        "views/report_action.xml",
        # "views/assets.xml",
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
