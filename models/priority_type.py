from odoo import models, fields

class PriorityType(models.Model):
    _name = 'logistics.priority_type'
    _description = 'Priority Type'
    
    name = fields.Char(string='Priority Name', required=True, unique=True)
