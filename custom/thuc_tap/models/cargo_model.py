from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Cargo(models.Model):
    _name = "manage.cargo"
    _description = "Cargo"

    code = fields.Char(String='code')

    name = fields.Char(String='Name')

    total_weight = fields.Float(String='Total weight')

    length = fields.Float(String='Length')

    weight = fields.Float(String='Weight')

    height = fields.Float(String='Height')

    from_depot = fields.Float(String='From')

    to_depot = fields.Float(String='To')

    total_distance = fields.Float(String='Total distance')

    bidding_package_id = fields.Char(String='Bidding package')

    size_standard_id = fields.Char(String='Size standard')
