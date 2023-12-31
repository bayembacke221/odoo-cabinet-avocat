# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from odoo.exceptions import ValidationError

class Notaire(models.Model):
    _name = 'avocat.notaire'
    _description = "Liste notaires"

    id = fields.Integer(required=True, autoincrement=True)
    nom = fields.Char(string='Nom',required=True)
    prenom = fields.Char(string='Prénom',required=True)
    sexe = fields.Selection([('male', 'Masculin'),('female', 'Féminin'),], 
        required=False, default='male', tracking=True, string="Sexe")
    type = fields.Selection(selection=[('Notaire associé', 'Notaire associé'), ('Notaire associé principal', 'Notaire associé principal'), ('Notaire gérant', 'Notaire gérant')])
    date_integration = fields.Date()
    fonction_associee = fields.Many2one('avocat.fonction', string="Fonction Associée")
    fonction_associee_nom = fields.Char(string="Fonction Associée", compute="_compute_fonction_associee_nom")

    @api.depends('fonction_associee')
    def _compute_fonction_associee_nom(self):
        for record in self:
            if record.fonction_associee:
                record.fonction_associee_nom = record.fonction_associee.nom
            else:
                record.fonction_associee_nom = ""
