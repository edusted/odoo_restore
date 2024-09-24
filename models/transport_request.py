from odoo import models, fields, api

class TransportRequest(models.Model):
    _name = 'logistics.transport_request'
    _description = 'Transport Request'
    
    name = fields.Char(string='Request Name', required=True)
    request_type = fields.Many2one('logistics.request_type', string='Request Type')
    sender_id = fields.Many2one('res.partner', string='Sender')
    receiver_id = fields.Many2one('res.partner', string='Receiver')
    responsible_manager_id = fields.Many2one('hr.employee', string='Responsible Manager')
    status = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('shipped', 'Shipped')], default='draft')
    package_type_id = fields.Many2one('logistics.packaging_type', string='Package Type')
    package_qty = fields.Integer(string='Package Quantity')
    priority_id = fields.Many2one('logistics.priority_type', string='Priority')
    total_weight = fields.Float(string='Total Weight')
    total_volume = fields.Float(string='Total Volume')

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        # Логика для подтверждения запроса
        self.status = 'confirmed'  
        return True

    @api.multi
    def action_cancel(self):
        self.ensure_one()
        # Логика для отмены запроса
        self.status = 'draft'  # Или 'canceled', в зависимости от вашей логики
        return True

