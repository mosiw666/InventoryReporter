{
    "name": "Inventory Report",

    "version": "2.0.1",

    "depends": ["stock"],
    "author": "mosiw",
    "category": "Inventory",
    "summary": "Report for Inventory Request",
    "description": "inventory reporter / pdf",
    "data": [
        "report/report_inventory_request_template.xml",
        "report/report_inventory_request_template2.xml",
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
