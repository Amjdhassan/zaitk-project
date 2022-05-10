# Copyright 2015-TODAY Eficent
# - Jordi Ballester Alomar
# Copyright 2015-TODAY Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError



class OperatingUnit(models.Model):

    _name = 'operating.unit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Operating Unit'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    active = fields.Boolean('Active', default=True)
    tec_id = fields.One2many('custom.technicians','tec_line_id',string='technicians')
    partner_id = fields.Many2one('res.partner', string="Customer")
    area_id = fields.Many2one('custom.area', string="Area")


class Technicians(models.Model):
        _name = 'custom.technicians'
        _description = 'New technicians '


        name = fields.Char(string='Name')
        phone = fields.Char('Phone')
        tec_line_id = fields.Many2one('operating.unit',string='ID')


class Area_work(models.Model):
    _name = 'custom.area'
    _description = 'New area '

    name = fields.Char(string='Name')
    descrb = fields.Char('description')







