# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "PageMaster",
			"color": "green",
			"icon": "octicon octicon-mention",
			"type": "module",
			"link": "#modules/PageMaster",
			"label": _("PageMaster")
		},
		{
			"module_name": "PageMaster Dashboard",
			"color": "green",
			"icon": "fa fa-line-chart",
			"type": "module",
			"link": "/dashboard",
			"label": _("Dashboard")
		}
	]