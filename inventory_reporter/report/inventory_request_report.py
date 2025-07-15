from odoo import models

class InventoryRequestReport(models.AbstractModel):
    _name = 'inventory_request_report'
    _description = 'Inventory Request Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'stock.picking',
            'docs': docs,
        }
