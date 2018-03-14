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
		   }
		]
	},
	{
		"label": _("Sub Pages"),
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
		"label": _("About Us"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "About Us",
			   "label": _("Setup"),
			   "description": _("About Us Setup")
			}
		]
	},
	{
		"label": _("General Data"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "Page Slideshow",
			   "label": _("Slideshows"),
			   "description": _("Slideshows Setup")
			},
			{
			   "type": "doctype",
			   "name": "Page Card Set",
			   "label": _("Card Sets"),
			   "description": _("Cards Setup")
			},
			{
			   "type": "doctype",
			   "name": "Media Set",
			   "label": _("Media Sets"),
			   "description": _("Medias Setup")
			},
			{
			   "type": "doctype",
			   "name": "Timeline Set",
			   "label": _("Timeline Sets"),
			   "description": _("Timeline Setup")
			}
		]
	}
]