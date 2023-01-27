# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions 


class Task(models.Model):
    _name = 'fct.task'

    name = fields.Char(string='Name',required=True)
    date = fields.Date(string='Date',required=True)
    duration = fields.Float(string='Duration',required=True)
    description = fields.Text(string='Description',required=True)
    remarks = fields.Text(string='Remarks')
    
    pupil = fields.Many2one('res.users',string='Pupil',required=True)


    @api.constrains('date')
    def _validate_date(self):
        for task in self:
            if fields.Date.from_string(task.date) > fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be greater than today's.")

    @api.onchange('date')
    def _onchange_date(self):
            if fields.Date.from_string(self.date) > fields.Date.from_string(fields.Date.today()):
                return {
                    'warning': {
                            'title': "Error on date",
                            'message': "Date cannot be greater than today's.",
                            }
                    }
    
    @api.constrains('duration')
    def _validate_duration(self):
        for task in self:
            if task.duration < 0.0:
                raise exceptions.ValidationError("Duration cannot be negative.")
            if task.duration > 8.0:
                raise exceptions.ValidationError("Duration for a day's task cannot be greater than 8 hours.")        
        
    @api.onchange('duration')
    def _onchange_duration(self):
        if self.duration < 0.0 or self.duration > 8.0:
            return {
               'warning': {
                    'title': "Error on duration",
                    'message': "Cannot be greater than 8 hours, 0 or negative!!",
                    }
            }
        

        
        
        
        
        
        