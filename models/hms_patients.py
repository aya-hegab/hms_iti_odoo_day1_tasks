from odoo import models, fields

class HMSPatient(models.Model):
  _name='hms.patient'

  firstName = fields.Char()
  lastName = fields.Char()
  age = fields.Integer()
  bloodType = fields.Selection([('a','A'),('b','B'),('o','O')])
  birthDate = fields.Date()
  history = fields.Html()
  crRatio = fields.Float()
  address = fields.Text()
  pcr = fields.Boolean()
  image = fields.Image()