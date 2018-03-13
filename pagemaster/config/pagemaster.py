from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
	{
		"label": _("Main Page"),
		"icon": "fa fa-bookmark",
		"items": [
		   {
			   "type": "doctype",
			   "name": "Main Page Setup",
			   "label": _("Setup"),
			   "description": _("Setup Tools for the Main Page")
		   },
		   {
			   "type": "doctype",
			   "name": "Page Slideshow",
			   "label": _("Slideshow"),
			   "description": _("Slideshows Setup")
			}
		]
	},
	{
		"label": _("Sub Page"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "Page Slideshow",
			   "label": _("Slideshow"),
			   "description": _("Slideshows Setup")
			}
		]
	},
	{
		"label": _("General"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "Page Slideshow",
			   "label": _("Slideshow"),
			   "description": _("Slideshows Setup")
			},
			{
			   "type": "doctype",
			   "name": "Page Cards",
			   "label": _("Cards"),
			   "description": _("Cards Setup")
			}
		]
	}
]