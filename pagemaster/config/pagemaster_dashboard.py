from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
	{
		"label": _("Main Pages"),
		"icon": "fa fa-bookmark",
		"items": [
		   {
			   "type": "doctype",
			   "name": "ttt",
			   "label": _("ttt"),
			   "description": _("Setup Tools for the Main Page")
		   }
		]
	}
]