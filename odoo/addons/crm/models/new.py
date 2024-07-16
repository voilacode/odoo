from odoo import fields, models

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    lead_type = fields.Selection([
        ('enquiry', 'Enquiry'),
        ('feedback', 'Feedback'),
        ('issue', 'Issue')
    ], string='Lead Type', required=True)