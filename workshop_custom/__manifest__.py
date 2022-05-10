# Copyright 2015-TODAY Eficent
# - Jordi Ballester Alomar
# Copyright 2015-TODAY Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License: LGPL-3 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "WorkSphop custom",
    "summary": "An operating unit (OU) is an organizational entity part of a "
               "company",
    "version": "12.0.1.4.0",
    "author": "  , ",
    "category": "Generic",
    "depends": ["base","mail"],
    "license": "LGPL-3",
    "data": [
        "security/partnership_groups.xml",
        "security/ir.model.access.csv",
        "view/operating_unit_view.xml",

    ],
    'demo': [

    ],
    'installable': True,
    'application':True

}
