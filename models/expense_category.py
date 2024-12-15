from odoo import models, fields

class ExpenseCategory(models.Model):
    _name = 'logistics.expense_category'
    _description = 'Expense Category'
    
    name = fields.Char(string='Expense Category Name')
    cost_exp = fields.Float(string="Cost")
    comments_exp = fields.Text(string = "Comments")
