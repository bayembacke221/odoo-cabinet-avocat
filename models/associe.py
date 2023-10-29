from odoo import models, fields
class Associe(models.Model):
    _name = 'avocat.associe'

    id = fields.Integer(required=True, autoincrement=True)
    nom = fields.Char(required=True)
    prenom = fields.Char(required=True)
    sexe = fields.Selection(selection=[('M', 'Homme'), ('F', 'Femme')])
    fonction_associee = fields.Many2one('avocat.fonction')