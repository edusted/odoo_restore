import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Product(models.Model):
    _name = 'logistics.product'
    _description = 'Product'

    request_id = fields.Many2one('logistics.transport_request', string="Transport Request")

    name_p = fields.Char(string='Product name')
    weight_p = fields.Float(string="Weight (kg)")
    quantity_p = fields.Integer(string="Quantity", default=1, required=True)
    dimensions_p = fields.Char(string="Dimensions (WxHxL) (cm)",help="Enter dimensions in the format: width x height x length")
    total_weight_p = fields.Float(string="Total weight (kg)", compute='_compute_total_weight', store=True)
    comments_p = fields.Text(string="Comments")

    @api.constrains('dimensions')
    def _check_dimensions(self):
        dimension_pattern = r'^\d+(\.\d+)? x \d+(\.\d+)? x \d+(\.\d+)?$'
        for record in self:
            if record.dimensions_p and not re.match(dimension_pattern, record.dimensions_p):
                raise ValidationError(
                    "Invalid dimensions format! Use the format: width x height x length (e.g., 10.5 x 20 x 15).")

    @api.depends('weight_p', 'quantity_p')
    def _compute_total_weight(self):
        for record in self:
            record.total_weight_p = record.weight_p * record.quantity_p

