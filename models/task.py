# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'fct.task'

    name = fields.Char(string='Name',required=True)
    date = fields.Date(string='Date',required=True)
    duration = fields.Float(string='Duration',required=True)
    description = fields.Text(string='Description',required=True)
    remarks = fields.Text(string='Remarks')
    
    pupil = fields.Many2one('res.users',string='Pupil',required=True)
