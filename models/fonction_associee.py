from odoo import models, fields, api

class FonctionAssociee(models.Model):
    _name = 'avocat.fonction'
    _description = "Liste des fonctions associees"

    nom = fields.Char(required=True)
    liste_associe_ids = fields.One2many('avocat.associe', 'fonction_associee_id', string="Liste des Associés")
    nbr_associe = fields.Integer(compute='_compute_nbr_associe', store=True)

    
    def _compute_nbr_associe(self):
        self.nbr_associe = self.env['avocat.associe'].search_count([('fonction_associee_id','=',self.id)])
