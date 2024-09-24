from odoo import models, fields

class RequestType(models.Model):
    _name = 'logistics.request_type'
    _description = 'Request Type'
    
    name = fields.Char(string='Type Name', required=True, unique=True)
