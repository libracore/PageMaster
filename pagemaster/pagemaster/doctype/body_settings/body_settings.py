# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BodySettings(Document):
	pass

@frappe.whitelist()
def updateValues(doctype, name, field, value):
	frappe.db.set_value(doctype, name, field, value, update_modified=False)