from odoo import models, fields
class Fonction(models.Model):
    _name = 'avocat.fonction'

    id = fields.Integer(required=True, autoincrement=True)
    nom = fields.Char(required=True)
    nbr_associe = fields.Integer(required=True)
    liste_associe = fields.Many2many('avocat.associe')