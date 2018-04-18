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
			   "name": "PageMaster Page",
			   "label": _("Sub Page"),
			   "description": _("Sub Page Setup")
			}
		]
	},
	{
		"label": _("News / Blog"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "PageMaster Blog Post",
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
			},
			{
			   "type": "doctype",
			   "name": "Page Box Set",
			   "label": _("Box Sets"),
			   "description": _("Box Setup")
			}
		]
	},
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
	},
	{
		"label": _("General Settings"),
		"icon": "fa fa-bookmark",
		"items": [
			{
			   "type": "doctype",
			   "name": "Head Settings",
			   "label": _("Header Settings"),
			   "description": _("Head Setup")
			},
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
			},
			{
			   "type": "doctype",
			   "name": "Google Analytics",
			   "label": _("Google Analytics"),
			   "description": _("Google Analytics Setup")
			}
		]
	}
]