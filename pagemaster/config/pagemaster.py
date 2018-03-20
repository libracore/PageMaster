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
			   "name": "Main Page Setup",
			   "label": _("Main Page"),
			   "description": _("Setup Tools for the Main Page")
		   },
		   {
			   "type": "doctype",
			   "name": "About Us",
			   "label": _("About Us"),
			   "description": _("About Us Setup")
			},
			{
			   "type": "doctype",
			   "name": "PageMaster Contact",
			   "label": _("Contact"),
			   "description": _("Contact Setup")
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
			   "label": _("Has to be programmed!"),
			   "description": _("Slideshows Setup")
			}
		]
	},
	{
		"label": _("News / Blog"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "Blog Post",
			   "label": _("Posts"),
			   "description": _("News / Blog Post")
			},
			{
			   "type": "doctype",
			   "name": "Blog Settings",
			   "label": _("Settings"),
			   "description": _("News / Blog Settings")
			},
			{
			   "type": "doctype",
			   "name": "Blog Category",
			   "label": _("Categories"),
			   "description": _("News / Blog Categories")
			}
		]
	},
	{
		"label": _("Bootstrap Modules"),
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
	},
	{
		"label": _("General Settings"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "Navbar",
			   "label": _("Navbar Settings"),
			   "description": _("Navbar Setup")
			},
			{
			   "type": "doctype",
			   "name": "Body Settings",
			   "label": _("Body Settings"),
			   "description": _("Body Setup")
			},
			{
			   "type": "doctype",
			   "name": "PageMaster Footer",
			   "label": _("Footer Settings"),
			   "description": _("Footer Setup")
			}
		]
	},
]