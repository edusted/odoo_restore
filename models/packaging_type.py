from odoo import models, fields

class PackagingType(models.Model):
    _name = 'logistics.packaging_type'
    _description = 'Packaging Type'
    
    name = fields.Char(string='Packaging Name')
