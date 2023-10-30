from odoo import models, fields, api

class Associe(models.Model):
    _name = 'avocat.associe'
    _description = "Liste des associes"

    nom = fields.Char(required=True)
    prenom = fields.Char(required=True)
    sexe = fields.Selection(selection=[('M', 'Homme'), ('F', 'Femme')])
    fonction_associee_id = fields.Many2one('avocat.fonction', string="Fonction Associée")
    fonction_associee_nom = fields.Char(string="Fonction Associée", compute="_compute_fonction_associee_nom")

    @api.depends('fonction_associee_id')
    def _compute_fonction_associee_nom(self):
        for record in self:
            if record.fonction_associee_id:
                record.fonction_associee_nom = record.fonction_associee_id.nom
            else:
                record.fonction_associee_nom = ""


