import re
from importlib.resources import _
from odoo import models, fields, api
from odoo.exceptions import ValidationError



class TransportRequest(models.Model):
    _name = 'logistics.transport_request'
    _description = 'Transport Request'

    product_ids = fields.One2many('logistics.product', 'request_id', string="Products")

    name = fields.Char(string="Request Number", required=True, copy=False, readonly=True, default=lambda self: _(" "))
    is_own_transport = fields.Boolean(string="Own Transport")
    request_type_id = fields.Many2one('logistics.request_type', string="Request Type")
    sender_id = fields.Many2one('res.partner', string="Sender")
    sender_contact_id = fields.Many2one('res.partner', string="Sender Contact")
    receiver_id = fields.Many2one('res.partner', string="Receiver")
    receiver_contact_id = fields.Many2one('res.partner', string="Receiver Contact")
    responsible_manager_id = fields.Many2one('hr.employee', string="Responsible Manager")
    responsible_logistician_id = fields.Many2one('hr.employee', string="Responsible Logistician")
    request_date = fields.Date(string="Request Date")
    comments = fields.Text(string="Comments")
    package_type_id = fields.Many2one('logistics.packaging_type', string="Package Type")
    package_quantity = fields.Integer(string="Package Quantity")
    # total_weight = fields.Float(string="Total Weight (kg)", compute = '_compute_total_weight', store = True )
    # total_volume = fields.Float(string="Total Volume", compute = '_compute_total_volume', store = True)
    has_carry_service = fields.Boolean(string="Carry Service", default = False)
    floor_number = fields.Integer(string="Floor Number")
    priority_id = fields.Many2one('logistics.priority_type', string="Priority")
    delivery_date = fields.Date(string="Delivery Date")
    delivery_time_start = fields.Float(string="Delivery Time From")
    delivery_time_end = fields.Float(string="Delivery Time To")
# Вкладка Забор/Доставка
    transport_type = fields.Selection([('pickup', 'Pickup'), ('delivery', 'Delivery')], string="Type", required=True)
    date_time = fields.Datetime(string="Date/time", required=True)
    partner_id = fields.Many2one('res.partner', string="Pickup point", required=True)
    street = fields.Char(string="Street", related='partner_id.street', readonly=True)
    city = fields.Char(string="City", related='partner_id.city',readonly=True)
    zip_code = fields.Char(string="ZIP", related='partner_id.zip',readonly=True)
    country_id = fields.Many2one('res.country', string="Country", related='partner_id.country_id', readonly=True)
# Вкладка Перевозчики
    carrier = fields.Char(string = "Carrier")
    delivery = fields.Date(string = "Delivery Date")
    cost = fields.Float(string = "Cost")
    service_type = fields.Char(string = "Service Type")
# Вкладка Стоимость
    expense_category = fields.Many2many("logistics.expense_category", string = "Expense Category")
    # cost_exp = fields.Float(string = "Cost")
    # comments_exp = fields.Text(string = "Comments")
# Вкладка Состав заявки
    product_id = fields.Many2many('product.product', string="Product", required=True)
    # weight = fields.Float(string="Weight")
    # quantity = fields.Integer(string="Quantity", default=1, required=True)
    # dimensions = fields.Char(string="Dimensions (WxHxL)", help="Enter dimensions in the format: width x height x length")
    # total_weight_req = fields.Float(string="Total weight", compute='_compute_total_weight', store=True)
    # comments_req = fields.Text(string="Comments")

    # @api.depends('package_quantity', 'package_type_id')
    # def _compute_totals(self):
    #     for record in self:
    #         record.total_weight = record.package_quantity * 23.5
    #         record.total_volume = record.package_quantity * 0.1

    @api.model_create_multi
    def create(self, vals_list):
        """Sets sequence code to name"""
        for vals in vals_list:
            if vals.get("name", _("New")) == _("New"):
                vals["name"] = self.env["ir.sequence"].next_by_code("logistics.transport_request") or _(" ")
        return super().create(vals_list)


    def action_create_invoice(self):
            return {
                'type': 'ir.actions.act_window',
                'name': 'Transport Requests',
                'view_mode': 'tree,form',
                'res_model': 'logistics.transport_request',
                # 'target': 'current',
            }



    # def action_create_route(self):
    #     pass

    # @api.depends('product_id')
    # def _compute_dimensions(self):
    #     for record in self:
    #         if record.product_id:
    #             record.dimensions = f"{record.product_id.width} x {record.product_id.length}"
    #         else:
    #             record.dimensions = ""



    @api.constrains('dimensions')
    def _check_dimensions(self):
        dimension_pattern = r'^\d+(\.\d+)? x \d+(\.\d+)? x \d+(\.\d+)?$'
        for record in self:
            if record.dimensions and not re.match(dimension_pattern, record.dimensions):
                raise ValidationError(
                    "Invalid dimensions format! Use the format: width x height x length (e.g., 10.5 x 20 x 15).")

    # @api.depends('product_ids.weight_p', 'product_ids.quantity_p')
    # def _compute_total_weight(self):
    #     for record in self:
    #         total_weight = 0.0
    #         for product in record.product_ids:
    #             total_weight += product.weight_p * product.quantity_p
    #         record.total_weight = total_weight

