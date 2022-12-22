# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Data(models.Model):
    _name = 'fct.data'

    end = fields.Date()
    start = fields.Date()
    
    pupils = fields.One2many('res.users','fctdata')
    company = fields.Many2one('res.company')
