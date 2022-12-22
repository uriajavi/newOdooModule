# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    
    activities = fields.One2many('fct.task','pupil')
    fctdata = fields.Many2one('fct.data')
