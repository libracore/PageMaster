from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
	{
		"label": _("Dashboard Settings"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "PageMaster Dashboard",
			   "label": _("Dashboard"),
			   "description": _("Dashboard Setup")
			},
			{
			   "type": "doctype",
			   "name": "PageMaster Dashboard Item",
			   "label": _("Charts"),
			   "description": _("Charts Setup")
			}
		]
	}
]