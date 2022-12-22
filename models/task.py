# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'fct.task'

    name = fields.Char()
    date = fields.Date()
    duration = fields.Float()
    description = fields.Text()
    remarks = fields.Text()
    
    pupil = fields.Many2one('res.users')
